from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Union, Literal
from .types import KeyCode, ModifiersKeys, ToDict, FromDict

@dataclass
class From:
    key_code: KeyCode
    modifiers: Optional[Dict[str, List[ModifiersKeys]]] = None

    def to_dict(self) -> FromDict:
        return {k: v for k, v in asdict(self).items() if v is not None}

@dataclass
class To:
    key_code: Optional[KeyCode] = None
    modifiers: Optional[List[ModifiersKeys]] = None
    shell_command: Optional[str] = None
    set_variable: Optional[Dict[str, Union[str, bool, int]]] = None

    def to_dict(self) -> ToDict:
        return {k: v for k, v in asdict(self).items() if v is not None}

@dataclass
class Manipulator:
    type: Literal["basic"]
    from_: From
    to: Optional[List[To]] = None
    to_after_key_up: Optional[List[To]] = None
    to_if_alone: Optional[List[To]] = None
    description: Optional[str] = None
    conditions: Optional[List[Dict]] = None

    def to_dict(self) -> Dict:
        result = {"type": self.type, "from": self.from_.to_dict()}
        if self.to:
            result["to"] = [t.to_dict() for t in self.to]
        if self.to_after_key_up:
            result["to_after_key_up"] = [t.to_dict() for t in self.to_after_key_up]
        if self.to_if_alone:
            result["to_if_alone"] = [t.to_dict() for t in self.to_if_alone]
        if self.description:
            result["description"] = self.description
        if self.conditions:
            result["conditions"] = self.conditions
        return result

@dataclass
class KarabinerRule:
    description: str
    manipulators: List[Manipulator]

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "manipulators": [m.to_dict() for m in self.manipulators]
        }