try:
    import studio
except:
    import lfs_studio as studio

class StartEditorOperator(studio.Operator):
    bl_idname = "lichtfeld.start_editor"
    bl_label = "Start Spreadsheet Editor"

    def execute(self, context):
        print("Editor Started")
        return {'FINISHED'}
