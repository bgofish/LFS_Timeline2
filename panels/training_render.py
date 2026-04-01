def setup_data_binding(context):
    # This will be used to sync your spreadsheet data
    pass

class KeyframeSpreadsheetPanel:
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    # Ensure training_render.rml is in the same folder as this file
    panel_path = "training_render.rml" 

    def draw(self, context):
        # UI logic is handled by the RML file
        pass
