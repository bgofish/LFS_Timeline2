import lfs

class RemoveKeyframeOperator(lfs.types.Operator):
    id = "timeline.remove_keyframe"
    label = "Remove Keyframe"
    
    def execute(self, index=None):
        if index is not None:
            lfs.context.scene.timeline.remove(index)
            lfs.log.info(f"Removed keyframe at index {index}")
        return True

class AddKeyframeOperator(lfs.types.Operator):
    id = "timeline.add_current_keyframe"
    label = "Add Keyframe"
    
    def execute(self):
        # Logic to capture current camera/scene state as a keyframe
        lfs.context.scene.timeline.add_keyframe(lfs.context.scene.current_frame)
        return True
