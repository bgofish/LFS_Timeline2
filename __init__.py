# SPDX-License-Identifier: GPL-3.0-or-later
import lichtfeld
from .panels.training_render import KeyframeSpreadsheetPanel
from .operators.start import RemoveKeyframeOperator

def register():
    # Registration for LichtFeld Studio v0.5+
    lichtfeld.registry.register_class(KeyframeSpreadsheetPanel)
    lichtfeld.registry.register_class(RemoveKeyframeOperator)
    lichtfeld.log.info("Timeline Spreadsheet Plugin Loaded Successfully")
