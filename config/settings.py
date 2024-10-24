# config/settings.py
from .models import To
from .actions import run_automator, run_shell_command, rectangle, open_app, app, canva_action

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
    "c": app("Canva"),
    "n": app("Obsidian"),
    "t": app("iTerm"),
    "f": app("Finder"),
    "m": app("Messages"),
    "a": app("Arc"),
    "r": app("Screen Studio Beta"),
}

# Window management
SUBLAYER_WINDOW = {
    "semicolon": {"to": [To(key_code="h", modifiers=["right_command"])], "description": "Window: Hide"},
    "y": rectangle("previous-display"),
    "o": rectangle("next-display"),
    "k": rectangle("top-half"),
    "j": rectangle("bottom-half"),
    "h": rectangle("left-half"),
    "l": rectangle("right-half"),
    "f": rectangle("maximize"),
    "r": rectangle("restore"),
    "c": rectangle("center"),
    "open_bracket": rectangle("smaller"),
    "close_bracket": rectangle("larger"),
    "u": {"to": [To(key_code="tab", modifiers=["right_control", "right_shift"])], "description": "Window: Previous Tab"},
    "i": {"to": [To(key_code="tab", modifiers=["right_control"])], "description": "Window: Next Tab"},
    "t": {"to": [To(key_code="grave_accent_and_tilde", modifiers=["right_command"])], "description": "Window: Switch window in same app"},
}

# Shell commands and scripts
SUBLAYER_TERMINAL = {
    "k": run_shell_command("python /Users/ariestwn/Downloads/Kitabisa/download.py", "Run Kitabisa download script"),
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
    "spacebar": {"to": [To(key_code="a", modifiers=["right_shift", "right_option"])], "description": "Ayai Workflow Continue Chat"},
    "h": {"to": [To(key_code="a", modifiers=["right_shift", "right_command"])], "description": "Ayai Workflow History Chat"},
    "i": {"to": [To(key_code="i", modifiers=["right_shift", "right_option"])], "description": "Ayai Workflow Action Inference Chat"},
    "c": {"to": [To(key_code="c", modifiers=["right_command", "right_option"])], "description": "Alfred Clipboard history"},
    "s": {"to": [To(key_code="s", modifiers=["right_command", "right_option"])], "description": "Alfred Snippet"},
}

# Quick Access (directly with Hyper key, no sublayer needed)
SUBLAYER_QUICK = {
    "spacebar": {"to": [To(key_code="f4", modifiers=["right_command"])], "description": "Open/Close Alfred"},
    "period": {"to": [To(key_code="period", modifiers=["left_shift", "left_command"])], "description": "Open/Close Alfred"},
    "t": app("Things3"),
    "k": app("Authy"),
}

SUBLAYER_CANVA = {
    # New content
    "n": canva_action("new_design"),
    "p": canva_action("new_presentation"),
    "i": canva_action("new_instagram"),
    "s": canva_action("new_story"),
    "f": canva_action("new_facebook"),
    "v": canva_action("new_video"),
    
    # Resources
    "t": canva_action("templates"),
    "h": canva_action("photos"),
    "e": canva_action("elements"),
    "o": canva_action("fonts"),
    
    # Management
    "m": canva_action("projects"),
    "b": canva_action("brand_kit"),
    "d": canva_action("designs"),
    "l": canva_action("logos"),
}

# Raycast commands (commented out)
# SUBLAYER_RAYCAST = {
#     "c": open_app("raycast://extensions/thomas/color-picker/pick-color"),
#     "n": open_app("raycast://script-commands/dismiss-notifications"),
#     "l": open_app("raycast://extensions/stellate/mxstbr-commands/create-mxs-is-shortlink"),
#     "e": open_app("raycast://extensions/raycast/emoji-symbols/search-emoji-symbols"),
#     "p": open_app("raycast://extensions/raycast/raycast/confetti"),
#     "a": open_app("raycast://extensions/raycast/raycast-ai/ai-chat"),
#     "s": open_app("raycast://extensions/peduarte/silent-mention/index"),
#     "h": open_app("raycast://extensions/raycast/clipboard-history/clipboard-history"),
#     "1": open_app("raycast://extensions/VladCuciureanu/toothpick/connect-favorite-device-1"),
#     "2": open_app("raycast://extensions/VladCuciureanu/toothpick/connect-favorite-device-2"),
# }

# Main sublayers configuration
SUBLAYERS = {
    **SUBLAYER_QUICK,
    "x": SUBLAYER_CANVA,
    "b": SUBLAYER_BROWSER,
    "o": SUBLAYER_APPS,
    "w": SUBLAYER_WINDOW,
    "i": SUBLAYER_TERMINAL,
    "s": SUBLAYER_SYSTEM,
    "v": SUBLAYER_NAV,
    "c": SUBLAYER_MEDIA,
    "a": SUBLAYER_ALFRED
}

# Arc browser specific bindings
ARC_BROWSER_BINDINGS = [
    ("n", "n", ["left_command", "left_shift"], "Open new incognito window in Arc"),
    ("l", "n", ["left_command", "left_option"], "Open little browser in Arc"),
    ("equal_sign", "equal_sign", ["left_shift", "left_control"], "Open little browser in Arc"),
]