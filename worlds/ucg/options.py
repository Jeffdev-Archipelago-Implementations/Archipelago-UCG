from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, DefaultOnToggle, OptionSet, DeathLink, Range, Choice

class GoalLevel(Choice):
    """
    Set what goal level you want to do have as your final level.
    This level is removed from the multiworld, if selected, and will not be an item sent.
    Levels from World 5 or World P will force enable those worlds if selected, and the worlds aren't enabled
    """
    display_name = "Goal Level"
    default = 1

    option_3_18 = 0
    option_4_17 = 1
    option_5_18 = 2
    option_P_17 = 3

class GimmickLocking(DefaultOnToggle):
    """
    Lock level gimmicks such as wormholes, dogs, toggle switches, etc. behind items in the multiworld.
    """
    display_name = "Gimmick Locking"

class Minigames(DefaultOnToggle):
    """
    Enable minigames as checks, such as Bort Bash, UNCANNY_DASH, Meowls, etc. 
    """
    display_name = "Minigames"

class World5Levels(Toggle):
    """
    Include World 5 (Elysian Fields) levels as checks.
    """
    display_name = "World 5 Levels"

class WorldPLevels(Toggle):
    """
    Include World P (Cosmic Championship) levels as checks. These are a big step up in difficulty, so be warned 
    """
    display_name = "World P Levels"

class WorldELevels(Toggle):
    """
    Include World E levels as checks, which are exclusive levels from the Endless Shuffle.
    """
    display_name = "World E Levels"

class PeakChecks(Toggle):
    """
    Add a check for gaining a "PEAK" rank in a level. These can be extremely difficult.
    """
    display_name = "Peak Checks"

class ChillMode(Toggle):
    """
    Enable the "Chill Mode" modifier that removes the Uncanny Cat entirely. This makes the game significantly easier.
    """
    display_name = "Chill Mode"

class PanicMode(Toggle):
    """
    Enable the "Panic Mode" modifier that speeds up the Uncanny Cat quite a bit. This makes the game significantly harder, and may
    result in unbeatable seeds depending on your skill levels. BE WARNED.

    DO NOT ENABLE THIS IF YOU AREN'T PREPARED FOR WHAT IT ENTAILS.

    Automatically disabled if "Chill Mode" is enabled.
    """
    display_name = "Panic Mode"

@dataclass
class UncannyCatOptions(PerGameCommonOptions):
    gimmick_lock: GimmickLocking
    minigames: Minigames
    world_5_levels: World5Levels
    world_p_levels: WorldPLevels
    world_e_levels: WorldELevels
    peak_checks: PeakChecks
    chill_mode: ChillMode
    panic_mode: PanicMode