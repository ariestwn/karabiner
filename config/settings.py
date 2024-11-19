# config/settings.py
from config import To, open_app, app, rectangle, run_shell_command, run_automator, canva_action

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
    "c": app("cursor"),
    "n": app("Obsidian"),
    "t": app("iTerm"),
    "f": app("Finder"),
    "m": app("Messages"),
    "w": app("WhatsApp"),
    "a": app("Arc"),
    "r": app("Screen Studio Beta"),
}

# Window management
SUBLAYER_WINDOW = {
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
    "h": open_app("alfred://runtrigger/com.zeitlings.gpt.nexus/chat.view.archive/"), #archive ayai
    "i": {"to": [To(key_code="i", modifiers=["right_command", "right_option"])], "description": "Inference Action Ayai"},
    "p": open_app("alfred://runtrigger/com.zeitlings.colorpicker/cPicker/"), #colorPicker trigger
    "s": {"to": [To(key_code="s", modifiers=["right_command", "right_option"])], "description": "Alfred Snippet"},
    "c": {"to": [To(key_code="c", modifiers=["right_command", "right_option"])], "description": "Alfred Clipboard History"},
}

# Quick Access (directly with Hyper key, no sublayer needed)
SUBLAYER_QUICK = {
    "spacebar": {"to": [To(key_code="f4", modifiers=["right_command"])], "description": "Open/Close Alfred"},
    "period": {"to": [To(key_code="period", modifiers=["left_shift", "left_command"])], "description": "Show/Hide Hidden File Finder"},
    "t": app("Things3"),
    "k": app("Authy"),
    "m": app("Mail"),  
}

SUBLAYER_CANVA = {
    "c": open_app("raycast://extensions/thomas/color-picker/pick-color"),
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