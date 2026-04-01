import lichtfeld

class RemoveKeyframeOperator(lichtfeld.types.Operator):
    id = "timeline.remove_keyframe"
    label = "Remove Keyframe"
    
    def execute(self, index=None):
        if index is not None:
            # Access the scene timeline through the lichtfeld context
            lichtfeld.context.scene.timeline.remove(index)
            lichtfeld.log.info(f"Removed keyframe {index}")
        return True
