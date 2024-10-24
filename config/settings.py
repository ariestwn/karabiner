# config/settings.py
from .models import To

# Browser-related URLs and apps
SUBLAYER_BROWSER = {
    "x": {"to": [To(shell_command="open https://x.com")], "description": "Open X (Twitter)"},
    "t": {"to": [To(shell_command="open https://www.tokopedia.com/")], "description": "Open Tokopedia"},
    "g": {"to": [To(shell_command="open https://meet.google.com/landing?authuser=1")], "description": "Open Google Meet"},
    "r": {"to": [To(shell_command="open https://reddit.com")], "description": "Open Reddit"},
    "s": {"to": [To(shell_command="open https://shopee.co.id")], "description": "Open Shopee"},
}

# Application shortcuts
SUBLAYER_APPS = {
    "p": {"to": [To(shell_command="open -a 'Passwords.app'")], "description": "Open Passwords"},
    "v": {"to": [To(shell_command="open -a 'OpenVPN Connect.app'")], "description": "Open OpenVPN"},
    "s": {"to": [To(shell_command="open -a 'Slack.app'")], "description": "Open Slack"},
    "c": {"to": [To(shell_command="open -a 'Canva.app'")], "description": "Open Canva"},
    "n": {"to": [To(shell_command="open -a 'Obsidian.app'")], "description": "Open Obsidian"},
    "t": {"to": [To(shell_command="open -a 'iTerm.app'")], "description": "Open iTerm"},
    "f": {"to": [To(shell_command="open -a 'Finder.app'")], "description": "Open Finder"},
    "m": {"to": [To(shell_command="open -a 'Messages.app'")], "description": "Open Messages"},
    "a": {"to": [To(shell_command="open -a 'Arc.app'")], "description": "Open Arc"},
    "r": {"to": [To(shell_command="open -a 'Screen Studio Beta.app'")], "description": "Open Screen Studio"},
}

# Window management
SUBLAYER_WINDOW = {
    "semicolon": {"to": [To(key_code="h", modifiers=["right_command"])], "description": "Window: Hide"},
    "y": {"to": [To(shell_command="open -g rectangle://execute-action?name=previous-display")], "description": "Window: Previous Display"},
    "o": {"to": [To(shell_command="open -g rectangle://execute-action?name=next-display")], "description": "Window: Next Display"},
    "k": {"to": [To(shell_command="open -g rectangle://execute-action?name=top-half")], "description": "Window: Top Half"},
    "j": {"to": [To(shell_command="open -g rectangle://execute-action?name=bottom-half")], "description": "Window: Bottom Half"},
    "h": {"to": [To(shell_command="open -g rectangle://execute-action?name=left-half")], "description": "Window: Left Half"},
    "l": {"to": [To(shell_command="open -g rectangle://execute-action?name=right-half")], "description": "Window: Right Half"},
    "f": {"to": [To(shell_command="open -g rectangle://execute-action?name=maximize")], "description": "Window: Maximize"},
    "r": {"to": [To(shell_command="open -g rectangle://execute-action?name=restore")], "description": "Window: Restore"},
    "c": {"to": [To(shell_command="open -g rectangle://execute-action?name=center")], "description": "Window: Center"},
    "open_bracket": {"to": [To(shell_command="open -g rectangle://execute-action?name=smaller")], "description": "Window: Smaller"},
    "close_bracket": {"to": [To(shell_command="open -g rectangle://execute-action?name=larger")], "description": "Window: Larger"},
    "u": {"to": [To(key_code="tab", modifiers=["right_control", "right_shift"])], "description": "Window: Previous Tab"},
    "i": {"to": [To(key_code="tab", modifiers=["right_control"])], "description": "Window: Next Tab"},
    "t": {"to": [To(key_code="grave_accent_and_tilde", modifiers=["right_command"])], "description": "Window: Switch window in same app"},
}

# Shell commands and scripts
SUBLAYER_TERMINAL = {
    "k": {"to": [To(shell_command="python /Users/ariestwn/Downloads/Kitabisa/download.py")], "description": "Run Kitabisa download script"},
    "f": {"to": [To(shell_command="fastfetch")], "description": "Run Fastfetch"},
}

