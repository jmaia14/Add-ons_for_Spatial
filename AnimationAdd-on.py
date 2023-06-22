bl_info = {
    "name": "Rotation Animation Add-on",
    "author": "Julio Maia",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolshelf",
    "description": "Adds a Rotation to the Mesh Object in the X, Y and Z axis",
    "warning": "",
    "doc_url": "",
    "category": "Aniamtion",
}

import math
import bpy
from bpy.types import PropertyGroup, Panel, Operator

class ANIMATION_Properties(PropertyGroup):
    
    x_axis: bpy.props.BoolProperty(name="X Axis", default=False)
    neg_x_axis: bpy.props.BoolProperty(name="X Axis", default=False)
    y_axis: bpy.props.BoolProperty(name="Y Axis", default=False)
    z_axis: bpy.props.BoolProperty(name="Z Axis", default=False)
    speed: bpy.props.IntProperty(name="Speed", default=100)

class ANIMATION_PT_Panel(Panel):
    bl_label = "Rotation"
    bl_idname = "ANIMATION_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animation"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        layout.prop(mytool, "x_axis")
        layout.prop(mytool, "y_axis")
        layout.prop(mytool, "z_axis")
        layout.prop(mytool, "speed")
        
        row = layout.row()
        row.operator("key.add_rotation", icon="CON_ROTLIKE")

class ANIMATION_OT_Operator(Operator):
    bl_label = "Rotation"
    bl_idname = "key.add_rotation"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        s = mytool.speed
        
        obj = context.active_object
        obj.name = 'Active'
        
        if mytool.x_axis == True:
            bpy.data.objects['Active'].keyframe_insert(data_path="rotation_euler", frame=1)
            bpy.ops.transform.rotate(value=math.pi, orient_axis='X')
            bpy.data.objects['Active'].keyframe_insert(data_path="rotation_euler", frame=s)
         
        if mytool.y_axis == True:
            bpy.data.objects['Active'].keyframe_insert(data_path="rotation_euler", frame=1)
            bpy.ops.transform.rotate(value=math.pi, orient_axis='Y')
            bpy.data.objects['Active'].keyframe_insert(data_path="rotation_euler", frame=s)
                     
        if mytool.z_axis == True:
            bpy.data.objects['Active'].keyframe_insert(data_path="rotation_euler", frame=1)
            bpy.ops.transform.rotate(value=math.pi, orient_axis='Z')
            bpy.data.objects['Active'].keyframe_insert(data_path="rotation_euler", frame=s)
        
        return {'FINISHED'}
    


classes = [ANIMATION_Properties, ANIMATION_PT_Panel, ANIMATION_OT_Operator]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= ANIMATION_Properties)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool
        
if __name__ == "__main__":
    register()
