from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import UncannyCatWorld

BASE_ID = 100

# name -> (id, list of gimmick items logically required to reach the check)
LOCATION_DATA: dict[str, tuple[int, list[str]]] = {
    "0-1: Welcome to UNCANNY CAT GOLF! Complete": (BASE_ID + 0, []),
    "0-1: Welcome to UNCANNY CAT GOLF! Peak": (BASE_ID + 1000, []),
    "0-2: Hello Walls Complete": (BASE_ID + 1, []),
    "0-2: Hello Walls Peak": (BASE_ID + 1001, []),
    "0-3: Meet the Slopes Complete": (BASE_ID + 2, []),
    "0-3: Meet the Slopes Peak": (BASE_ID + 1002, []),
    "0-4: Pretty Pennies Complete": (BASE_ID + 3, []),
    "0-4: Pretty Pennies Peak": (BASE_ID + 1003, []),
    "0-5: Onward and Golfward! Complete": (BASE_ID + 4, []),
    "0-5: Onward and Golfward! Peak": (BASE_ID + 1004, []),

    "1-1: Welcome to GOLF CENTRAL! Complete": (BASE_ID + 100, []),
    "1-1: Welcome to GOLF CENTRAL! Peak": (BASE_ID + 1100, []),
    "1-2: Getting Around Complete": (BASE_ID + 101, []),
    "1-2: Getting Around Peak": (BASE_ID + 1101, []),
    "1-3: A New Angle Complete": (BASE_ID + 102, []),
    "1-3: A New Angle Peak": (BASE_ID + 1102, []),
    "1-4: Breakthrough! Complete": (BASE_ID + 103, ["Breakable Tiles"]),
    "1-4: Breakthrough! Peak": (BASE_ID + 1103, ["Breakable Tiles"]),
    "1-5: Right up my Alley Complete": (BASE_ID + 104, ["Breakable Tiles"]),
    "1-5: Right up my Alley Peak": (BASE_ID + 1104, ["Breakable Tiles"]),
    "1-6: Roundabout Complete": (BASE_ID + 105, ["Breakable Tiles"]),
    "1-6: Roundabout Peak": (BASE_ID + 1105, ["Breakable Tiles"]),
    "1-7: Bunker Funk Complete": (BASE_ID + 106, ["Breakable Tiles"]),
    "1-7: Bunker Funk Peak": (BASE_ID + 1106, ["Breakable Tiles"]),
    "1-8: Bony Cronies Complete": (BASE_ID + 107, []),
    "1-8: Bony Cronies Peak": (BASE_ID + 1107, []),
    "1-9: Kitty Litter Complete": (BASE_ID + 108, []),
    "1-9: Kitty Litter Peak": (BASE_ID + 1108, []),
    "1-10: Double Trouble Complete": (BASE_ID + 109, []),
    "1-10: Double Trouble Peak": (BASE_ID + 1109, []),
    "1-11: Triple Trouble Complete": (BASE_ID + 110, []),
    "1-11: Triple Trouble Peak": (BASE_ID + 1110, []),
    "1-12: An Absurd Amount of Trouble Complete": (BASE_ID + 111, []),
    "1-12: An Absurd Amount of Trouble Peak": (BASE_ID + 1111, []),
    "1-13: The Key to Success Complete": (BASE_ID + 112, ["Keys"]),
    "1-13: The Key to Success Peak": (BASE_ID + 1112, ["Keys"]),
    "1-14: Ooooh, Pretty Colors Complete": (BASE_ID + 113, ["Keys"]),
    "1-14: Ooooh, Pretty Colors Peak": (BASE_ID + 1113, ["Keys"]),
    "1-15: Almost a Cakewalk Complete": (BASE_ID + 114, ["Keys"]),
    "1-15: Almost a Cakewalk Peak": (BASE_ID + 1114, ["Keys"]),
    "1-16: Silly Yard Complete": (BASE_ID + 115, ["Keys"]),
    "1-16: Silly Yard Peak": (BASE_ID + 1115, ["Keys"]),
    "1-17: Scattered Around Complete": (BASE_ID + 116, ["Keys"]),
    "1-17: Scattered Around Peak": (BASE_ID + 1116, ["Keys"]),
    "1-18: Rest Stop Complete": (BASE_ID + 117, []),
    "1-18: Rest Stop Peak": (BASE_ID + 1117, []),

    "2-1: Welcome to GLOWSTICK CITY! Complete": (BASE_ID + 200, []),
    "2-1: Welcome to GLOWSTICK CITY! Peak": (BASE_ID + 1200, []),
    "2-2: Stop Right There! Complete": (BASE_ID + 201, []),
    "2-2: Stop Right There! Peak": (BASE_ID + 1201, []),
    "2-3: Parking Lot Complete": (BASE_ID + 202, []),
    "2-3: Parking Lot Peak": (BASE_ID + 1202, []),
    "2-4: Just Zoomin' By Complete": (BASE_ID + 203, []),
    "2-4: Just Zoomin' By Peak": (BASE_ID + 1203, ["Go Markers"]),
    "2-5: Stop 'n' Start Complete": (BASE_ID + 204, ["Keys"]),
    "2-5: Stop 'n' Start Peak": (BASE_ID + 1204, ["Keys", "Go Markers", "Stop Markers"]),
    "2-6: Backstreet Skullz Complete": (BASE_ID + 205, ["Breakable Tiles"]),
    "2-6: Backstreet Skullz Peak": (BASE_ID + 1205, ["Breakable Tiles", "Go Markers", "Stop Markers"]),
    "2-7: Look Both Ways Complete": (BASE_ID + 206, []),
    "2-7: Look Both Ways Peak": (BASE_ID + 1206, []),
    "2-8: Dimlit District Complete": (BASE_ID + 207, []),
    "2-8: Dimlit District Peak": (BASE_ID + 1207, ["Stop Markers", "Go Markers"]),
    "2-9: This is A Mugging Complete": (BASE_ID + 208, []),
    "2-9: This is A Mugging Peak": (BASE_ID + 1208, ["Stop Markers", "Go Markers"]),
    "2-10: jump pad introductary level Complete": (BASE_ID + 209, ["Jump Pads"]),
    "2-10: jump pad introductary level Peak": (BASE_ID + 1209, ["Jump Pads"]),
    "2-11: Heist To Meet You Complete": (BASE_ID + 210, ["Keys", "Breakable Tiles", "Jump Pads", "Go Markers"]),
    "2-11: Heist To Meet You Peak": (BASE_ID + 1210, ["Keys", "Breakable Tiles", "Jump Pads", "Go Markers"]),
    "2-12: Highway Getaway! Complete": (BASE_ID + 211, []),
    "2-12: Highway Getaway! Peak": (BASE_ID + 1211, []),
    "2-13: Brawl In The Big City Complete": (BASE_ID + 212, ["Keys", "Jump Pads"]),
    "2-13: Brawl In The Big City Peak": (BASE_ID + 1212, ["Keys", "Jump Pads", "Go Markers", "Stop Markers"]),
    "2-14: Waiter! There's Slop In My Soup! Complete": (BASE_ID + 213, ["Keys"]),
    "2-14: Waiter! There's Slop In My Soup! Peak": (
        BASE_ID + 1213,
        ["Keys", "Breakable Tiles", "Jump Pads", "Go Markers", "Stop Markers"],
    ),
    "2-15: Back In The Back Alley Complete": (BASE_ID + 214, ["Keys", "Jump Pads"]),
    "2-15: Back In The Back Alley Peak": (BASE_ID + 1214, ["Keys", "Jump Pads", "Stop Markers", "Go Markers"]),
    "2-16: Trickshot! Complete": (BASE_ID + 215, ["Jump Pads"]),
    "2-16: Trickshot! Peak": (BASE_ID + 1215, ["Jump Pads", "Stop Markers", "Go Markers"]),
    "2-17: Baby Vegas Complete": (BASE_ID + 216, ["Keys", "Jump Pads"]),
    "2-17: Baby Vegas Peak": (BASE_ID + 1216, ["Keys", "Jump Pads", "Stop Markers"]),
    "2-18: Good Night, Glowstick City Complete": (BASE_ID + 217, ["Jump Pads"]),
    "2-18: Good Night, Glowstick City Peak": (BASE_ID + 1217, ["Jump Pads"]),

    "3-1: Welcome to CHUCKLE PARK! Complete": (BASE_ID + 300, []),
    "3-1: Welcome to CHUCKLE PARK! Peak": (BASE_ID + 1300, []),
    "3-1: Welcome to CHUCKLE PARK! Yellow Smiley": (BASE_ID + 2303, []),
    "3-2: Chuckle-Go-Round Complete": (BASE_ID + 301, ["Breakable Tiles"]),
    "3-2: Chuckle-Go-Round Peak": (BASE_ID + 1301, ["Breakable Tiles", "Stop Markers"]),
    "3-2: Chuckle-Go-Round Yellow Smiley": (BASE_ID + 2308, []),
    "3-3: Switch It Up! Complete": (BASE_ID + 302, ["Switch Tiles"]),
    "3-3: Switch It Up! Peak": (BASE_ID + 1302, ["Switch Tiles"]),
    "3-4: JumbleHouse Complete": (BASE_ID + 303, ["Switch Tiles"]),
    "3-4: JumbleHouse Peak": (BASE_ID + 1303, ["Switch Tiles"]),
    "3-5: Titular Chuckles Complete": (BASE_ID + 304, ["Keys"]),
    "3-5: Titular Chuckles Peak": (BASE_ID + 1304, ["Keys", "Breakable Tiles"]),
    "3-5: Titular Chuckles Yellow Smiley": (BASE_ID + 2323, []),
    "3-6: Cleanup On Aisle 2! Complete": (BASE_ID + 305, ["Breakable Tiles"]),
    "3-6: Cleanup On Aisle 2! Peak": (BASE_ID + 1305, ["Breakable Tiles"]),
    "3-7: Chuckles Inc. Complete": (BASE_ID + 306, ["Keys"]),
    "3-7: Chuckles Inc. Peak": (BASE_ID + 1306, ["Keys", "Jump Pads", "Stop Markers", "Go Markers"]),
    "3-7: Chuckles Inc. Yellow Smiley": (BASE_ID + 2333, ["Keys", "Stop Markers"]),
    "3-8: How Many Licks... Complete": (BASE_ID + 307, ["Breakable Tiles"]),
    "3-8: How Many Licks... Peak": (BASE_ID + 1307, ["Breakable Tiles"]),
    "3-9: House of Mirrors Complete": (BASE_ID + 308, ["Breakable Tiles"]),
    "3-9: House of Mirrors Peak": (BASE_ID + 1308, ["Breakable Tiles"]),
    "3-10: You Bring a Light? Complete": (BASE_ID + 309, []),
    "3-10: You Bring a Light? Peak": (BASE_ID + 1309, []),
    "3-11: Four Leaf Marathon Complete": (BASE_ID + 310, ["Keys", "Jump Pads"]),
    "3-11: Four Leaf Marathon Peak": (BASE_ID + 1310, ["Keys", "Jump Pads"]),
    "3-11: Four Leaf Marathon Red Smiley": (BASE_ID + 2350, []),
    "3-11: Four Leaf Marathon Green Smiley": (BASE_ID + 2351, []),
    "3-11: Four Leaf Marathon Blue Smiley": (BASE_ID + 2352, []),
    "3-11: Four Leaf Marathon Yellow Smiley": (BASE_ID + 2353, ["Keys", "Jump Pads"]),
    "3-12: Pursuit of Happiness Complete": (BASE_ID + 311, ["Switch Tiles"]),
    "3-12: Pursuit of Happiness Peak": (BASE_ID + 1311, ["Switch Tiles", "Stop Markers", "Go Markers"]),
    "3-12: Pursuit of Happiness Red Smiley": (BASE_ID + 2355, []),
    "3-12: Pursuit of Happiness Green Smiley": (BASE_ID + 2356, ["Switch Tiles"]),
    "3-12: Pursuit of Happiness Blue Smiley": (BASE_ID + 2357, ["Switch Tiles"]),
    "3-12: Pursuit of Happiness Yellow Smiley": (BASE_ID + 2358, ["Switch Tiles"]),
    "3-12: Pursuit of Happiness Orange Smiley": (BASE_ID + 2359, ["Switch Tiles", "Go Markers", "Stop Markers"]),
    "3-13: UNCANNY DOG GOLF Complete": (BASE_ID + 312, ["Dog", "Switch Tiles"]),
    "3-13: UNCANNY DOG GOLF Peak": (BASE_ID + 1312, ["Dog", "Switch Tiles"]),
    "3-14: Canny's Best Friend Complete": (BASE_ID + 313, ["Dog"]),
    "3-14: Canny's Best Friend Peak": (BASE_ID + 1313, ["Dog", "Switch Tiles"]),
    "3-15: UNCANNY DOG GOLF but with a cat instead of a dog Complete": (BASE_ID + 314, ["Dog", "Switch Tiles"]),
    "3-15: UNCANNY DOG GOLF but with a cat instead of a dog Peak": (BASE_ID + 1314, ["Dog", "Switch Tiles"]),
    "3-16: He Shoots! He scores! Complete": (BASE_ID + 315, ["Dog"]),
    "3-16: He Shoots! He scores! Peak": (BASE_ID + 1315, ["Dog"]),
    "3-16: He Shoots! He scores! Red Smiley": (BASE_ID + 2375, ["Dog"]),
    "3-17: Racetrack Chasetrack Complete": (BASE_ID + 316, ["Keys", "Dog", "Jump Pads"]),
    "3-17: Racetrack Chasetrack Peak": (
        BASE_ID + 1316,
        ["Keys", "Dog", "Jump Pads", "Go Markers", "Stop Markers"],
    ),
    "3-17: Racetrack Chasetrack Blue Smiley": (BASE_ID + 2382, ["Dog", "Jump Pads"]),
    "3-17: Racetrack Chasetrack Yellow Smiley": (BASE_ID + 2383, ["Dog", "Jump Pads"]),
    "3-18: The Chuckle Coaster Complete": (BASE_ID + 317, ["Jump Pads"]),
    "3-18: The Chuckle Coaster Peak": (BASE_ID + 1317, ["Jump Pads"]),

    "4-1: Welcome to THE FINAL FRONTIER. Complete": (BASE_ID + 400, []),
    "4-1: Welcome to THE FINAL FRONTIER. Peak": (BASE_ID + 1400, []),
    "4-2: No Time 4 Messing Around Complete": (BASE_ID + 401, ["Switch Tiles"]),
    "4-2: No Time 4 Messing Around Peak": (BASE_ID + 1401, ["Switch Tiles"]),
    "4-3: Now You're Thinking With Portal Complete": (BASE_ID + 402, ["Portals"]),
    "4-3: Now You're Thinking With Portal Peak": (BASE_ID + 1402, ["Portals"]),
    "4-4: Wholesome DIY Complete": (BASE_ID + 403, ["Portals"]),
    "4-4: Wholesome DIY Peak": (BASE_ID + 1403, ["Portals"]),
    "4-5: Cube Town Complete": (BASE_ID + 404, ["Switch Tiles"]),
    "4-5: Cube Town Peak": (BASE_ID + 1404, ["Switch Tiles"]),
    "4-6: Jumbling Labrynth Complete": (BASE_ID + 405, ["Portals", "Jump Pads"]),
    "4-6: Jumbling Labrynth Peak": (BASE_ID + 1405, ["Portals", "Jump Pads"]),
    "4-7: Production Room Complete": (BASE_ID + 406, ["Dog"]),
    "4-7: Production Room Peak": (BASE_ID + 1406, ["Dog", "Jump Pads", "Go Markers"]),
    "4-8: On Heavens No The Chuckles Are Plentiful Complete": (
        BASE_ID + 407,
        ["Nuke", "Stop Markers", "Switch Tiles"],
    ),
    "4-8: On Heavens No The Chuckles Are Plentiful Peak": (
        BASE_ID + 1407,
        ["Nuke", "Stop Markers", "Switch Tiles"],
    ),
    "4-9: Uncanny Valley Complete": (BASE_ID + 408, ["Jump Pads", "Stop Markers", "Keys", "Nuke"]),
    "4-9: Uncanny Valley Peak": (BASE_ID + 1408, ["Jump Pads", "Stop Markers"]),
    "4-10: Dog Patrol Complete": (BASE_ID + 409, ["Dog"]),
    "4-10: Dog Patrol Peak": (BASE_ID + 1409, ["Dog"]),
    "4-11: The Really Cool Mining Level Complete": (BASE_ID + 410, ["Dog", "Breakable Tiles"]),
    "4-11: The Really Cool Mining Level Peak": (BASE_ID + 1410, ["Dog", "Breakable Tiles"]),
    "4-12: Weather Alert Complete": (BASE_ID + 411, ["Keys", "Jump Pads"]),
    "4-12: Weather Alert Peak": (BASE_ID + 1411, ["Keys", "Jump Pads"]),
    "4-13: The Downfall Complete": (BASE_ID + 412, ["Breakable Tiles"]),
    "4-13: The Downfall Peak": (BASE_ID + 1412, ["Breakable Tiles"]),
    "4-14: I Saw This In A Movie Once Complete": (BASE_ID + 413, ["Keys"]),
    "4-14: I Saw This In A Movie Once Peak": (BASE_ID + 1413, ["Keys"]),
    "4-15: Abandoned Workspace Complete": (BASE_ID + 414, ["Keys"]),
    "4-15: Abandoned Workspace Peak": (BASE_ID + 1414, ["Keys"]),
    "4-16: Crimson Outpost Complete": (BASE_ID + 415, ["Breakable Tiles", "Nuke"]),
    "4-16: Crimson Outpost Peak": (BASE_ID + 1415, ["Breakable Tiles", "Nuke"]),
    "4-17: CATaclysmic CATastrophe Complete": (BASE_ID + 416, ["Switch Tiles", "Portals"]),
    "4-17: CATaclysmic CATastrophe Peak": (BASE_ID + 1416, ["Switch Tiles", "Portals", "Stop Markers"]),
    "4-18: The Wall Complete": (BASE_ID + 417, []),
    "4-18: The Wall Peak": (BASE_ID + 1417, []),

    "5-1: Elysian Fields. Complete": (BASE_ID + 500, []),
    "5-1: Elysian Fields. Peak": (BASE_ID + 1500, []),
    "5-2: ... Complete": (BASE_ID + 501, []),
    "5-2: ... Peak": (BASE_ID + 1501, []),
    "5-3: ..? Complete": (BASE_ID + 502, []),
    "5-3: ..? Peak": (BASE_ID + 1502, []),
    "5-4: The Horse Is Here. Complete": (BASE_ID + 503, ["Golf Balls"]),
    "5-4: The Horse Is Here. Peak": (BASE_ID + 1503, ["Golf Balls"]),
    "5-5: Unstable Complete": (BASE_ID + 504, ["Golf Balls"]),
    "5-5: Unstable Peak": (BASE_ID + 1504, ["Golf Balls"]),
    "5-6: Close Encounters Of The Equine Kind Complete": (BASE_ID + 505, ["Breakable Tiles", "Golf Balls"]),
    "5-6: Close Encounters Of The Equine Kind Peak": (BASE_ID + 1505, ["Breakable Tiles", "Golf Balls"]),
    "5-7: Late to the Party Complete": (BASE_ID + 506, ["Golf Balls"]),
    "5-7: Late to the Party Peak": (BASE_ID + 1506, ["Golf Balls"]),
    "5-8: Megaton Of Skeleton Complete": (BASE_ID + 507, ["Golf Balls"]),
    "5-8: Megaton Of Skeleton Peak": (BASE_ID + 1507, ["Golf Balls"]),
    "5-9: Neigh Impossible Complete": (BASE_ID + 508, ["Breakable Tiles", "Golf Balls"]),
    "5-9: Neigh Impossible Peak": (BASE_ID + 1508, ["Breakable Tiles", "Golf Balls"]),
    "5-10: Move It Or Lose It Complete": (BASE_ID + 509, ["Breakable Tiles", "Golf Balls"]),
    "5-10: Move It Or Lose It Peak": (
        BASE_ID + 1509,
        ["Breakable Tiles", "Golf Balls", "Go Markers", "Stop Markers"],
    ),
    "5-11: Why Is There A Highway Here?!?! Complete": (BASE_ID + 510, ["Golf Balls", "Jump Pads"]),
    "5-11: Why Is There A Highway Here?!?! Peak": (BASE_ID + 1510, ["Golf Balls", "Jump Pads"]),
    "5-12: Two Face Temple Complete": (BASE_ID + 511, ["Golf Balls", "Switch Tiles"]),
    "5-12: Two Face Temple Peak": (BASE_ID + 1511, ["Golf Balls", "Switch Tiles"]),
    "5-12: Two Face Temple Blue Smiley": (BASE_ID + 2557, []),
    "5-13: What Is This, A Crossover Episode? Complete": (BASE_ID + 512, ["Golf Balls"]),
    "5-13: What Is This, A Crossover Episode? Peak": (BASE_ID + 1512, ["Golf Balls"]),
    "5-14: Containment Breach Complete": (BASE_ID + 513, ["Golf Balls", "Switch Tiles", "Nuke"]),
    "5-14: Containment Breach Peak": (BASE_ID + 1513, ["Golf Balls", "Switch Tiles", "Nuke"]),
    "5-15: Hoppin' Mad Complete": (BASE_ID + 514, ["Golf Balls", "Portals|Jump Pads"]),
    "5-15: Hoppin' Mad Peak": (BASE_ID + 1514, ["Golf Balls", "Portals", "Jump Pads"]),
    "5-16: The Wizard of Gimmica Strikes!! Complete": (BASE_ID + 515, ["Golf Balls"]),
    "5-16: The Wizard of Gimmica Strikes!! Peak": (BASE_ID + 1515, ["Golf Balls"]),
    "5-17: Perilous Plinko Complete": (BASE_ID + 516, ["Golf Balls"]),
    "5-17: Perilous Plinko Peak": (BASE_ID + 1516, ["Golf Balls"]),
    "5-18: The End Is Neigh. Complete": (BASE_ID + 517, ["Landmines"]),
    "5-18: The End Is Neigh. Peak": (BASE_ID + 1517, ["Landmines"]),

    "P-1: Welcome to...? Complete": (BASE_ID + 600, []),
    "P-1: Welcome to...? Peak": (BASE_ID + 1600, []),
    "P-2: Welcome to COSMIC CHAMPIONSHIP!! Complete": (BASE_ID + 601, ["Keys", "Jump Pads"]),
    "P-2: Welcome to COSMIC CHAMPIONSHIP!! Peak": (BASE_ID + 1601, ["Keys", "Jump Pads"]),
    "P-3: Avoid the Void Complete": (BASE_ID + 602, ["Switch Tiles"]),
    "P-3: Avoid the Void Peak": (BASE_ID + 1602, ["Switch Tiles", "Stop Markers"]),
    "P-4: I Couldn't Beat This One :( Complete": (BASE_ID + 603, ["Switch Tiles"]),
    "P-4: I Couldn't Beat This One :( Peak": (BASE_ID + 1603, ["Switch Tiles"]),
    "P-5: Starstorm! Complete": (BASE_ID + 604, ["Breakable Tiles"]),
    "P-5: Starstorm! Peak": (BASE_ID + 1604, ["Breakable Tiles", "Stop Markers"]),
    "P-6: Oh My Goodness, This Beat Is So Hard Complete": (BASE_ID + 605, ["Metronome"]),
    "P-6: Oh My Goodness, This Beat Is So Hard Peak": (BASE_ID + 1605, ["Metronome"]),
    "P-7: Ourple Complete": (BASE_ID + 606, ["Metronome", "Switch Tiles"]),
    "P-7: Ourple Peak": (BASE_ID + 1606, ["Metronome", "Switch Tiles"]),
    "P-8: Get In The Groove! Complete": (BASE_ID + 607, ["Metronome", "Portals"]),
    "P-8: Get In The Groove! Peak": (BASE_ID + 1607, ["Metronome", "Portals"]),
    "P-9: Neon Hopscotch Complete": (BASE_ID + 608, ["Metronome"]),
    "P-9: Neon Hopscotch Peak": (BASE_ID + 1608, ["Metronome"]),
    "P-10: Claustrophobia Complete": (BASE_ID + 609, ["Metronome", "Keys"]),
    "P-10: Claustrophobia Peak": (BASE_ID + 1609, ["Metronome", "Keys"]),
    "P-11: Beat The Beat The Beat The Beat The Beat Complete": (BASE_ID + 610, ["Metronome", "Portals"]),
    "P-11: Beat The Beat The Beat The Beat The Beat Peak": (BASE_ID + 1610, ["Metronome", "Portals"]),
    "P-11: Beat The Beat The Beat The Beat The Beat Yellow Smiley": (BASE_ID + 2653, ["Metronome", "Portals"]),
    "P-12: JumbleRAVE!! Complete": (BASE_ID + 611, ["Switch Tiles", "Jump Pads"]),
    "P-12: JumbleRAVE!! Peak": (BASE_ID + 1611, ["Switch Tiles", "Jump Pads"]),
    "P-13: where are you going come back Complete": (BASE_ID + 612, []),
    "P-13: where are you going come back Peak": (BASE_ID + 1612, []),
    "P-14: Sea of Lies Complete": (BASE_ID + 613, []),
    "P-14: Sea of Lies Peak": (BASE_ID + 1613, []),
    "P-15: Santa's Revenge (What!!!) Complete": (BASE_ID + 614, ["Portals", "Breakable Tiles", "Keys"]),
    "P-15: Santa's Revenge (What!!!) Peak": (BASE_ID + 1614, ["Portals", "Breakable Tiles", "Keys"]),
    "P-15: Santa's Revenge (What!!!) Yellow Smiley": (BASE_ID + 2673, ["Portals", "Breakable Tiles", "Keys"]),
    "P-16: Towards The Singularity Complete": (BASE_ID + 615, ["Keys", "Jump Pads", "Go Markers"]),
    "P-16: Towards The Singularity Peak": (BASE_ID + 1615, ["Keys", "Jump Pads", "Go Markers"]),
    "P-17: One Last Huzzah Complete": (
        BASE_ID + 616,
        ["Keys", "Breakable Tiles", "Switch Tiles", "Stop Markers", "Nuke", "Dog", "Metronome"],
    ),
    "P-17: One Last Huzzah Peak": (
        BASE_ID + 1616,
        ["Keys", "Breakable Tiles", "Switch Tiles", "Stop Markers", "Nuke", "Dog", "Metronome", "Go Markers"],
    ),
    "P-17: One Last Huzzah Yellow Smiley": (
        BASE_ID + 2683,
        ["Keys", "Breakable Tiles", "Switch Tiles", "Stop Markers"],
    ),
    "P-18: Farewell, Uncanny Cat Golf Complete": (BASE_ID + 617, []),
    "P-18: Farewell, Uncanny Cat Golf Peak": (BASE_ID + 1617, []),

    "E-0: Deep Breaths... Complete": (BASE_ID + 700, []),
    "E-0: Deep Breaths... Peak": (BASE_ID + 1700, []),
    "E-1: Feline Beeline Complete": (BASE_ID + 701, ["Keys"]),
    "E-1: Feline Beeline Peak": (BASE_ID + 1701, ["Keys"]),
    "E-2: T-T-Tilted Complete": (BASE_ID + 702, []),
    "E-2: T-T-Tilted Peak": (BASE_ID + 1702, []),
    "E-3: Lying Face Complete": (BASE_ID + 703, ["Switch Tiles", "Jump Pads"]),
    "E-3: Lying Face Peak": (BASE_ID + 1703, ["Switch Tiles", "Jump Pads"]),
    "E-4: Tricky Thicket Complete": (BASE_ID + 704, ["Portals", "Jump Pads", "Breakable Tiles"]),
    "E-4: Tricky Thicket Peak": (BASE_ID + 1704, ["Portals", "Jump Pads", "Breakable Tiles", "Go Markers"]),
    "E-5: Three Ring Circus Complete": (BASE_ID + 705, []),
    "E-5: Three Ring Circus Peak": (BASE_ID + 1705, []),
    "E-6: But Passion Is Mortal... Complete": (BASE_ID + 706, ["Switch Tiles"]),
    "E-6: But Passion Is Mortal... Peak": (BASE_ID + 1706, ["Switch Tiles", "Stop Markers", "Go Markers"]),
    "E-7: The Key to Failure Complete": (BASE_ID + 707, ["Keys", "Jump Pads"]),
    "E-7: The Key to Failure Peak": (BASE_ID + 1707, ["Keys", "Jump Pads"]),
    "E-8: HE'S IN THE WALLS!!! Complete": (BASE_ID + 708, ["Keys", "Jump Pads"]),
    "E-8: HE'S IN THE WALLS!!! Peak": (BASE_ID + 1708, ["Keys", "Jump Pads"]),
    "E-9: Infinity Plaza Complete": (BASE_ID + 709, ["Keys", "Breakable Tiles"]),
    "E-9: Infinity Plaza Peak": (BASE_ID + 1709, ["Keys", "Breakable Tiles"]),
}

