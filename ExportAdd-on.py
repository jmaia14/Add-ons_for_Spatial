bl_info = {
    "name": "Export Scene Objects to Spatial",
    "author": "Julio Maia",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolshelf",
    "description": "Export the Objects in the Scene to an extension to be imported into Spatial.",
    "warning": "",
    "doc_url": "",
    "category": "Export Scene",
}


import bpy
from bpy.types import Panel, Operator

class EXPORT_PT_MainPanel(Panel):
    bl_label = "Export Scene/Object"
    bl_idname = "EXPORT_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Export"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("export.obj", icon='EXPORT')
        row = layout.row()
        row.operator("export.gltf", icon='EXPORT')
        row = layout.row()
        row.operator("export.fbx", icon='EXPORT')


class EXPORT_OT_OBJ(Operator):
    bl_label = "Export .obj(max.100mb)"
    bl_idname = "export.obj"
    
    def execute(self, context):
        bpy.ops.export_scene.obj('INVOKE_DEFAULT')    
        return {'FINISHED'}

class EXPORT_OT_GLTF(Operator):
    bl_label = "Export .gltf/glb(max.100mb)"
    bl_idname = "export.gltf"
    
    def execute(self, context):
        bpy.ops.export_scene.gltf('INVOKE_DEFAULT')    
        return {'FINISHED'}

class EXPORT_OT_FBX(Operator):
    bl_label = "Export .fbx(max.100mb)"
    bl_idname = "export.fbx"
    
    def execute(self, context):
        bpy.ops.export_scene.fbx('INVOKE_DEFAULT')    
        return {'FINISHED'}
  

classes = [EXPORT_PT_MainPanel, EXPORT_OT_OBJ, EXPORT_OT_GLTF, EXPORT_OT_FBX]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
