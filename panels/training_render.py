def setup_spreadsheet_data(context):
    pass

class KeyframeSpreadsheetPanel:
    # Unique ID for the panel
    id = "TIMELINE_PT_spreadsheet"
    # The text that appears on the tab itself
    label = "Spreadsheet"
    # Try these identifiers which are standard for the LFS sidebar
    category = "LichtFeld" 
    # v0.5 internal UI tag
    type = "SIDEBAR" 
    
    # Path to your UI file (must be in the same folder as this .py file)
    panel_path = "training_render.rml" 

    def draw(self, context):
        """Standard draw call, logic is in the RML."""
        pass
