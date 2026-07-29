from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from Options import OptionError


if TYPE_CHECKING:
    from .world import UncannyCatWorld

BASE_ID = 100

GOAL_LEVEL = {0: "3-18: The Chuckle Coaster", 1: "4-17: CATaclysmic CATastrophe",
              2: "5-18: The End Is Neigh.", 3: "P-17: One Last Huzzah"}

# Every item must have a unique integer ID associated with it.
ITEM_NAME_TO_ID = {
    # Levels
    "1-1: Welcome to GOLF CENTRAL!": BASE_ID + 100,
    "1-2: Getting Around": BASE_ID + 101,
    "1-3: A New Angle": BASE_ID + 102,
    "1-4: Breakthrough!": BASE_ID + 103,
    "1-5: Right up my Alley": BASE_ID + 104,
    "1-6: Roundabout": BASE_ID + 105,
    "1-7: Bunker Funk": BASE_ID + 106,
    "1-8: Bony Cronies": BASE_ID + 107,
    "1-9: Kitty Litter": BASE_ID + 108,
    "1-10: Double Trouble": BASE_ID + 109,
    "1-11: Triple Trouble": BASE_ID + 110,
    "1-12: An Absurd Amount of Trouble": BASE_ID + 111,
    "1-13: The Key to Success": BASE_ID + 112,
    "1-14: Ooooh, Pretty Colors": BASE_ID + 113,
    "1-15: Almost a Cakewalk": BASE_ID + 114,
    "1-16: Silly Yard": BASE_ID + 115,
    "1-17: Scattered Around": BASE_ID + 116,
    "1-18: Rest Stop": BASE_ID + 117,
    "2-1: Welcome to GLOWSTICK CITY!": BASE_ID + 200,
    "2-2: Stop Right There!": BASE_ID + 201,
    "2-3: Parking Lot": BASE_ID + 202,
    "2-4: Just Zoomin' By": BASE_ID + 203,
    "2-5: Stop 'n' Start": BASE_ID + 204,
    "2-6: Backstreet Skullz": BASE_ID + 205,
    "2-7: Look Both Ways": BASE_ID + 206,
    "2-8: Dimlit District": BASE_ID + 207,
    "2-9: This is A Mugging": BASE_ID + 208,
    "2-10: jump pad introductary level": BASE_ID + 209,
    "2-11: Heist To Meet You": BASE_ID + 210,
    "2-12: Highway Getaway!": BASE_ID + 211,
    "2-13: Brawl In The Big City": BASE_ID + 212,
    "2-14: Waiter! There's Slop In My Soup!": BASE_ID + 213,
    "2-15: Back In The Back Alley": BASE_ID + 214,
    "2-16: Trickshot!": BASE_ID + 215,
    "2-17: Baby Vegas": BASE_ID + 216,
    "2-18: Good Night, Glowstick City": BASE_ID + 217,
    "3-1: Welcome to CHUCKLE PARK!": BASE_ID + 300,
    "3-2: Chuckle-Go-Round": BASE_ID + 301,
    "3-3: Switch It Up!": BASE_ID + 302,
    "3-4: JumbleHouse": BASE_ID + 303,
    "3-5: Titular Chuckles": BASE_ID + 304,
    "3-6: Cleanup On Aisle 2!": BASE_ID + 305,
    "3-7: Chuckles Inc.": BASE_ID + 306,
    "3-8: How Many Licks...": BASE_ID + 307,
    "3-9: House of Mirrors": BASE_ID + 308,
    "3-10: You Bring a Light?": BASE_ID + 309,
    "3-11: Four Leaf Marathon": BASE_ID + 310,
    "3-12: Pursuit of Happiness": BASE_ID + 311,
    "3-13: UNCANNY DOG GOLF": BASE_ID + 312,
    "3-14: Canny's Best Friend": BASE_ID + 313,
    "3-15: UNCANNY DOG GOLF but with a cat instead of a dog": BASE_ID + 314,
    "3-16: He Shoots! He scores!": BASE_ID + 315,
    "3-17: Racetrack Chasetrack": BASE_ID + 316,
    "3-18: The Chuckle Coaster": BASE_ID + 317,
    "4-1: Welcome to THE FINAL FRONTIER.": BASE_ID + 400,
    "4-2: No Time 4 Messing Around": BASE_ID + 401,
    "4-3: Now You're Thinking With Portal": BASE_ID + 402,
    "4-4: Wholesome DIY": BASE_ID + 403,
    "4-5: Cube Town": BASE_ID + 404,
    "4-6: Jumbling Labrynth": BASE_ID + 405,
    "4-7: Production Room": BASE_ID + 406,
    "4-8: On Heavens No The Chuckles Are Plentiful": BASE_ID + 407,
    "4-9: Uncanny Valley": BASE_ID + 408,
    "4-10: Dog Patrol": BASE_ID + 409,
    "4-11: The Really Cool Mining Level": BASE_ID + 410,
    "4-12: Weather Alert": BASE_ID + 411,
    "4-13: The Downfall": BASE_ID + 412,
    "4-14: I Saw This In A Movie Once": BASE_ID + 413,
    "4-15: Abandoned Workspace": BASE_ID + 414,
    "4-16: Crimson Outpost": BASE_ID + 415,
    "4-17: CATaclysmic CATastrophe": BASE_ID + 416,
    "4-18: The Wall": BASE_ID + 417,
    "5-1: Elysian Fields.": BASE_ID + 500,
    "5-2: ...": BASE_ID + 501,
    "5-3: ..?": BASE_ID + 502,
    "5-4: The Horse Is Here.": BASE_ID + 503,
    "5-5: Unstable": BASE_ID + 504,
    "5-6: Close Encounters Of The Equine Kind": BASE_ID + 505,
    "5-7: Late to the Party": BASE_ID + 506,
    "5-8: Megaton Of Skeleton": BASE_ID + 507,
    "5-9: Neigh Impossible": BASE_ID + 508,
    "5-10: Move It Or Lose It": BASE_ID + 509,
    "5-11: Why Is There A Highway Here?!?!": BASE_ID + 510,
    "5-12: Two Face Temple": BASE_ID + 511,
    "5-13: What Is This, A Crossover Episode?": BASE_ID + 512,
    "5-14: Containment Breach": BASE_ID + 513,
    "5-15: Hoppin' Mad": BASE_ID + 514,
    "5-16: The Wizard of Gimmica Strikes!!": BASE_ID + 515,
    "5-17: Perilous Plinko": BASE_ID + 516,
    "5-18: The End Is Neigh.": BASE_ID + 517,
    "P-1: Welcome to...?": BASE_ID + 600,
    "P-2: Welcome to COSMIC CHAMPIONSHIP!!": BASE_ID + 601,
    "P-3: Avoid the Void": BASE_ID + 602,
    "P-4: I Couldn't Beat This One :(": BASE_ID + 603,
    "P-5: Starstorm!": BASE_ID + 604,
    "P-6: Oh My Goodness, This Beat Is So Hard": BASE_ID + 605,
    "P-7: Ourple": BASE_ID + 606,
    "P-8: Get In The Groove!": BASE_ID + 607,
    "P-9: Neon Hopscotch": BASE_ID + 608,
    "P-10: Claustrophobia": BASE_ID + 609,
    "P-11: Beat The Beat The Beat The Beat The Beat": BASE_ID + 610,
    "P-12: JumbleRAVE!!": BASE_ID + 611,
    "P-13: where are you going come back": BASE_ID + 612,
    "P-14: Sea of Lies": BASE_ID + 613,
    "P-15: Santa's Revenge (What!!!)": BASE_ID + 614,
    "P-16: Towards The Singularity": BASE_ID + 615,
    "P-17: One Last Huzzah": BASE_ID + 616,
    "P-18: Farewell, Uncanny Cat Golf": BASE_ID + 617,
    "E-0: Deep Breaths...": BASE_ID + 700,
    "E-1: Feline Beeline": BASE_ID + 701,
    "E-2: T-T-Tilted": BASE_ID + 702,
    "E-3: Lying Face": BASE_ID + 703,
    "E-4: Tricky Thicket": BASE_ID + 704,
    "E-5: Three Ring Circus": BASE_ID + 705,
    "E-6: But Passion Is Mortal...": BASE_ID + 706,
    "E-7: The Key to Failure": BASE_ID + 707,
    "E-8: HE'S IN THE WALLS!!!": BASE_ID + 708,
    "E-9: Infinity Plaza": BASE_ID + 709,

    # Worlds
    "World 1 (Golf Central) Unlock": BASE_ID + 1000,
    "World 2 (Glowstick City) Unlock": BASE_ID + 1001,
    "World 3 (Chuckle Park) Unlock": BASE_ID + 1002,
    "World 4 (Final Frontier) Unlock": BASE_ID + 1003,
    "World 5 (Elysian Fields) Unlock": BASE_ID + 1004,
    "World P (Cosmic Championship) Unlock": BASE_ID + 1005,
    "World E (Endless Levels) Unlock": BASE_ID + 1006,

    # Gimmicks
    "Breakable Tiles": BASE_ID + 2000,
    "Keys": BASE_ID + 2001,
    "Stop Markers": BASE_ID + 2002,
    "Go Markers": BASE_ID + 2003,
    "Jump Pads": BASE_ID + 2004,
    "Switch Tiles": BASE_ID + 2005,
    "Dog": BASE_ID + 2006,
    "Portals": BASE_ID + 2007,
    "Nuke": BASE_ID + 2008,
    # World 5 Exclusive
    "Golf Balls": BASE_ID + 2009,
    "Landmines": BASE_ID + 2010,
    # World P Exclusive
    "Metronome": BASE_ID + 2011,

    # Modifiers
    "Burst Modifier Trap": BASE_ID + 3000,
    "Telekinesis Modifier Trap": BASE_ID + 3001,
    "Little Buddy Modifier Trap": BASE_ID + 3002,
    "Parry Modifier Trap": BASE_ID + 3003, # Not a trap really, but just count it as one, make it trap + useful
    "Jumpy Modifier Trap": BASE_ID + 3004,
    "Dizzy Modifier Trap": BASE_ID + 3005,
    "Missile Strike Modifier Trap": BASE_ID + 3006,
    "Sticky Modifier Trap": BASE_ID + 3007,

    # Filler
    "Golf!": BASE_ID + 4000
}

