from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import TYPE_CHECKING, override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from Options import OptionError
from rule_builder.rules import CanReachRegion, Has, HasFromList, Rule, And, HasAll, True_

from . import items
from .items import GOAL_LEVEL, ITEM_GROUPS
from .locations import LOCATION_DATA, get_excluded_locations, level_item_name


if TYPE_CHECKING:
    from .world import UncannyCatWorld

@dataclass
class OutOfLogic(Rule["UncannyCatWorld"], game="Uncanny Cat Golf"):
    description: str

    class Resolved(Rule.Resolved):
        glitches_item_name: str
        player: int
        description: str
        skip_cache = True

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.has(self.glitches_item_name, self.player)

        @override
        def item_dependencies(self):
            yield self.glitches_item_name, self.player

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            return [{"text": f"Glitch: {self.description}", "color": "magenta"}]

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            return f"Glitch: {self.description}"

    @override
    def _instantiate(self, world: "UncannyCatWorld") -> "OutOfLogic.Resolved":
        return OutOfLogic.Resolved(
            glitches_item_name=world.glitches_item_name,
            player=world.player,
            description=self.description,
        )

def set_all_rules(world: UncannyCatWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def gimmick_rule(requirements: list[str]) -> Rule[UncannyCatWorld] | None:
    """Turn a requirement list into one rule. "A|B is just an OR."""
    all_of = [req for req in requirements if "|" not in req]
    either_of = [HasFromList(*req.split("|")) for req in requirements if "|" in req]
    if not all_of and not either_of:
        return None
    return And(HasAll(*all_of), *either_of)


def location_rule(world: UncannyCatWorld, location_name: str) -> Rule[UncannyCatWorld] | None:
    _loc_id, requirements = LOCATION_DATA[location_name]
    parts: list[Rule[UncannyCatWorld]] = []

    unlock = items.unlock_item_name(world, level_item_name(location_name))
    if unlock is not None:
        parts.append(Has(unlock))
    if world.options.gimmick_lock:
        gimmicks = gimmick_rule(requirements)
        if gimmicks is not None:
            parts.append(gimmicks)

    return And(*parts) if parts else None


def set_all_location_rules(world: UncannyCatWorld) -> None:
    for location_name in LOCATION_DATA:
        rule = location_rule(world, location_name)
        if rule is None:
            continue
        try:
            location = world.get_location(location_name)
        except KeyError:
            continue  
        world.set_rule(location, rule)

    set_location_rule_exceptions(world)


def set_location_rule_exceptions(world: UncannyCatWorld) -> None:
    """Glitched logic stuff goes here"""
    def rule(name: str, r: Rule[UncannyCatWorld]) -> None:
        try:
            world.set_rule(world.get_location(name), r)
        except KeyError:
            return

    # EXAMPLE v
    # rule(
    #    "1-6: Roundabout Complete",
    #    Has("1-6: Roundabout")
    #    & (Has("Breakable Tiles") | OutOfLogic("1-6 can be cleared without breaking tiles")),
    #)

def levels_per_unlock_item(world: UncannyCatWorld) -> dict[str, int]:
    """How many playable levels each unlock item in the pool grants. One each under individual unlocks."""
    excluded = get_excluded_locations(world)
    levels_by_unlock: dict[str, set[str]] = {}
    for location_name in LOCATION_DATA:
        if location_name in excluded:
            continue
        level = level_item_name(location_name)
        unlock = items.unlock_item_name(world, level)
        if unlock is not None:
            levels_by_unlock.setdefault(unlock, set()).add(level)
    return {unlock: len(levels) for unlock, levels in levels_by_unlock.items()}


def has_enough_prisms(world: UncannyCatWorld) -> Rule[UncannyCatWorld] | None:
    prisms_per_level = 5 if world.options.peak_checks else 4
    levels_needed = ceil(world.options.prism_unlock_amount.value / prisms_per_level) - 5  # world 0 is free
    if levels_needed <= 0:
        return None
    unlocks = levels_per_unlock_item(world)
    total = 0
    for count, levels in enumerate(sorted(unlocks.values()), start=1):
        total += levels
        if total >= levels_needed:
            return HasFromList(*unlocks, count=count)
    raise OptionError(f"Uncanny Cat Golf ({world.player_name}): prism requirement exceeds available levels")


def set_completion_condition(world: UncannyCatWorld) -> None:
    goal = GOAL_LEVEL[world.options.goal_level.value]
    parts: list[Rule[UncannyCatWorld]] = []

    if world.options.gimmick_lock:
        gimmicks = gimmick_rule(LOCATION_DATA[f"{goal} Complete"][1])
        if gimmicks is not None:
            parts.append(gimmicks)

    prisms = has_enough_prisms(world)
    if prisms is not None:
        parts.append(prisms)

    world.set_rule(world.get_location("Victory"), And(*parts) if parts else True_())
    world.set_completion_rule(Has("Victory"))
