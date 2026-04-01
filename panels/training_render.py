def setup_data_binding(context):
    # This must exist to satisfy the import in __init__.py
    pass

class KeyframeSpreadsheetPanel:
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    category = "LichtFeld" 
    panel_path = "training_render.rml" 

    def draw(self, context):
        pass
