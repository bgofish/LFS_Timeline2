import lichtfeld

class KeyframeSpreadsheetPanel(lichtfeld.types.Panel):
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    # Point this to the .rml file in your plugin folder
    panel_path = "training_render.rml"

    def draw(self):
        # This draw method can be left empty if you are using 
        # RML for the entire UI layout.
        pass
