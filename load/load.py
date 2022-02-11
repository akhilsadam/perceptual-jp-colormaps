from matplotlib.colors import ListedColormap as LCM
import numpy as np
import json as js

datafile = "../cmaps.txt"

with open(datafile,'r') as file:
    mapdata = js.load(file)

cmaps = {key: LCM(np.array(mapdata[key]),key) for key in mapdata.keys()}

print(cmaps)