# SPDX-License-Identifier: GPL-3.0-or-later
from .panels.training_render import setup_data_binding, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    """
    LichtFeld Studio calls register() and passes the context.
    We use that context to access the registry.
    """
    setup_data_binding(context)
    
    # Registering classes via the context registry
    context.registry.register_class(KeyframeSpreadsheetPanel)
    context.registry.register_class(StartEditorOperator)
    
    print("Spreadsheet Editor Plugin Registered")

def unregister(context):
    context.registry.unregister_class(KeyframeSpreadsheetPanel)
    context.registry.unregister_class(StartEditorOperator)
