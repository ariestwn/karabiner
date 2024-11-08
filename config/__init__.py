# config/__init__.py

# Core models
from .models import From, To, Manipulator, KarabinerRule

# Types
from .types import KeyCode, ModifiersKeys

# Actions
from .actions import (
    open_app,
    app,
    rectangle,
    run_shell_command,
    run_automator,
    canva_action,
)

# Sublayer functions
from .sublayers import (
    create_hyper_sublayer,
    create_hyper_sublayers,
    generate_sublayer_variable_name,
)

# Device profiles
from .device_profiles import create_device_profile

# App-specific functions
from .apps.arc import create_arc_browser_rule, create_arc_browser_manipulator

# Settings and configurations
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
    SUBLAYER_ALFRED,
    SUBLAYER_QUICK,
    SUBLAYER_CANVA,
    SUBLAYER_SHOTTR,
)

__version__ = '1.0.0'

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
    'canva_action',
    
    # Sublayer functions
    'create_hyper_sublayer',
    'create_hyper_sublayers',
    'generate_sublayer_variable_name',
    
    # Device profiles
    'create_device_profile',
    
    # App-specific functions
    'create_arc_browser_rule',
    'create_arc_browser_manipulator',
    
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
    'SUBLAYER_QUICK',
    'SUBLAYER_CANVA',
    'SUBLAYER_SHOTTR',
]