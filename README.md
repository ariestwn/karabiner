# Karabiner Elements Configuration Generator

A Python-based configuration generator for Karabiner Elements that transforms your Caps Lock into a powerful Hyper key with multiple sublayers of functionality.

## Features

### 1. Hyper Key System
- **Primary Hyper Key**: Caps Lock transforms into a powerful modifier key
- **When pressed alone**: Acts as Escape
- **When held**: Activates Hyper mode for accessing all sublayers

### 2. Sublayer System

#### Quick Access (Hyper + Key)
Direct commands without entering a sublayer:
- `Spacebar` - Open/Close Alfred
- `Period` - Open/Close Alfred
- `T` - Open Things3
- `K` - Open Authy

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
- `S + .` - Start Screen Saver
- `S + L` - Lock system
- `S + V` - Quick Look

#### Navigation (Hyper + V)
- `V + H/J/K/L` - Arrow keys
- `V + U/I` - Page Down/Up

#### Media Controls (Hyper + C)
- `C + P` - Play/pause
- `C + N` - Next track
- `C + B` - Previous track

#### Alfred Workflow (Hyper + A)
- `A + Space` - Continue Chat
- `A + H` - History Chat
- `A + I` - Action Inference Chat
- `A + C` - Clipboard History
- `A + S` - Snippets

#### Canva Integration (Hyper + X)
- New Content:
  - `X + N` - New design
  - `X + P` - New presentation
  - `X + I` - New Instagram post
  - `X + S` - New story
  - `X + F` - New Facebook post
  - `X + V` - New video
- Resources:
  - `X + T` - Templates
  - `X + H` - Photos
  - `X + E` - Elements
  - `X + O` - Fonts
- Management:
  - `X + M` - Projects
  - `X + B` - Brand kit
  - `X + D` - Designs
  - `X + L` - Logos

### 3. Arc Browser Integration
Special shortcuts when Arc browser is active:
- `Hyper + N` - New incognito window
- `Hyper + L` - Open little browser
- `Hyper + =` - Toggle split view

## Prerequisites

1. [Karabiner Elements](https://karabiner-elements.pqrs.org/) installed
2. Python 3.x installed
3. [Rectangle](https://rectangleapp.com/) for window management
4. [iTerm2](https://iterm2.com/) for terminal commands
5. [Alfred](https://www.alfredapp.com/) for Alfred workflows
6. [Arc Browser](https://arc.net/) for Arc-specific features

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

## Project Structure
```
karabiner/
├── config/
│   ├── __init__.py      # Package initialization and exports
│   ├── models.py        # Data models for Karabiner configuration
│   ├── types.py         # Type definitions
│   ├── actions.py       # Action helper functions
│   ├── sublayers.py     # Sublayer creation logic
│   ├── settings.py      # Sublayer configurations
│   └── apps/
│       └── arc.py       # Arc browser specific configurations
└── generate.py          # Main configuration generator
```

## Customization

### Modifying Sublayers
Edit `config/settings.py` to modify existing sublayers or add new ones:

```python
SUBLAYER_BROWSER = {
    "x": open_app("https://x.com"),
    # Add more browser shortcuts
}

SUBLAYER_APPS = {
    "s": app("Slack"),
    # Add more app shortcuts
}
```

### Adding New Actions
Add new action helpers in `config/actions.py`:

```python
def my_custom_action(param: str) -> Dict:
    return {
        "to": [To(shell_command=f"my_command {param}")],
        "description": f"My custom action: {param}"
    }
```

### Modifying Device Settings
Edit device profiles in `config/device_profiles.py`:

```python
def create_device_profile() -> Dict[str, Any]:
    return {
        "disable_built_in_keyboard_if_exists": True,
        "identifiers": {
            "product_id": YOUR_PRODUCT_ID,
            "vendor_id": YOUR_VENDOR_ID
        }
    }
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT License - feel free to use and modify as needed.