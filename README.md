1. Use [**QuickBMS**](https://github.com/LittleBigBug/QuickBMS/releases) to extract the ipks from a game disc iso.
	- In this instace, I extracted "sw01.ipk" from the iso of the first Blue Dragon disc, which is only about 3.33 MB.

1. Set up a folder with the following structure
    - **`/IPKUnpacker_BD/`**  *(Folder name doesn't matter)*
    - */IPKUnpacker_BD/* **`IPKUnpacker_BD.exe`**
    - */IPKUnpacker_BD/* **`out/`** *(MUST be "out")*
    - */IPKUnpacker_BD/* **`input/`**  *(MUST be "input")*
    - */IPKUnpacker_BD/input/* **`sw01.ipk`** (And any other ipk files)

1. Run `IPKUnpacker_BD.exe`, which you should have put in `/IPKUnpacker_BD/`
	- The script will create **`out.log`** and place the extracted files in the **`out`** folder
    - A model unpacked with `IPKUnpacker_BD` can only be properly imported into Blender 2.49, I don't know why
1. The .dds textures must be unswizzled with [**Noesis**](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91) and the provided **`tex_dds_offset0x800.py`** plugin, so place **`tex_dds_offset0x800.py`** in **`/plugins/python`** in the directory for your version of Noesis.
	- The original `tex_dds.py` has `dataOffset = 0x180`, but it's vital to use `dataOffset = 0x800` to unswizzle Blue Dragon textures.
    - I have no memory of where I got the plugin from, and I can't find the source now. 😓
1. Use Noesis with the provided plugin to extract the textures.
	- The textures should be unswizzled at this point.
1. In Blender 2.49, import the models and unswizzled textures.
2. If you wish, save the blend file and open it in a newer version of Blender.
	- The models will likely still be arranged very awkwardly and will require some meticulous manual untangling in Blender.
 	- You will _also_ need to fix _every single bone_ in the model.
 	- When I did this, I made sure all my rotations were tied to the three axes and snapped to certain values to keep things consistent.
