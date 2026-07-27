from collections.abc import Mapping
from typing import Any

from BaseClasses import ItemClassification
from worlds.AutoWorld import World
from Options import OptionError

from . import items, locations, regions, rules, web_world
from . import options as UncannyCat_options

class UncannyCatWorld(World):
    """
    Uncanny Cat Golf is a game about shooting a cat into various golf holes, with hijinx aplenty
    """
    
    game = "Uncanny Cat Golf"
    web = web_world.UncannyCatWebWorld()

    options_dataclass = UncannyCat_options.UncannyCatOptions
    options: UncannyCat_options.UncannyCatOptions 

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    item_name_groups = items.ITEM_GROUPS

    origin_region_name = "Overworld"

    ut_can_gen_without_yaml = True
    glitches_item_name: str = "out_of_logic"
        
    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.UncannyCatItem:
        if name == self.glitches_item_name:
            return items.UncannyCatItem(name, ItemClassification.progression, None, self.player)
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "goal":        sorted(self.options.goal.value)
        }

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data