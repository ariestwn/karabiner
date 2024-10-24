# config/__init__.py
from .models import From, To, Manipulator, KarabinerRule
from .types import KeyCode, ModifiersKeys
from .actions import (
    open_app,
    app,
    rectangle,
    run_shell_command,
    run_automator
)
from .sublayers import (
    create_hyper_sublayer,
    create_hyper_sublayers,
    generate_sublayer_variable_name
)
from .device_profiles import create_device_profile
from .settings import (
    SUBLAYERS,
    ARC_BROWSER_BINDINGS,
    SUBLAYER_BROWSER,
    SUBLAYER_APPS,
    SUBLAYER_WINDOW,
    SUBLAYER_TERMINAL,
    SUBLAYER_SYSTEM,
    SUBLAYER_NAV,
    SUBLAYER_MEDIA,
    SUBLAYER_ALFRED
)

__all__ = [
    # Core models
    'From',
    'To',
    'Manipulator',
    'KarabinerRule',
    
    # Types
    'KeyCode',
    'ModifiersKeys',
    
    # Actions
    'open_app',
    'app',
    'rectangle',
    'run_shell_command',
    'run_automator',
    
    # Sublayer functions
    'create_hyper_sublayer',
    'create_hyper_sublayers',
    'generate_sublayer_variable_name',
    
    # Device profiles
    'create_device_profile',
    
    # Settings
    'SUBLAYERS',
    'ARC_BROWSER_BINDINGS',
    'SUBLAYER_BROWSER',
    'SUBLAYER_APPS',
    'SUBLAYER_WINDOW',
    'SUBLAYER_TERMINAL',
    'SUBLAYER_SYSTEM',
    'SUBLAYER_NAV',
    'SUBLAYER_MEDIA',
    'SUBLAYER_ALFRED',
]

__version__ = '1.0.0'