from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification


if TYPE_CHECKING:
    from .world import UncannyCatWorld

BASE_ID = 100

# Every item must have a unique integer ID associated with it.
ITEM_NAME_TO_ID = {
    # Levels
    "0-1: Welcome to UNCANNY CAT GOLF!": BASE_ID + 0,
    "0-2: Hello Walls": BASE_ID + 1,
    "0-3: Meet the Slopes": BASE_ID + 2,
    "0-4: Pretty Pennies": BASE_ID + 3,
    "0-5: Onward and Golfward!": BASE_ID + 4,
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
    "Sticky Modifier Trap": BASE_ID + 3007
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
    "Sticky Modifier Trap": ItemClassification.trap
}

ITEM_GROUPS: dict[str, set[str]] = {
    "Gimmicks": { "Breakable Tiles", "Keys", "Stop Markers", "Go Markers", "Jump Pads", "Switch Tiles", "Dog", "Portals", "Nuke", "Golf Balls", "Landmines", "Metronome"},
    "Traps": { "Burst Modifier Trap", "Telekinesis Modifier Trap", "Little Buddy Modifier Trap", "Parry Modifier Trap", "Jumpy Modifier Trap", "Dizzy Modifier Trap", "Missile Strike Modifier Trap", "Sticky Modifier Trap"}
}


def is_progression_item(world: UncannyCatWorld, name: str) -> bool:
    prog_item = (DEFAULT_ITEM_CLASSIFICATIONS[name] in (
        ItemClassification.progression,
        ItemClassification.progression_deprioritized_skip_balancing,
    ) or "-" in name)
    return


class UncannyCatItem(Item):
    game = "Uncanny Cat Golf"


def get_random_filler_item_name(world: UncannyCatWorld) -> str:
    return "Golf!"


def create_item_with_correct_classification(world: UncannyCatWorld, name: str) -> UncannyCatItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return UncannyCatItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: UncannyCatWorld) -> None:
    # Create one of every progression item.
    itempool: list[Item] = [
        world.create_item(name)
        for name in DEFAULT_ITEM_CLASSIFICATIONS
        if is_progression_item(world, name)
    ]

    # Fill remaining location slots with filler.
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_filler = number_of_unfilled_locations - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += itempool
