# config/actions.py
from typing import Dict, List
from .models import To

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

def canva_action(action: str) -> Dict:
    urls = {
        # Create new designs
        "new_design": "https://www.canva.com/design?create&type=default",
        "new_presentation": "https://www.canva.com/design?create&type=presentation",
        "new_instagram": "https://www.canva.com/design?create&type=instagram-post",
        "new_story": "https://www.canva.com/design?create&type=instagram-story",
        "new_facebook": "https://www.canva.com/design?create&type=facebook-post",
        "new_video": "https://www.canva.com/design?create&type=video",
        
        # Resources
        "templates": "https://www.canva.com/templates",
        "photos": "https://www.canva.com/photos",
        "elements": "https://www.canva.com/elements",
        "fonts": "https://www.canva.com/font-combinations",
        "icons": "https://www.canva.com/icons",
        "logos": "https://www.canva.com/logos",
        
        # Management
        "projects": "https://www.canva.com/folder/all-designs",
        "brand_kit": "https://www.canva.com/brand",
        "teams": "https://www.canva.com/teams",
        "designs": "https://www.canva.com/your-designs",
        
        # Content types
        "presentations": "https://www.canva.com/presentations",
        "social_media": "https://www.canva.com/social-media",
        "videos": "https://www.canva.com/videos",
        "documents": "https://www.canva.com/documents",
    }
    
    url = urls.get(action, urls["designs"])  # Default to designs if action not found
    return {
        "to": [To(shell_command=f"open '{url}'")],
        "description": f"Canva: {action.replace('_', ' ').title()}"
    }