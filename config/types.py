# config/types.py
from typing import Dict, List, Union, Optional, Literal, TypedDict

KeyCode = str
ModifiersKeys = Literal[
    "caps_lock", "left_command", "left_control", "left_option", "left_shift",
    "right_command", "right_control", "right_option", "right_shift",
    "fn", "command", "control", "option", "shift", "left_alt", "left_gui",
    "right_alt", "right_gui", "any"
]

class FromDict(TypedDict, total=False):
    key_code: KeyCode
    modifiers: Dict[str, List[ModifiersKeys]]

class ToDict(TypedDict, total=False):
    key_code: KeyCode
    modifiers: List[ModifiersKeys]
    shell_command: str
    set_variable: Dict[str, Union[str, bool, int]]