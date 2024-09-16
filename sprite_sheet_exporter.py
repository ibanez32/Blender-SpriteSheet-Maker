import bpy
import math
import os

bl_info = {
    "name": "Sprite Sheet Exporter",
    "blender": (3, 0, 0),
    "category": "Render",
    "description": "Export the current scene as a sprite sheet with customizable tile dimensions."
}

class SpriteSheetExporterProperties(bpy.types.PropertyGroup):
    tile_width: bpy.props.IntProperty(
        name="Tile Width",
        description="Width of each tile in pixels",
        default=64,
        min=1
    )
    
    tile_height: bpy.props.IntProperty(
        name="Tile Height",
        description="Height of each tile in pixels",
        default=64,
        min=1
    )
    
    num_tiles: bpy.props.IntProperty(
        name="Number of Tiles",
        description="Total number of tiles",
        default=16,
        min=1
    )
    
    output_filepath: bpy.props.StringProperty(
        name="Output Filepath",
        description="Filepath to save the sprite sheet",
        default="//sprite_sheet.png",
        subtype='FILE_PATH'
    )


class RENDER_PT_SpriteSheetExporter(bpy.types.Panel):
    bl_label = "Sprite Sheet Exporter"
    bl_idname = "RENDER_PT_sprite_sheet_exporter"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        exporter_props = scene.sprite_sheet_exporter
        
        layout.prop(exporter_props, "tile_width")
        layout.prop(exporter_props, "tile_height")
        layout.prop(exporter_props, "num_tiles")
        layout.prop(exporter_props, "output_filepath")
        layout.operator("render.export_sprite_sheet", text="Export Sprite Sheet")


class RENDER_OT_ExportSpriteSheet(bpy.types.Operator):
    bl_idname = "render.export_sprite_sheet"
    bl_label = "Export Sprite Sheet"
    
    def execute(self, context):
        scene = context.scene
        exporter_props = scene.sprite_sheet_exporter
        
        # Grab the properties
        tile_width = exporter_props.tile_width
        tile_height = exporter_props.tile_height
        num_tiles = exporter_props.num_tiles
        output_filepath = bpy.path.abspath(exporter_props.output_filepath)
        
        # Set render resolution
        rows = math.ceil(math.sqrt(num_tiles))
        cols = rows
        
        sprite_sheet_width = cols * tile_width
        sprite_sheet_height = rows * tile_height
        
        # Render settings
        bpy.context.scene.render.resolution_x = tile_width
        bpy.context.scene.render.resolution_y = tile_height
        
        # Create a blank image for the sprite sheet
        sprite_sheet = bpy.data.images.new("Sprite Sheet", width=sprite_sheet_width, height=sprite_sheet_height)
        pixels = [0] * (sprite_sheet_width * sprite_sheet_height * 4)
        
        tile_count = 0
        
        # Render each frame as a tile and place it into the sprite sheet
        for row in range(rows):
            for col in range(cols):
                if tile_count >= num_tiles:
                    break
                
                # Render current frame
                bpy.context.scene.frame_set(tile_count + 1)
                bpy.ops.render.render(write_still=True)
                
                # Get rendered image
                rendered_image = bpy.data.images['Render Result']
                rendered_pixels = list(rendered_image.pixels)
                
                # Place it into the sprite sheet pixels array
                for y in range(tile_height):
                    for x in range(tile_width):
                        idx = ((sprite_sheet_height - (row * tile_height + y) - 1) * sprite_sheet_width + (col * tile_width + x)) * 4
                        rendered_idx = (y * tile_width + x) * 4
                        pixels[idx:idx + 4] = rendered_pixels[rendered_idx:rendered_idx + 4]
                
                tile_count += 1
        
        sprite_sheet.pixels = pixels
        sprite_sheet.filepath_raw = output_filepath
        sprite_sheet.file_format = 'PNG'
        sprite_sheet.save()
        
        self.report({'INFO'}, f"Sprite sheet exported to {output_filepath}")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SpriteSheetExporterProperties)
    bpy.utils.register_class(RENDER_PT_SpriteSheetExporter)
    bpy.utils.register_class(RENDER_OT_ExportSpriteSheet)
    bpy.types.Scene.sprite_sheet_exporter = bpy.props.PointerProperty(type=SpriteSheetExporterProperties)


def unregister():
    bpy.utils.unregister_class(SpriteSheetExporterProperties)
    bpy.utils.unregister_class(RENDER_PT_SpriteSheetExporter)
    bpy.utils.unregister_class(RENDER_OT_ExportSpriteSheet)
    del bpy.types.Scene.sprite_sheet_exporter


if __name__ == "__main__":
    register()