# System commands
SUBLAYER_SYSTEM = {
    "d": {"to": [To(shell_command="open '/Users/ariestwn/bin/delete-old-media.app'")], "description": "Run delete old media script"},
    "l": {"to": [To(key_code="q", modifiers=["right_control", "right_command"])], "description": "System: Lock"},
    "v": {"to": [To(key_code="spacebar", modifiers=["left_option"])], "description": "System: Quick Look"},
}

# Navigation keys
SUBLAYER_NAV = {
    "h": {"to": [To(key_code="left_arrow")], "description": "Navigation: Left"},
    "j": {"to": [To(key_code="down_arrow")], "description": "Navigation: Down"},
    "k": {"to": [To(key_code="up_arrow")], "description": "Navigation: Up"},
    "l": {"to": [To(key_code="right_arrow")], "description": "Navigation: Right"},
    "m": {"to": [To(key_code="f", modifiers=["right_control"])], "description": "Navigation: Page Forward"},
    "s": {"to": [To(key_code="j", modifiers=["right_control"])], "description": "Navigation: Scroll Down"},
    "d": {"to": [To(key_code="d", modifiers=["right_shift", "right_command"])], "description": "Navigation: Duplicate"},
    "u": {"to": [To(key_code="page_down")], "description": "Navigation: Page Down"},
    "i": {"to": [To(key_code="page_up")], "description": "Navigation: Page Up"},
}

# Media controls
SUBLAYER_MEDIA = {
    "p": {"to": [To(key_code="play_or_pause")], "description": "Media: Play/Pause"},
    "n": {"to": [To(key_code="fastforward")], "description": "Media: Next"},
    "b": {"to": [To(key_code="rewind")], "description": "Media: Previous"},
}

# Alfred Shortcut
SUBLAYER_ALFRED = {
    "c": {"to": [To(key_code="a", modifiers=["right_shift", "right_option"])], "description": "Ayai Workflow Continue Chat"},
    "h": {"to": [To(key_code="a", modifiers=["right_shift", "right_command"])], "description": "Ayai Workflow History Chat"},
    "i": {"to": [To(key_code="i", modifiers=["right_shift", "right_option"])], "description": "Ayai Workflow Action Inference Chat"},
}

# Raycast commands / Uncomment to use this feature
# SUBLAYER_RAYCAST = {
#     "c": {"to": [To(shell_command="open raycast://extensions/thomas/color-picker/pick-color")], "description": "Raycast: Color Picker"},
#     "n": {"to": [To(shell_command="open raycast://script-commands/dismiss-notifications")], "description": "Raycast: Dismiss Notifications"},
#     "l": {"to": [To(shell_command="open raycast://extensions/stellate/mxstbr-commands/create-mxs-is-shortlink")], "description": "Raycast: Create Short Link"},
#     "e": {"to": [To(shell_command="open raycast://extensions/raycast/emoji-symbols/search-emoji-symbols")], "description": "Raycast: Emoji Search"},
#     "p": {"to": [To(shell_command="open raycast://extensions/raycast/raycast/confetti")], "description": "Raycast: Confetti"},
#     "a": {"to": [To(shell_command="open raycast://extensions/raycast/raycast-ai/ai-chat")], "description": "Raycast: AI Chat"},
#     "s": {"to": [To(shell_command="open raycast://extensions/peduarte/silent-mention/index")], "description": "Raycast: Silent Mention"},
#     "h": {"to": [To(shell_command="open raycast://extensions/raycast/clipboard-history/clipboard-history")], "description": "Raycast: Clipboard History"},
#     "1": {"to": [To(shell_command="open raycast://extensions/VladCuciureanu/toothpick/connect-favorite-device-1")], "description": "Raycast: Connect Device 1"},
#     "2": {"to": [To(shell_command="open raycast://extensions/VladCuciureanu/toothpick/connect-favorite-device-2")], "description": "Raycast: Connect Device 2"},
# }

# Main sublayers configuration
SUBLAYERS = {
    "spacebar": {"to": [To(key_code="f4", modifiers=["right_command"])], "description": "Open/Close Alfred"},
    "t": {"to": [To(shell_command="open -a 'Things3.app'")], "description": "Open Things"},
    "k": {"to": [To(shell_command="open -a 'Authy.app'")], "description": "Open Authy"},
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