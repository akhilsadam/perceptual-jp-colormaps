from maps import *
readmefile = "../README.md"
readme = """
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
"""

def generate():
    lines = []
    for key in cmaps.keys():
        imagename = [path0+key+suffix,path0+key+segmentOPT+suffix]
        line = "\n![]("+"{}".format(imagename[0])+" | width=100) ![]("+"{}".format(imagename[1])+" | width=100)"
        lines.append(line)
    readmeHT = readme + "  ".join(lines)  
    with open(readmefile, 'w') as file:
        file.write(readmeHT)
