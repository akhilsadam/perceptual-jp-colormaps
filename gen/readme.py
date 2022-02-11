from maps import *
readmefile = "../README.md"
uname='akhilsadam'
rname='perceptual-jp-colormaps'
branch='master'
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
    `python3 gen.py` or `python3 gen.py --readme`

load colormaps:
    add load.py and the maps/cmaps.txt to your code.
    load.jpcm_load() will return a dictonary containing all the colormaps

## gallery  
"""

def generate():
    lines = []
    for key in cmaps.keys():
        names = ["/"+path0+key+suffix,"/"+path0+key+segmentOPT+suffix]
        imagenames = ["https://github.com/{}/{}/blob/{}/{}?raw=true".format(uname,rname,branch,name) for name in names]
        line = "\n![]("+"{}".format(imagenames[0])+")  \n![]("+"{}".format(imagenames[1])+")"
        lines.append(line)
    readmeHT = readme + "  ".join(lines)  
    with open(readmefile, 'w') as file:
        file.write(readmeHT)