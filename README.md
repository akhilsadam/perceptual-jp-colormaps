
# perceptual-jp-colormaps  
  
A perceptually uniform colormap generator for Matplotlib equipped with traditional-ish Japanese colors to serve as a fixed color palette.   
Additions are welcome.  
[![Python package](https://github.com/akhilsadam/perceptual-jp-colormaps/actions/workflows/python-package.yml/badge.svg)](https://github.com/akhilsadam/perceptual-jp-colormaps/actions/workflows/python-package.yml)

Why perceptually uniform colormaps? Can you not just use default Matplotlib colormaps?   
- non-perceptually uniform colormaps induce dangerous artifacts, as seen in the below image: ![top-view of pyramid](https://i.stack.imgur.com/JcTDb.png).
The left colormap introduces new features to the data.
- Matplotlib perceptually uniform colormaps are *simply not visually appealing* and sometimes lack enough contrast.
With this package, anyone can design colormaps to fit their visual style.

dependencies:  
- Python3:  
--	colour-science  
--	numpy==1.23.4  
--	logging  
--	scipy  
--	json  
--	pynverse  
--	matplotlib  
  
tested on:  
- Windows 10  
  
expected to work on:  
- Linux  
- MacOS  
  
install:
- `pip3 install jpcm` or download source

run generator:   
- to create your own colormaps 
   - as a package:  
       - `import jpcm` 
       - `jpcm.register()` will register all default colormaps and any additional ones via the optional `custom_maps` argument. 
        Note any custom_maps should be of the following format (note the RGB key colors):  
            `cmaps = {  
                'def' : [[0,0,0],[255,0,0]],  
            }`  
       - The optional `datafile` argument will cause jpcm to save all colormaps to that location as well.
  - directly via code:
       - edit maps.py with your preferred cmap styles, and run `python3 gen.py` or `python3 gen.py --readme` from `/gen/`

load colormaps:
- `import jpcm`  
- `jpcm.open(<filename>)` will return a dictionary containing all the colormaps in the file at <filename>. 
- Note the file should be of the same type as the generated 'cmap.txt' from the generator


## gallery  

![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/def.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/def_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/fuyu.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/fuyu_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/ice.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/ice_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/iron-ice.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/iron-ice_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/water.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/water_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/momiji.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/momiji_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/sky.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/sky_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/sunburst.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/sunburst_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/flamingo.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/flamingo_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/tree.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/tree_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/ocean.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/ocean_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/desert.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/desert_segmented.png?raw=true)  
![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/fire.png?raw=true) ![](https://github.com/akhilsadam/perceptual-jp-colormaps/blob/master/src/jpcm/maps/fire_segmented.png?raw=true)
