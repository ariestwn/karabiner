import json
from typing import Dict, List, Union, Optional, Literal

# Type definitions
KeyCode = str
ModifiersKeys = Literal[
    "caps_lock", "left_command", "left_control", "left_option", "left_shift",
    "right_command", "right_control", "right_option", "right_shift",
    "fn", "command", "control", "option", "shift", "left_alt", "left_gui",
    "right_alt", "right_gui", "any"
]

class From:
    def __init__(self, key_code: KeyCode, modifiers: Optional[Dict[str, List[ModifiersKeys]]] = None):
        self.key_code = key_code
        self.modifiers = modifiers

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

class To:
    def __init__(
        self,
        key_code: Optional[KeyCode] = None,
        modifiers: Optional[List[ModifiersKeys]] = None,
        shell_command: Optional[str] = None,
        set_variable: Optional[Dict[str, Union[str, bool, int]]] = None
    ):
        self.key_code = key_code
        self.modifiers = modifiers
        self.shell_command = shell_command
        self.set_variable = set_variable

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

class Manipulator:
    def __init__(
        self,
        type: Literal["basic"],
        from_: From,
        to: Optional[List[To]] = None,
        to_after_key_up: Optional[List[To]] = None,
        to_if_alone: Optional[List[To]] = None,
        description: Optional[str] = None,
        conditions: Optional[List[Dict]] = None
    ):
        self.type = type
        self.from_ = from_
        self.to = to
        self.to_after_key_up = to_after_key_up
        self.to_if_alone = to_if_alone
        self.description = description
        self.conditions = conditions

    def to_dict(self):
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

class KarabinerRule:
    def __init__(self, description: str, manipulators: List[Manipulator]):
        self.description = description
        self.manipulators = manipulators

    def to_dict(self):
        return {
            "description": self.description,
            "manipulators": [m.to_dict() for m in self.manipulators]
        }

# Utility functions
def open_app(*what: str) -> Dict:
    return {
        "to": [To(shell_command=f"open {w}") for w in what],
        "description": f"Open {' & '.join(what)}"
    }

def run_automator(path: str) -> Dict:
    file_name = path.split('/')[-1]
    file_type = 'workflow' if path.endswith('.workflow') else 'app'
    return {
        "to": [To(shell_command=f"open '{path}'")],
        "description": f"Run Automator {file_type}: {file_name}"
    }

# Updated function to handle shell commands by opening iTerm2 first
def run_shell_command(command: str, description: str) -> Dict:
    escaped_command = command.replace('"', '\\"').replace("'", "'\\''")
    iterm_script = f'''
    on run
        if application "iTerm" is running then
            tell application "iTerm"
                activate
                try
                    select first window
                on error
                    create window with default profile
                end try
                tell current window
                    create tab with default profile
                    tell current session
                        write text "{escaped_command}"
                    end tell
                end tell
            end tell
        else
            tell application "iTerm"
                activate
                tell current window
                    tell current session
                        write text "{escaped_command}"
                    end tell
                end tell
            end tell
        end if
    end run
    '''
    return {
        "to": [To(shell_command=f"osascript -e '{iterm_script}'")],
        "description": description
    }

def rectangle(name: str) -> Dict:
    return {
        "to": [To(shell_command=f"open -g rectangle://execute-action?name={name}")],
        "description": f"Window: {name}"
    }

def app(name: str) -> Dict:
    return open_app(f"-a '{name}.app'")

def generate_sublayer_variable_name(key: KeyCode) -> str:
    return f"hyper_sublayer_{key}"

def create_hyper_sublayer(sublayer_key: KeyCode, commands: Dict[KeyCode, Dict], all_sublayer_variables: List[str]) -> List[Manipulator]:
    sublayer_variable_name = generate_sublayer_variable_name(sublayer_key)
    
    manipulators = [
        Manipulator(
            type="basic",
            from_=From(key_code=sublayer_key, modifiers={"optional": ["any"]}),
            to=[To(set_variable={"name": sublayer_variable_name, "value": 1})],
            to_after_key_up=[To(set_variable={"name": sublayer_variable_name, "value": 0})],
            description=f"Toggle Hyper sublayer {sublayer_key}",
            conditions=[
                {"type": "variable_if", "name": var, "value": 0}
                for var in all_sublayer_variables if var != sublayer_variable_name
            ] + [{"type": "variable_if", "name": "hyper", "value": 1}]
        )
    ]
    
    for command_key, command in commands.items():
        to_list = []
        if isinstance(command, dict) and "to" in command:
            for to_item in command["to"]:
                if isinstance(to_item, dict):
                    to_list.append(To(**to_item))
                elif isinstance(to_item, To):
                    to_list.append(to_item)
        elif isinstance(command, dict) and "shell_command" in command:
            to_list.append(To(shell_command=command["shell_command"]))
        
        manipulators.append(
            Manipulator(
                type="basic",
                from_=From(key_code=command_key, modifiers={"optional": ["any"]}),
                to=to_list,
                description=command.get("description"),
                conditions=[{"type": "variable_if", "name": sublayer_variable_name, "value": 1}]
            )
        )
    
    return manipulators

