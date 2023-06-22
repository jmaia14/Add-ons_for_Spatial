bl_info = {
    "name": "HotSpot Creator",
    "author": "Julio Maia",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolshelf",
    "description": "Adds a HotSpot to your object, it has a panel that you can access by pressing 'N' in the View3D.",
    "warning": "",
    "doc_url": "",
    "category": "Add HotSpot",
}

import bpy

from bpy.types import Panel, Operator, PropertyGroup

class HOTSPOT_Properties(PropertyGroup):
    
    float_loc: bpy.props.FloatVectorProperty(name="Local", default= (0,0,0))

class HOTSPOT_PT_Panel(Panel):
    bl_label = "Hotspot Panel"
    bl_idname = "HOTSPOT_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Hotspot"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool=scene.my_tool
        
        layout.prop(mytool, "float_loc")

        row = layout.row()
        row.operator("wm.hotspot_operator", icon='OBJECT_ORIGIN')

class HOTSPOT_OT_Operator(Operator):
    bl_label = "Add HotSpot"
    bl_idname = "wm.hotspot_operator"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        list = []
        
        bpy.ops.object.empty_add(type='SPHERE', align='WORLD',location=(0, 0, 0), scale=(1, 1, 1))  
        bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))     
        bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))
        bpy.data.objects["Empty"].name = "chair -hotspot"
        bpy.data.objects["Empty.001"].name = "RootNode"
        bpy.data.objects["Empty.002"].name = "3DSMeshMatrix"
        objects = bpy.data.objects
        cube1 = objects['RootNode']
        cube2 = objects['3DSMeshMatrix']
        sphere = objects['chair -hotspot']
        cube2.parent = cube1
        sphere.parent = cube2

        list.append(cube1)
        list.append(cube2)
        list.append(sphere)
           
        for el in list:
            el = bpy.context.object.location[0] = mytool.float_loc[0]    
            el = bpy.context.object.location[1] = mytool.float_loc[1]
            el = bpy.context.object.location[2] = mytool.float_loc[2]
           
        return {'FINISHED'}
    
classes = [HOTSPOT_Properties, HOTSPOT_PT_Panel, HOTSPOT_OT_Operator]    

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= HOTSPOT_Properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
