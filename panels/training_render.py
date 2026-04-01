def setup_spreadsheet_data(context):
    pass

class KeyframeSpreadsheetPanel:
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    # Try SCENE in all caps, as many LFS versions use this internally
    category = "SCENE" 
    # Fallback for alternative UI engines
    bl_category = "SCENE"
    # Ensure this points to the right file
    panel_path = "training_render.rml" 

    def draw(self, context):
        pass
