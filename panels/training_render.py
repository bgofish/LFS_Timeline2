# No top-level 'lfs' import needed here
def setup_data_binding(context):
    pass

class KeyframeSpreadsheetPanel:
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    panel_path = "training_render.rml" # Ensure this file exists in the folder
