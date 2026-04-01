def setup_spreadsheet_data(context):
    pass

class KeyframeSpreadsheetPanel:
    # This ID must be unique
    id = "TIMELINE_PT_spreadsheet_v3" 
    label = "Spreadsheet"
    
    # Standard v0.5 Sidebar Categories: "SCENE", "TOOLS", or "VIEW"
    category = "SCENE" 
    # This flag tells the UI engine to force a sidebar tab
    type = "SIDEBAR" 
    
    # Path MUST be relative to the plugin root
    panel_path = "panels/training_render.rml" 

    def draw(self, context):
        # Even if empty, this method must exist
        pass
