# Karabiner-Elements Configuration Generator

This Python script generates custom configurations for Karabiner-Elements, a powerful keyboard customization tool for macOS. It allows you to create complex modifications, including Hyper key setup, sublayers, and custom shortcuts.

## Features

- **Hyper Key**: Transform Caps Lock into a powerful Hyper key (⌃⌥⇧⌘).
- **Sublayers**: Create multiple sublayers activated by holding Hyper + another key.
- **Custom Shortcuts**: Define simple Hyper key shortcuts for quick actions.
- **App Launching**: Easily set up shortcuts to open applications or URLs.
- **Window Management**: Integration with Rectangle for window management shortcuts.
- **Automator Integration**: Run Automator workflows or applications with custom shortcuts.
- **Shell Command Execution**: Run shell commands directly from keyboard shortcuts.
- **iTerm2 Integration**: Open iTerm2 and run commands efficiently.

## Requirements

- Python 3.6+
- Karabiner-Elements installed on your macOS
- (Optional) Rectangle app for window management features
- (Optional) iTerm2 for terminal command execution

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/ariestwn/karabiner.git
   cd karabiner
   ```

2. Ensure you have Python 3.6+ installed.

3. Install Karabiner-Elements if not already: [Karabiner-Elements](https://karabiner-elements.pqrs.org/)

4. (Optional) Install Rectangle for window management: [Rectangle](https://rectangleapp.com/)

5. (Optional) Install iTerm2 for better terminal integration: [iTerm2](https://iterm2.com/)

## Usage

1. Edit the following files to customize your configuration:
   - `config.py`: Define sublayers and simple shortcuts.
   - `functions.py`: Contains utility functions for creating configurations.
   - `karabiner.py`: Main script to generate the Karabiner-Elements configuration.

2. Run the script to generate the Karabiner-Elements configuration:
   ```
   python karabiner.py
   ```

3. The script will generate a `karabiner.json` file in the same directory.

4. Copy the generated `karabiner.json` to your Karabiner-Elements configuration directory:
   ```
   cp karabiner.json ~/.config/karabiner/
   ```

5. Restart Karabiner-Elements or reload the configuration from Karabiner-Elements preferences.

## Customization

### Adding Sublayers

Modify the `sublayers` dictionary in `config.py`. Example:

```python
sublayers = {
    "b": {
        "x": open_app("https://example.com"),
        "t": open_app("https://another-example.com"),
    },
    "o": {
        "s": app("Slack"),
        "f": app("Finder"),
    },
    # Add more sublayers and shortcuts as needed
}
```

### Adding Simple Shortcuts

Modify the `simple_hyper_shortcuts` dictionary in `config.py`:

```python
simple_hyper_shortcuts = {
    "t": {"description": "Open Things", "command": "open -a 'Things3.app'"},
    # Add more shortcuts here
}
```

### Running Shell Commands

Use the `run_shell_command` function from `functions.py` in your sublayers or simple shortcuts:

```python
"i": {
    "k": run_shell_command("python /path/to/your/script.py", "Run custom Python script"),
},
```

## Contributing

Contributions are welcome! Feel free to submit Pull Requests.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Karabiner-Elements](https://karabiner-elements.pqrs.org/) for the amazing keyboard customization tool.
- [Rectangle](https://rectangleapp.com/) for window management capabilities.
- [iTerm2](https://iterm2.com/) for enhanced terminal functionality.