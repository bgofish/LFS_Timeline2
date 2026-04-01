# SPDX-FileCopyrightText: 2025
# SPDX-License-Identifier: GPL-3.0-or-later

PLUGIN_NAME = "Training Render Spreadsheet"
PLUGIN_VERSION = "1.0"

from .panels.training_render import setup_data_binding, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def initialize(context):
    """Entry point for LichtFeld Studio plugins."""
    setup_data_binding(context)
    
    # Register the spreadsheet UI and the logic operator
    context.registry.register_class(KeyframeSpreadsheetPanel)
    context.registry.register_class(StartEditorOperator)
    
    print(f"{PLUGIN_NAME} initialized successfully.")
