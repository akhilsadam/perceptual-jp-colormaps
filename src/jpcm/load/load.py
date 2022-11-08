import matplotlib
from matplotlib.colors import ListedColormap as LCM
import matplotlib as mpl
import numpy as np
import json as js

rev = "_rev"

def jpcm_load(datafile):

    with open(datafile,'r') as file:
        mapdata = js.load(file)

    return {key: (np.array(mapdata[key]),key) for key in mapdata.keys()}

def jpcm_register(jpcm_cmaps):
    for key in jpcm_cmaps.keys():
        if key not in matplotlib.pyplot.colormaps():
            mpl.colormaps.register(LCM(jpcm_cmaps[key]),name = key)
            mpl.colormaps.register(np.flip(LCM(jpcm_cmaps[key])),name = key+rev)


