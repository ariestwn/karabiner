# config/sublayers.py
from typing import Dict, List, Union
from config import From, To, Manipulator, KarabinerRule, KeyCode

def generate_sublayer_variable_name(key: KeyCode) -> str:
    return f"hyper_sublayer_{key}"

def create_hyper_sublayer(
    sublayer_key: KeyCode,
    commands: Dict[KeyCode, Dict],
    all_sublayer_variables: List[str]
) -> List[Manipulator]:
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
