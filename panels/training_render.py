class KeyframeSpreadsheetPanel:
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    # Try "Scene" or "Tools" if "LichtFeld" isn't working
    category = "Scene" 
    # Use a direct path relative to the plugin folder
    panel_path = "panels/training_render.rml" 

    def draw(self, context):
        pass
