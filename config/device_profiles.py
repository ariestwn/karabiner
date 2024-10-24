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