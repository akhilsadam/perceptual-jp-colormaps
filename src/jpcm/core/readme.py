from jpcm.core.maps import *
readmefile = "/../../../../README.md"
uname='akhilsadam'
rname='perceptual-jp-colormaps'
branch='master'
readme = """
# perceptual-jp-colormaps  
  
A perceptually uniform colormap generator for Matplotlib equipped with traditional-ish Japanese colors to serve as a fixed color palette.   
(Culture appropriation at its finest.) Additions are welcomed.  

Why perceptually uniform colormaps? Can you not just use default Matplotlib colormaps?   
- non-perceptually uniform colormaps induce dangerous artifacts, as seen in the below image: ![top-view of pyramid](https://i.stack.imgur.com/JcTDb.png).
The left colormap introduces new features to the data.
- Matplotlib perceptually uniform colormaps are not visually appealing and sometimes lack enough contrast.
With this package, anyone can design colormaps to fit their visual style.

dependencies:  
- Python3:  
--	colour-science  
--	numpy  
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
"""

def generate():
    lines = []
    for key in cmaps.keys():
        names = [path1+key+suffix,path1+key+segmentOPT+suffix]
        imagenames = [f"https://github.com/{uname}/{rname}/blob/{branch}/{name}?raw=true" for name in names]

        line = "\n![](" + f"{imagenames[0]}" + ") ![](" + f"{imagenames[1]}" + ")"
        lines.append(line)
    readmeHT = readme + "  ".join(lines)
    with open(readmefile, 'w') as file:
        file.write(readmeHT)
