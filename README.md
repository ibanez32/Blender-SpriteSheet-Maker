# Sprite Sheet Exporter for Blender

A Blender add-on to export animations as a sprite sheet with customizable tile dimensions. You can configure the tile width, height, and number of tiles in the sprite sheet and then export the result as a single image.

## Features

- Customizable tile width and height for each sprite in the sheet.
- Define the total number of tiles to be exported.
- Exports the animation frames into a neatly organized sprite sheet.
- Saves the sprite sheet as a PNG file with the specified configuration.

## Installation

1. **Download the Add-on**:
   - Save the `sprite_sheet_exporter.py` file to your computer.

2. **Install the Add-on**:
   - Open Blender.
   - Go to `Edit > Preferences > Add-ons`.
   - Click the `Install` button and select the `sprite_sheet_exporter.py` file.
   - Enable the add-on by checking the checkbox next to "Sprite Sheet Exporter".

3. **Save User Preferences** (optional):
   - To have the add-on enabled every time you open Blender, click `Save Preferences` at the bottom of the Preferences window.

## How to Use

1. **Set up your Scene**:
   - Make sure you have an animation ready for rendering in Blender.

2. **Configure Sprite Sheet Properties**:
   - Go to the `Render Properties` tab.
   - In the "Sprite Sheet Exporter" panel, specify the following:
     - **Tile Width**: Width of each tile in pixels.
     - **Tile Height**: Height of each tile in pixels.
     - **Number of Tiles**: The total number of frames to be exported into the sprite sheet.
     - **Output Filepath**: Where you want to save the exported sprite sheet (e.g., `//sprite_sheet.png`).

3. **Export the Sprite Sheet**:
   - Click the `Export Sprite Sheet` button.
   - The script will render each frame and generate a sprite sheet based on your configuration.
   - The sprite sheet will be saved as a PNG file in the specified location.

## Example

Let's say you have an animation with 16 frames and you want to export it as a sprite sheet where each tile is 64x64 pixels. Set the following in the Sprite Sheet Exporter panel:

- **Tile Width**: 64
- **Tile Height**: 64
- **Number of Tiles**: 16
- **Output Filepath**: `//my_sprite_sheet.png`

When you click `Export Sprite Sheet`, the add-on will render the animation and generate a 4x4 sprite sheet.

## Requirements

- Blender 3.0 or later.

## License

This project is licensed under the Creative Commons Zero v1.0 Universal. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.

## Support

If you encounter any issues or have any questions, feel free to open an issue on the [GitHub repository](https://github.com/ibanez32/Blender-SpriteSheet-Maker).