# The world class needs a plain name -> id mapping, without the logic requirements attached.
LOCATION_NAME_TO_ID: dict[str, int] = {name: data[0] for name, data in LOCATION_DATA.items()}

LEVEL_LOCATION_SUFFIXES = (
    " Complete", " Peak",
    " Red Smiley", " Green Smiley", " Blue Smiley", " Yellow Smiley", " Orange Smiley",
)


class UncannyCatLocation(Location):
    game = "Uncanny Cat Golf"


def level_item_name(location_name: str) -> str:
    """"1-4: Breakthrough! Peak" -> "1-4: Breakthrough!" (the level unlock item)."""
    for suffix in LEVEL_LOCATION_SUFFIXES:
        if location_name.endswith(suffix):
            return location_name[: -len(suffix)]
    return location_name


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def get_excluded_locations(world: UncannyCatWorld) -> set[str]:
    """Locations that don't exist under the player's options, and so get neither a check nor an unlock item."""
    included_worlds = items.get_included_world_prefixes(world)
    # The goal level is not included
    goal_level = items.GOAL_LEVEL[world.options.goal_level.value]

    excluded: set[str] = set()
    for location_name in LOCATION_NAME_TO_ID:
        level = level_item_name(location_name)
        if items.world_prefix(level) not in included_worlds:
            excluded.add(location_name)
        elif level == goal_level:
            excluded.add(location_name)
        elif not world.options.peak_checks and location_name.endswith(" Peak"):
            excluded.add(location_name)
    return excluded