# All level and world unlocks are progression deprioritzed skip balancing, and thus are excluded from this list for simplicity.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Breakable Tiles": ItemClassification.progression,
    "Keys": ItemClassification.progression,
    "Stop Markers": ItemClassification.progression,
    "Go Markers": ItemClassification.progression,
    "Jump Pads": ItemClassification.progression,
    "Switch Tiles": ItemClassification.progression,
    "Dog": ItemClassification.progression,
    "Portals": ItemClassification.progression,
    "Nuke": ItemClassification.progression,
    "Golf Balls": ItemClassification.progression,
    "Landmines": ItemClassification.progression,
    "Metronome": ItemClassification.progression,

    "Burst Modifier Trap": ItemClassification.trap,
    "Telekinesis Modifier Trap": ItemClassification.trap,
    "Little Buddy Modifier Trap": ItemClassification.trap,
    "Parry Modifier Trap": ItemClassification.trap,
    "Jumpy Modifier Trap": ItemClassification.trap,
    "Dizzy Modifier Trap": ItemClassification.trap,
    "Missile Strike Modifier Trap": ItemClassification.trap,
    "Sticky Modifier Trap": ItemClassification.trap,

    "Golf!": ItemClassification.filler
}

LEVEL_ITEM_NAMES: set[str] = {
    name for name, item_id in ITEM_NAME_TO_ID.items() if item_id < BASE_ID + 1000
}

