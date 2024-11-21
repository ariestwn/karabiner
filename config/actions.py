# config/actions.py
from typing import Dict, List
from config import To

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