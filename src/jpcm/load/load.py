from matplotlib.colors import ListedColormap as LCM
import matplotlib as mpl
import numpy as np
import json as js

rev = "_rev"

def jpcm_load(datafile):

    with open(datafile,'r') as file:
        mapdata = js.load(file)

    jpcm_cmaps = {key: LCM(np.array(mapdata[key]),key) for key in mapdata.keys()}
    jpcm_cmaps.update({key+rev: LCM(np.flip(np.array(mapdata[key]),axis=0),key+rev) for key in mapdata.keys()})

    return jpcm_cmaps

def jpcm_register(jpcm_cmaps):
    for key in jpcm_cmaps.keys():
        mpl.colormaps.register(jpcm_cmaps[key],name = key)