ITEM_GROUPS: dict[str, set[str]] = {
    "Levels": LEVEL_ITEM_NAMES,
    "Worlds": { 
        "World 1 (Golf Central) Unlock",
        "World 2 (Glowstick City) Unlock",
        "World 3 (Chuckle Park) Unlock",
        "World 4 (Final Frontier) Unlock",
        "World 5 (Elysian Fields) Unlock",
        "World P (Cosmic Championship) Unlock",
        "World E (Endless Levels) Unlock",
    },
    "Gimmicks": { "Breakable Tiles", "Keys", "Stop Markers", "Go Markers", "Jump Pads", "Switch Tiles", "Dog", "Portals", "Nuke", "Golf Balls", "Landmines", "Metronome"},
    "Traps": { "Burst Modifier Trap", "Telekinesis Modifier Trap", "Little Buddy Modifier Trap", "Parry Modifier Trap", "Jumpy Modifier Trap", "Dizzy Modifier Trap", "Missile Strike Modifier Trap", "Sticky Modifier Trap"}
}

FILLER_ITEM_NAME = "Golf!"
TRAP_CHANCE = 25 # Percentage of traps replacing filler

WORLD_UNLOCK_BY_PREFIX: dict[str, str] = {
    "1": "World 1 (Golf Central) Unlock",
    "2": "World 2 (Glowstick City) Unlock",
    "3": "World 3 (Chuckle Park) Unlock",
    "4": "World 4 (Final Frontier) Unlock",
    "5": "World 5 (Elysian Fields) Unlock",
    "P": "World P (Cosmic Championship) Unlock",
    "E": "World E (Endless Levels) Unlock",
}

