import lfs

class KeyframeSpreadsheetPanel(lfs.types.Panel):
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    
    def draw(self):
        layout = self.layout
        # Access the current timeline/camera path
        timeline = lfs.context.scene.timeline 
        
        # Header Row
        row = layout.row(heading=True)
        row.label("Frame", width=50)
        row.label("Position X", width=80)
        row.label("Position Y", width=80)
        row.label("Position Z", width=80)
        row.label("Actions", width=60)
        
        layout.separator()

        # Data Rows (The "Spreadsheet")
        for i, kf in enumerate(timeline.keyframes):
            row = layout.row()
            # editable properties
            row.prop(kf, "frame", text="") 
            row.prop(kf.position, "x", text="")
            row.prop(kf.position, "y", text="")
            row.prop(kf.position, "z", text="")
            
            # Delete button for each row
            row.button("X", operator="timeline.remove_keyframe", args={'index': i})

        layout.separator()
        layout.button("Add New Keyframe", operator="timeline.add_current_keyframe")
