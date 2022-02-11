
# perceptual-jp-colormaps  
  
A collection of perceptually uniform colormaps with traditional-ish Japanese colors. (Culture appropriation at its finest.)  
Additions are welcomed.  

dependencies:  
	Python3:  
		colour-science  
		numpy  
		logging  
		scipy  
		json  
		pynverse  
		matplotlib  
  
tested on:  
	Windows 10  
  
expected to work on:  
	Linux  
	MacOS  
  
run generator:   
    `python3 gen.py`

load colormaps:
    add load.py and the maps/cmaps.txt to your code.
    load.jpcm_load() will return a dictonary containing all the colormaps

## gallery:  

![](maps/def.png | width=100) ![](maps/def_segmented.png | width=100)  
![](maps/sky.png | width=100) ![](maps/sky_segmented.png | width=100)  
![](maps/sunburst.png | width=100) ![](maps/sunburst_segmented.png | width=100)  
![](maps/flamingo.png | width=100) ![](maps/flamingo_segmented.png | width=100)  
![](maps/tree.png | width=100) ![](maps/tree_segmented.png | width=100)