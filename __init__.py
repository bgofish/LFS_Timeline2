# SPDX-License-Identifier: GPL-3.0-or-later
from .panels.training_render import setup_data_binding, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    # This must match the function name in training_render.py
    setup_data_binding(context)
    
    context.registry.register_class(KeyframeSpreadsheetPanel)
    context.registry.register_class(StartEditorOperator)