def create_hyper_sublayers(sublayers: Dict[KeyCode, Union[Dict[KeyCode, Dict], Dict]]) -> List[KarabinerRule]:
    all_sublayer_variables = [generate_sublayer_variable_name(key) for key in sublayers.keys()]
    
    rules = []
    for key, value in sublayers.items():
        if isinstance(value, dict) and "to" in value:
            to_list = []
            for to_item in value["to"]:
                if isinstance(to_item, dict):
                    to_list.append(To(**to_item))
                elif isinstance(to_item, To):
                    to_list.append(to_item)
                else:
                    raise ValueError(f"Unexpected 'to' item type: {type(to_item)}")
            
            rules.append(KarabinerRule(
                description=f"Hyper Key + {key}",
                manipulators=[
                    Manipulator(
                        type="basic",
                        from_=From(key_code=key, modifiers={"optional": ["any"]}),
                        to=to_list,
                        description=value.get("description"),
                        conditions=[
                            {"type": "variable_if", "name": "hyper", "value": 1},
                            *[{"type": "variable_if", "name": var, "value": 0} for var in all_sublayer_variables]
                        ]
                    )
                ]
            ))
        else:
            rules.append(KarabinerRule(
                description=f"Hyper Key sublayer \"{key}\"",
                manipulators=create_hyper_sublayer(key, value, all_sublayer_variables)
            ))
    
    return rules

# New function to create simple Hyper shortcuts
def create_simple_hyper_shortcuts(shortcuts: Dict[str, Dict[str, str]], sublayers: Dict[str, Union[Dict[str, Dict], Dict]]) -> List[KarabinerRule]:
    rules = []
    for key, action in shortcuts.items():
        if key in sublayers:
            print(f"Warning: Hyper + {key.upper()} is already used as a sublayer. Skipping simple shortcut.")
            continue
        rules.append(KarabinerRule(
            description=f"Hyper + {key.upper()} to {action['description']}",
            manipulators=[
                Manipulator(
                    type="basic",
                    from_=From(key_code=key),
                    to=[To(shell_command=action['command'])],
                    conditions=[{"type": "variable_if", "name": "hyper", "value": 1}] +
                               [{"type": "variable_if", "name": f"hyper_sublayer_{sl}", "value": 0} for sl in sublayers],
                    description=action['description']
                )
            ]
        ))
    return rules

# Define your simple Hyper shortcuts here
simple_hyper_shortcuts = {
    "t": {"description": "Open Things", "command": "open -a 'Things3.app'"},
    # Add more shortcuts here as needed
}

