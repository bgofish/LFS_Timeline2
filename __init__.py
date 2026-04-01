# SPDX-License-Identifier: GPL-3.0-or-later
import lfs
from .panels.training_render import KeyframeSpreadsheetPanel
from .operators.start import RemoveKeyframeOperator, AddKeyframeOperator

def register():
    lfs.registry.register_class(KeyframeSpreadsheetPanel)
    lfs.registry.register_class(RemoveKeyframeOperator)
    lfs.registry.register_class(AddKeyframeOperator)
    lfs.log.info("Timeline Spreadsheet Plugin Loaded")
