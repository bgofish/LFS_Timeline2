# No imports needed here
def setup_data_binding(context):
    """Provides the data for the RML spreadsheet."""
    # This creates the 'keyframes' list used in the RML file
    context.registry.register_property("keyframes", [])

class KeyframeSpreadsheetPanel:
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    category = "LichtFeld" # This puts it in the sidebar
    panel_path = "training_render.rml" 

    def draw(self, context):
        pass