sublayers = {
        "spacebar": open_app("raycast://extensions/stellate/mxstbr-commands/create-notion-todo"),
        "b": {
            "x": open_app("https://jable.tv"),
            "t": open_app("https://www.tokopedia.com/"),
            "g": open_app("https://meet.google.com/landing?authuser=1"),
            "r": open_app("https://reddit.com"),
            "s": open_app("https://shopee.co.id"),
        },
        "o": {
            "p": app("Passwords"),
            "v": app("OpenVPN Connect"),
            "s": app("Slack"),
            "n": app("Obsidian"),
            "t": app("iTerm"),
            "f": app("Finder"),
            "m": app("Messages"),
            "a": app("Arc"),
            "r": app("Screen Studio Beta"),
        },
        "w": {
            "semicolon": {"to": [To(key_code="h", modifiers=["right_command"])], "description": "Window: Hide"},
            "y": rectangle("previous-display"),
            "o": rectangle("next-display"),
            "k": rectangle("top-half"),
            "j": rectangle("bottom-half"),
            "h": rectangle("left-half"),
            "l": rectangle("right-half"),
            "f": rectangle("maximize"),
            "r": rectangle("restore"),
            #"u": {"to": [To(key_code="tab", modifiers=["right_control", "right_shift"])], "description": "Window: Previous Tab"},
            #"i": {"to": [To(key_code="tab", modifiers=["right_control"])], "description": "Window: Next Tab"},
            #"n": {"to": [To(key_code="grave_accent_and_tilde", modifiers=["right_command"])], "description": "Window: Next Window"},
            #"b": {"to": [To(key_code="open_bracket", modifiers=["right_command"])], "description": "Window: Back"},
            #"m": {"to": [To(key_code="close_bracket", modifiers=["right_command"])], "description": "Window: Forward"},
        },
        "a": {
            "d": run_automator("/Users/ariestwn/bin/delete-old-media.app"),
        },
        "i": {
            "k": run_shell_command("python /Users/ariestwn/Downloads/Kitabisa/download.py", "Run Kitabisa download script"),
            "f": run_shell_command("fastfetch", "Run Fastfetch"),
        },
        #"s": {
        #    "u": {"to": [To(key_code="volume_increment")]},
        #    "j": {"to": [To(key_code="volume_decrement")]},
        #    "i": {"to": [To(key_code="display_brightness_increment")]},
        #    "k": {"to": [To(key_code="display_brightness_decrement")]},
        #    "l": {"to": [To(key_code="q", modifiers=["right_control", "right_command"])]},
        #    "p": {"to": [To(key_code="play_or_pause")]},
        #    "semicolon": {"to": [To(key_code="fastforward")]},
        #    "e": open_app("raycast://extensions/thomas/elgato-key-light/toggle?launchType=background"),
        #    "d": open_app("raycast://extensions/yakitrak/do-not-disturb/toggle?launchType=background"),
        #    "t": open_app("raycast://extensions/raycast/system/toggle-system-appearance"),
        #    "c": open_app("raycast://extensions/raycast/system/open-camera"),
        #   "v": {"to": [To(key_code="spacebar", modifiers=["left_option"])]},
        #},
        #"v": {
        #    "h": {"to": [To(key_code="left_arrow")]},
        #    "j": {"to": [To(key_code="down_arrow")]},
        #    "k": {"to": [To(key_code="up_arrow")]},
        #    "l": {"to": [To(key_code="right_arrow")]},
        #    "m": {"to": [To(key_code="f", modifiers=["right_control"])]},
        #    "s": {"to": [To(key_code="j", modifiers=["right_control"])]},
        #    "d": {"to": [To(key_code="d", modifiers=["right_shift", "right_command"])]},
        #    "u": {"to": [To(key_code="page_down")]},
        #    "i": {"to": [To(key_code="page_up")]},
        #},
        #"c": {
        #    "p": {"to": [To(key_code="play_or_pause")]},
        #    "n": {"to": [To(key_code="fastforward")]},
        #    "b": {"to": [To(key_code="rewind")]},
        #},
        #"r": {
        #    "c": open_app("raycast://extensions/thomas/color-picker/pick-color"),
        #    "n": open_app("raycast://script-commands/dismiss-notifications"),
        #    "l": open_app("raycast://extensions/stellate/mxstbr-commands/create-mxs-is-shortlink"),
        #    "e": open_app("raycast://extensions/raycast/emoji-symbols/search-emoji-symbols"),
        #    "p": open_app("raycast://extensions/raycast/raycast/confetti"),
        #    "a": open_app("raycast://extensions/raycast/raycast-ai/ai-chat"),
        #    "s": open_app("raycast://extensions/peduarte/silent-mention/index"),
        #    "h": open_app("raycast://extensions/raycast/clipboard-history/clipboard-history"),
        #    "1": open_app("raycast://extensions/VladCuciureanu/toothpick/connect-favorite-device-1"),
        #    "2": open_app("raycast://extensions/VladCuciureanu/toothpick/connect-favorite-device-2"),
        #},
}

# Main configuration
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
    *create_simple_hyper_shortcuts(simple_hyper_shortcuts, sublayers),
    *create_hyper_sublayers(sublayers),
    KarabinerRule(
        description="Change Backspace to Spacebar when Minecraft is focused",
        manipulators=[
            Manipulator(
                type="basic",
                from_=From(key_code="delete_or_backspace"),
                to=[To(key_code="spacebar")],
                conditions=[{
                    "type": "frontmost_application_if",
                    "file_paths": [
                        "^/Users/mxstbr/Library/Application Support/minecraft/runtime/java-runtime-gamma/mac-os-arm64/java-runtime-gamma/jre.bundle/Contents/Home/bin/java$"
                    ]
                }]
            )
        ]
    )
]

# Generate the final configuration
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
            "devices": [
                {
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
            ],
            "virtual_hid_keyboard": {
                "keyboard_type_v2": "ansi"
            }
        }
    ]
}

# Write the configuration to a file
with open("karabiner.json", "w") as f:
    json.dump(config, f, indent=2)

print("Karabiner-Elements configuration has been generated and saved to karabiner.json")