def create_all_locations(world: UncannyCatWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: UncannyCatWorld) -> None:
    excluded = get_excluded_locations(world)
    for loc_name, loc_id in LOCATION_NAME_TO_ID.items():
        if loc_name in excluded:
            continue
        if loc_name.startswith("0"):
            region_name = "World 0 (Tutorial)"
        elif loc_name.startswith("1"):
            region_name = "World 1 (Golf Central)"
        elif loc_name.startswith("2"):
            region_name = "World 2 (Glowstick City)"
        elif loc_name.startswith("3"):
            region_name = "World 3 (Chuckle Park)"
        elif loc_name.startswith("4"):
            region_name = "World 4 (Final Frontier)"
        elif loc_name.startswith("5"):
            region_name = "World 5 (Elysian Fields)"
        elif loc_name.startswith("P"):
            region_name = "World P (Cosmic Championship)"
        elif loc_name.startswith("E"):
            region_name = "World E (Endless Levels)"
        else:
            region_name = "Summer Villa"
        region = world.get_region(region_name)
        region.add_locations({loc_name: loc_id}, UncannyCatLocation)


def create_events(world: UncannyCatWorld) -> None:
    # Victory lives in Menu because it is always physically reachable; its access rule is what actually gates it.
    menu = world.get_region("Menu")
    menu.add_event(
        "Victory", "Victory", location_type=UncannyCatLocation, item_type=items.UncannyCatItem
    )
