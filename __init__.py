# SPDX-License-Identifier: GPL-3.0-or-later

PLUGIN_NAME = "Spreadsheet Editor"
PLUGIN_VERSION = "1.0"

from .panels.training_render import KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def initialize(context):
    """LichtFeld Studio calls this and provides the 'context' object."""
    # Register your classes using the provided context
    context.registry.register_panel(KeyframeSpreadsheetPanel)
    context.registry.register_operator(StartEditorOperator)
    
    print(f"{PLUGIN_NAME} version {PLUGIN_VERSION} initialized.")
