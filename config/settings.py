# config/settings.py
from config import To, open_app, app, rcustomw, raycastw, run_shell_command, run_automator

# Browser-related URLs and apps
SUBLAYER_BROWSER = {
    "x": open_app("https://x.com"),
    "t": open_app("https://www.tokopedia.com/"),
    "g": open_app("https://meet.google.com/landing?authuser=0"),
    "r": open_app("https://reddit.com"),
    "s": open_app("https://shopee.co.id"),
}

# Application shortcuts
SUBLAYER_APPS = {
    "p": app("Passwords"),
    "v": app("OpenVPN Connect"),
    "s": app("Slack"),
    "d": app("Canva"),
    "c": app("Visual Studio Code"),
    "n": app("Obsidian"),
    "t": app("Ghostty"),
    "f": app("Finder"),
    "m": app("Messages"),
    "w": app("WhatsApp"),
    "r": app("Screen Studio"),
    "b": app("Bruno"),
}

# Window management
SUBLAYER_WINDOW = {
    "1": rcustomw("work-v1"),
    "2": rcustomw("work-v2"),
    "3": rcustomw("work-v3"),
    "c": raycastw("center"),
    "r": raycastw("restore"),
    "f": raycastw("maximize"),
    "h": raycastw("left-half"),
    "l": raycastw("right-half"),
    "j": raycastw("top-half"),
    "k": raycastw("bottom-half"),
    "open_bracket": raycastw("make-smaller"),
    "close_bracket": raycastw("make-larger"),
    "right_arrow": raycastw("next-desktop"),
    "left_arrow": raycastw("previous-desktop"),
    "up_arrow": raycastw("next-display"),
    "down_arrow": raycastw("previous-display"),
    # "u": {"to": [To(key_code="tab", modifiers=["right_control", "right_shift"])], "description": "Window: Previous Tab"},
    # "i": {"to": [To(key_code="tab", modifiers=["right_control"])], "description": "Window: Next Tab"},
    # "t": {"to": [To(key_code="grave_accent_and_tilde", modifiers=["right_command"])], "description": "Window: Switch window in same app"},
}

# Shell commands and scripts
SUBLAYER_TERMINAL = {
    "k": run_shell_command("python /Users/ariestwn/Downloads/Kitabisa/download.py", "Run download script"),
    "f": run_shell_command("fastfetch", "Run Fastfetch"),
}

# System commands
SUBLAYER_SYSTEM = {
    "d": run_automator("/Users/ariestwn/bin/delete-old-media.app"),
    "period": open_app("-b 'com.apple.ScreenSaver.Engine'"),
    "l": {"to": [To(key_code="q", modifiers=["right_control", "right_command"])], "description": "System: Lock"},
    "v": {"to": [To(key_code="spacebar", modifiers=["left_option"])], "description": "System: Quick Look"},
}

# Navigation keys
SUBLAYER_NAV = {
    "h": {"to": [To(key_code="left_arrow")], "description": "Navigation: Left"},
    "j": {"to": [To(key_code="down_arrow")], "description": "Navigation: Down"},
    "k": {"to": [To(key_code="up_arrow")], "description": "Navigation: Up"},
    "u": {"to": [To(key_code="page_down")], "description": "Navigation: Page Down"},
    "i": {"to": [To(key_code="page_up")], "description": "Navigation: Page Up"},
    "l": {"to": [To(key_code="right_arrow")], "description": "Navigation: Right"},
}

# Media controls
SUBLAYER_MEDIA = {
    "p": {"to": [To(key_code="play_or_pause")], "description": "Media: Play/Pause"},
    "n": {"to": [To(key_code="fastforward")], "description": "Media: Next"},
    "b": {"to": [To(key_code="rewind")], "description": "Media: Previous"},
}

# Alfred Shortcut
SUBLAYER_ALFRED = {
    "h": open_app("raycast-x://extensions/raycast/ai/ai-chat"), #archive ayai
    "i": open_app("raycast-x://extensions/ariestwn/quickai/improve-writing"),
    "p": open_app("raycast-x://extensions/raycast/raycast/open-camera"), #colorPicker trigger
    "c": open_app("raycast-x://extensions/raycast/clipboard-history/clipboard-history"), #supercmd clipboard history
    "s": open_app("raycast-x://extensions/raycast/snippets/search-snippets"), #supercmd search snippet
    "e": open_app("raycast-x://extensions/raycast/emoji-symbols/search-emoji-symbols"), #supercmd search snippet
}

# Quick Access (directly with Hyper key, no sublayer needed)
SUBLAYER_QUICK = {
    "spacebar": {"to": [To(key_code="f4", modifiers=["right_command"])], "description": "Open/Close Alfred"},
    "period": {"to": [To(key_code="period", modifiers=["left_shift", "left_command"])], "description": "Show/Hide Hidden File Finder"},
}

# Preserved Shottr commands (commented out) 
SUBLAYER_SHOTTR = {
    "1": {"to": [To(key_code="0", modifiers=["right_shift", "right_command"])], "description": "OCR Screenshot Alfred Shortcuts"},
    "2": open_app("shottr://grab/area"), #select area then copy to clip
    "3": open_app("shottr://grab/window"), #select window then copy to clip
    "4": open_app("shottr://grab/fullscreen?then=save"), #select scroll then copy to clip
    "c": open_app("shottr://load/clipboard"), #select window then copy to clip
}

# Main sublayers configuration
SUBLAYERS = {
    **SUBLAYER_QUICK,
    "tab": SUBLAYER_SHOTTR,
    "b": SUBLAYER_BROWSER,
    "o": SUBLAYER_APPS,
    "w": SUBLAYER_WINDOW,
    "i": SUBLAYER_TERMINAL,
    "s": SUBLAYER_SYSTEM,
    "v": SUBLAYER_NAV,
    "c": SUBLAYER_MEDIA,
    "a": SUBLAYER_ALFRED
}

# Zen browser specific bindings
ZEN_BROWSER_BINDINGS = [
    ("n", "p", ["left_command", "left_shift"], "Open new private window in Zen"),
    ("right_arrow", "right_arrow", ["left_command", "left_option", "left_control"], "Zen: Next workspace"),
    ("left_arrow", "left_arrow", ["left_command", "left_option", "left_control"], "Zen: Previous workspace"),
    ("1", "1", ["left_command", "left_option", "left_control"], "Zen: Workspace 1"),
    ("2", "2", ["left_command", "left_option", "left_control"], "Zen: Workspace 2"),
    ("3", "3", ["left_command", "left_option", "left_control"], "Zen: Workspace 3"),
]