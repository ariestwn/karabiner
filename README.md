# Karabiner Elements Configuration Generator

A Python-based configuration generator for Karabiner Elements that transforms your Caps Lock into a powerful Hyper key with multiple sublayers of functionality.

## Features

### 1. Hyper Key System
- **Primary Hyper Key**: Caps Lock transforms into a powerful modifier key
- **When pressed alone**: Acts as Escape
- **When held**: Activates Hyper mode for accessing all sublayers

### 2. Sublayer System
Each sublayer is activated by holding Hyper + the sublayer key:

#### Browser Shortcuts (Hyper + B)
- `B + X` - Open X (Twitter)
- `B + T` - Open Tokopedia
- `B + G` - Open Google Meet
- `B + R` - Open Reddit
- `B + S` - Open Shopee

#### Application Launchers (Hyper + O)
- `O + P` - Open Passwords
- `O + V` - Open OpenVPN Connect
- `O + S` - Open Slack
- `O + C` - Open Canva
- `O + N` - Open Obsidian
- `O + T` - Open iTerm
- `O + F` - Open Finder
- `O + M` - Open Messages
- `O + A` - Open Arc
- `O + R` - Open Screen Studio Beta

#### Window Management (Hyper + W)
- `W + ;` - Hide window
- `W + Y/O` - Move to previous/next display
- `W + K/J` - Top/bottom half
- `W + H/L` - Left/right half
- `W + F` - Maximize
- `W + R` - Restore
- `W + C` - Center
- `W + [/]` - Smaller/larger
- `W + U/I` - Previous/next tab
- `W + T` - Switch window in same app

#### Terminal Commands (Hyper + I)
- `I + K` - Run Kitabisa download script
- `I + F` - Run Fastfetch

#### System Commands (Hyper + S)
- `S + D` - Run delete old media script
- `S + L` - Lock system
- `S + V` - Quick Look

#### Navigation (Hyper + V)
- `V + H/J/K/L` - Arrow keys
- `V + M` - Page forward
- `V + S` - Scroll down
- `V + D` - Duplicate
- `V + U/I` - Page down/up

#### Media Controls (Hyper + C)
- `C + P` - Play/pause
- `C + N` - Next track
- `C + B` - Previous track

#### Raycast Integration (Hyper + R)
- `R + C` - Color picker
- `R + N` - Dismiss notifications
- `R + L` - Create short link
- `R + E` - Emoji search
- `R + P` - Confetti
- `R + A` - AI chat
- `R + S` - Silent mention
- `R + H` - Clipboard history
- `R + 1/2` - Connect favorite devices

### 3. Arc Browser Integration
Special shortcuts when Arc browser is active:
- `Hyper + N` - New incognito window
- `Hyper + L` - Open little browser

## Prerequisites

1. [Karabiner Elements](https://karabiner-elements.pqrs.org/) installed
2. Python 3.x installed
3. [Rectangle](https://rectangleapp.com/) for window management features
4. [Raycast](https://www.raycast.com/) for Raycast integration features

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/karabiner-config.git
cd karabiner-config
```

2. Generate the configuration:
```bash
python generate.py
```

3. Copy the generated configuration:
```bash
cp karabiner.json ~/.config/karabiner/
```

## Customization

### Modifying Sublayers
Edit `config/settings.py` to modify existing sublayers or add new ones:

```python
SUBLAYER_BROWSER = {
    "x": {"to": [To(shell_command="open https://x.com")], "description": "Open X"},
    # Add more browser shortcuts
}

SUBLAYER_APPS = {
    "s": {"to": [To(shell_command="open -a 'Slack.app'")], "description": "Open Slack"},
    # Add more app shortcuts
}
```

### Adding New Sublayers
1. Define a new sublayer in `config/settings.py`
2. Add it to the `SUBLAYERS` dictionary
3. Regenerate the configuration

### Modifying Device Settings
Edit the device profile in `generate.py` to match your keyboard:

```python
def create_device_profile():
    return {
        "disable_built_in_keyboard_if_exists": True,
        "identifiers": {
            "is_keyboard": True,
            "is_pointing_device": True,
            "product_id": YOUR_PRODUCT_ID,
            "vendor_id": YOUR_VENDOR_ID
        },
        "ignore": False,
        "manipulate_caps_lock_led": False
    }
```

## Project Structure
```
karabiner/
├── config/
│   ├── __init__.py
│   ├── models.py        # Data models for Karabiner configuration
│   ├── types.py         # Type definitions
│   ├── actions.py       # Helper functions for actions
│   ├── sublayers.py     # Sublayer creation logic
│   ├── settings.py      # Sublayer configurations
│   └── apps/
│       ├── __init__.py
│       └── arc.py       # Arc browser specific configurations
└── generate.py          # Main configuration generator
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT License - feel free to use and modify as needed.

## Acknowledgments

- [Karabiner Elements](https://karabiner-elements.pqrs.org/)
- [Rectangle](https://rectangleapp.com/)
- [Raycast](https://www.raycast.com/)