# Gimmicks that are dependent on worlds being enabled
GIMMICK_WORLD_PREFIX: dict[str, str] = {
    "Golf Balls": "5",
    "Landmines": "5",
    "Metronome": "P",
}


def world_prefix(level_name: str) -> str:
    """5-18: The End Is Neigh. -> "5". P-17: One Last Huzzah -> "P"."""
    return level_name.split("-", 1)[0]


def get_included_world_prefixes(world: UncannyCatWorld) -> set[str]:
    """The worlds whose levels exist as checks under the player's options."""
    prefixes = {"0", "1", "2", "3", "4"}
    if world.options.world_5_levels:
        prefixes.add("5")
    if world.options.world_p_levels:
        prefixes.add("P")
    if world.options.world_e_levels:
        prefixes.add("E")
    return prefixes


def unlock_item_name(world: UncannyCatWorld, level_name: str) -> str | None:
    """The item that unlocks the given level, or None if the level requires nothing."""
    from .options import LevelUnlockStyle

    if world.options.level_unlock_style == LevelUnlockStyle.option_individual and level_name in LEVEL_ITEM_NAMES:
        return level_name
    return WORLD_UNLOCK_BY_PREFIX.get(world_prefix(level_name))


def get_unlock_item_names(world: UncannyCatWorld) -> list[str]:
    """Every level/world unlock item needed to reach the locations this world actually creates, without duplicates."""
    # Imported here rather than at module scope because locations.py imports this module.
    from .locations import LOCATION_DATA, get_excluded_locations, level_item_name

    excluded = get_excluded_locations(world)
    names: list[str] = []
    seen: set[str] = set()
    for location_name in LOCATION_DATA:
        if location_name in excluded:
            continue
        name = unlock_item_name(world, level_item_name(location_name))
        if name is not None and name not in seen:
            seen.add(name)
            names.append(name)
    return names


def get_gimmick_item_names(world: UncannyCatWorld) -> list[str]:
    """The gimmick items that are actually required by logic under the player's options."""
    if not world.options.gimmick_lock:
        return []
    included = get_included_world_prefixes(world)
    return [
        name for name in ITEM_GROUPS["Gimmicks"]
        if GIMMICK_WORLD_PREFIX.get(name, "0") in included
    ]


def get_item_classification(name: str) -> ItemClassification:
    if name in DEFAULT_ITEM_CLASSIFICATIONS:
        return DEFAULT_ITEM_CLASSIFICATIONS[name]
    if name in LEVEL_ITEM_NAMES or name in ITEM_GROUPS["Worlds"]:
        return ItemClassification.progression_deprioritized_skip_balancing
    raise KeyError(f"No classification defined for Uncanny Cat Golf item {name!r}")


class UncannyCatItem(Item):
    game = "Uncanny Cat Golf"


def get_random_filler_item_name(world: UncannyCatWorld) -> str:
    if world.random.randint(0, 99) < TRAP_CHANCE:
        return world.random.choice(sorted(ITEM_GROUPS["Traps"]))
    return FILLER_ITEM_NAME


def create_item_with_correct_classification(world: UncannyCatWorld, name: str) -> UncannyCatItem:
    return UncannyCatItem(name, get_item_classification(name), ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: UncannyCatWorld) -> None:
    itempool: list[Item] = [
        world.create_item(name)
        for name in get_unlock_item_names(world) + get_gimmick_item_names(world)
    ]

    # Fill remaining location slots with filler/traps
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_filler = number_of_unfilled_locations - len(itempool)
    if needed_filler < 0:
        raise OptionError(
            f"Uncanny Cat Golf ({world.player_name}) created {len(itempool)} items for only "
            f"{number_of_unfilled_locations} locations. Enable more worlds or peak checks."
        )
    itempool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += itempool
