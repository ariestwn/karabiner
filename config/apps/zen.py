# config/apps/zen.py
from typing import List, Tuple
from config import From, To, Manipulator, KarabinerRule

def create_zen_browser_manipulator(
    from_key: str,
    to_key: str,
    to_modifiers: List[str],
    description: str
) -> Manipulator:
    return Manipulator(
        type="basic",
        from_=From(key_code=from_key),
        to=[To(key_code=to_key, modifiers=to_modifiers)],
        conditions=[
            {"type": "variable_if", "name": "hyper", "value": 1},
            {
                "type": "frontmost_application_if",
                "bundle_identifiers": ["app.zen-browser.zen"]
            }
        ],
        description=description
    )

def create_zen_browser_rule(bindings: List[Tuple[str, str, List[str], str]]) -> KarabinerRule:
    return KarabinerRule(
        description="Hyper key bindings untuk Zen browser",
        manipulators=[
            create_zen_browser_manipulator(from_key, to_key, to_modifiers, description)
            for from_key, to_key, to_modifiers, description in bindings
        ]
    )
