from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.rules import CanReachRegion, Has, HasFromList, Rule

from .items import ITEM_NAME_TO_ID
from .locations import LOCATION_NAME_TO_ID


if TYPE_CHECKING:
    from .world import UncannyCatWorld

"""
[NR] means not required, [NRP] means not required for peak
All gimmicks are logically required for peaks unless specified
World 0: N/A

World 1:
1-1: N/A
1-2: N/A
1-3: N/A
1-4: Breakable Tiles
1-5: Breakable Tiles
1-6: Breakable Tiles (maybe possible without?)
1-7: Breakable Tiles
1-8: N/A
1-9: N/A
1-10: N/A
1-11: N/A
1-12: N/A
1-13: Keys
1-14: Keys
1-15: Keys
1-16: Keys
1-17: Keys
1-18: N/A

World 2:
2-1: N/A
2-2: Stop Markers [NR, NRP]
2-3: Stop Markers [NR, NRP]
2-4: Go Markers [NR]
2-5: Keys, Go Markers [NR], Stop Markers [NR]
2-6: Breakable Tiles, Go Markers [NR], Stop Markers [NR]
2-7: Stop Markers [NR, NRP]
2-8: Stop Markers [NR], Go Markers [NR]
2-9: Stop Markers [NR], Go Markers [NR]
2-10: Jump Pads, Go Markers [NR, NRP]
2-11: Keys, Breakable Tiles, Jump Pads, Go Markers
2-12: N/A
2-13: Keys, Jump Pads, Go Markers [NR], Stop Markers [NR]
2-14: Keys, Breakable Tiles [NR], Jump Pads [NR], Go Markers [NR], Stop Markers [NR]
2-15: Keys, Jump Pads, Stop Markers [NR], Go Markers [NR]
2-16: Jump Pads, Stop Markers [NR], Go Markers [NR]
2-17: Keys, Jump Pads, Stop Markers [NR]
2-18: Jump Pads

World 3:
3-1: N/A
3-1 Yellow Smiley: N/A
3-2: Breakable Tiles, Stop Markers [NR]
3-2 Yellow Smiley: N/A
3-3: Switch Tiles
3-4: Switch Tiles
3-5: Keys, Breakable Tiles [NR]
3-5 Yellow Smiley: N/A
3-6: Breakable Tiles
3-7: Keys, Switch Tiles [NR, NRP], Jump Pads [NR], Stop Markers [NR], Go Markers [NR]
3-7 Yellow Smiley: Keys, Stop Markers
3-8: Breakable Tiles
3-9: Breakable Tiles
3-10: N/A
3-11: Keys, Jump Pads
3-11 Red Smiley: N/A
3-11 Green Smiley: N/A
3-11 Blue Smiley: N/A
3-11 Yellow Smiley: Keys, Jump Pads
3-12: Switch Tiles, Stop Markers [NR], Go Markers [NR]
3-12 Red Smiley: N/A
3-12 Yellow Smiley: Switch Tiles
3-12 Green Smiley: Switch Tiles
3-12 Blue Smiley: Switch Tiles
3-12 Orange Smiley: Switch Tiles, Go Markers, Stop Markers
3-13: Dog, Switch Tiles
3-14: Dog, Switch Tiles [NR]
3-15: Dog, Switch Tiles
3-16: Dog
3-16 Red Smiley: Dog
3-17: Keys, Dog, Jump Pads, Go Markers [NR], Stop Markers [NR], Switch Tiles: [NR, NRP]
3-17 Yellow Smiley: Dog, Jump Pads
3-17 Blue Smiley: Dog, Jump Pads
3-18: Jump Pads

World 4:
4-1: Breakable Tiles [NR, NRP]
4-2: Switch Tiles
4-3: Portals
4-4: Portals, Stop Markers [NR, NRP], Go Markers [NR, NRP], Switch Tiles [NR, NRP]
4-5: Switch Tiles
4-6: Portals, Jump Pads
4-7: Dog, Jump Pads [NR], Go Markers [NR], Stop Markers [NR, NRP], Nuke [NR, NRP]
4-8: Nuke, Stop Markers, Switch Tiles
4-9: Jump Pads, Stop Markers, Keys [NRP], Nuke [NRP]
4-10: Dog
4-11: Dog, Breakable Tiles
4-12: Keys, Jump Pads
4-13: Breakable Tiles
4-14: Keys
4-15: Keys, Stop Markers [NR, NRP]
4-16: Breakable Tiles, Nukes
4-17: Switch Tiles, Portals, Stop Markers [NR]
4-18: N/A (remove the wall barrier)

World 5:
5-1: N/A
5-2: N/A
5-3: N/A
5-4: Golf Balls
5-5: Golf Balls
5-6: Breakable Tiles, Golf Balls
5-7: Golf Balls
5-8: Golf Balls
5-9: Breakable Tiles, Golf Balls
5-10: Breakable Tiles, Golf Balls, Go Markers [NR], Stop Markers [NR]
5-11: Golf Balls, Jump Pads
5-12: Golf Balls, Switch Tiles
5-12 Blue Smiley: N/A
5-13: Golf Balls
5-14: Golf Balls, Switch Tiles, Nuke
5-15: Golf Balls, Portal OR Jump Pad (Peak requires both)
5-16: Golf Balls
5-17: Golf Balls
5-18: Landmines

World P:
P-1: N/A (remove the wall barrier)
P-2: Keys, Jump Pads, Breakable Tiles [NR, NRP], Go Markers [NR, NRP]
P-3: Switch Tiles, Stop Markers [NR], Go Markers [NR, NRP]
P-4: Switch Tiles
P-5: Breakable Tiles, Stop Markers [NR], Go Markers [NR, NRP]
P-6: Metronome
P-7: Metronome, Switch Tiles
P-8: Metronome, Portals
P-9: Metronome
P-10: Metronome, Keys, Nuke [NR, NRP]
P-11: Metronome, Portals
P-11 Yellow Smiley: Metronome, Portals
P-12: Switch Tiles, Jump Pads
P-13: N/A
P-14: N/A
P-15: Portals, Breakable Tiles, Keys
P-15 Yellow Smiley: Portals, Breakable Tiles, Keys
P-16: Keys, Jump Pads, Go Markers
P-17: Keys, Breakable Tiles, Switch Tiles, Stop Markers, Nuke, Dog, Metronome, Go Markers [NR]
P-17 Yellow Smiley: Keys, Breakable Tiles, Switch Tiles, Stop Markers
P-18: N/A

World E:
E-0: N/A
E-1: Keys
E-2: N/A
E-3: Switch Tiles, Jump Pads, Go Markers [NR, NRP]
E-4: Portals, Jump Pads, Breakable Tiles, Go Markers [NR]
"""


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


def set_all_location_rules(world: UncannyCatWorld) -> None:
    def rule(name: str, r) -> None:
        try:
            world.set_rule(world.get_location(name), r)
        except KeyError:
            return

def set_completion_condition(world: UncannyCatWorld) -> None:
    # TODO: ADD
    pass