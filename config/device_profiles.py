# config/device_profiles.py
from typing import Dict, Any

def create_device_profile() -> Dict[str, Any]:
    return {
        "disable_built_in_keyboard_if_exists": True,
        "identifiers": {
            "is_keyboard": True,
            "is_pointing_device": True,
            "product_id": 544,
            "vendor_id": 13364
        },
        "ignore": False,
        "manipulate_caps_lock_led": False
    }

# generate.py
import json
from config.models import From, To, Manipulator, KarabinerRule
from config.settings import SUBLAYERS, ARC_BROWSER_BINDINGS
from config.sublayers import create_hyper_sublayers
from config.apps.arc import create_arc_browser_rule
from config.device_profiles import create_device_profile

def main():
    # Create basic rules
    rules = [
        KarabinerRule(
            description="Hyper Key (⌃⌥⇧⌘)",
            manipulators=[
                Manipulator(
                    type="basic",
                    from_=From(key_code="caps_lock", modifiers={"optional": ["any"]}),
                    to=[To(set_variable={"name": "hyper", "value": 1})],
                    to_after_key_up=[To(set_variable={"name": "hyper", "value": 0})],
                    to_if_alone=[To(key_code="escape")],
                    description="Caps Lock -> Hyper Key"
                )
            ]
        ),
        *create_hyper_sublayers(SUBLAYERS),
        create_arc_browser_rule(ARC_BROWSER_BINDINGS),
    ]

    # Create final configuration
    config = {
        "global": {
            "show_in_menu_bar": False
        },
        "profiles": [
            {
                "name": "Default",
                "complex_modifications": {
                    "rules": [rule.to_dict() for rule in rules]
                },
                "devices": [create_device_profile()],
                "virtual_hid_keyboard": {
                    "keyboard_type_v2": "ansi"
                }
            }
        ]
    }

    # Write configuration to file
    with open("karabiner.json", "w") as f:
        json.dump(config, f, indent=2)

if __name__ == "__main__":
    main()
    print("Karabiner configuration has been generated successfully!")
    print("Please copy karabiner.json to: ~/.config/karabiner/")