#!/usr/bin/env python3

"""
jpcm | perceptual-jp-colormaps  
  
A perceptually uniform colormap generator for Matplotlib equipped with traditional-ish Japanese colors to serve as a fixed color palette.
"""
from matplotlib.colors import ListedColormap as LCM
import jpcm.core.core as core
import jpcm.core.utils as ul
import jpcm.load.load as load
import jpcm.core.maps as maps

def register(custom_maps=None,datafile=None):
    """
    registers default and custom colormaps (if given), and saves to datafile (is given)
    args: custom_maps (dict) : colormap dictionary of keycolors, datafile (str) : file path to save at 
    """
    cmaps = {}
    cmaps.update(maps.cmaps)
    if custom_maps is not None: cmaps.update(custom_maps)
    mapdata = core.gen_cmaps(cmaps, memory_only = True)
    load.jpcm_register(mapdata)
    if datafile is not None: core.save(mapdata,datafile)

def open(datafile = f'{maps.path}cmaps.txt'):
    """
    registers colormaps given by datafile
    args: datafile (str) : file path containing colormap data
    """
    load.jpcm_register(load.jpcm_load(datafile))

#mainly for MATPLOTLIB 3.3/3.4
def get(key,segmented = False,cmaps=maps.cmaps):
    RGB,_ = core.get(key,segmented = False,cmaps=maps.cmaps)
    return LCM(RGB.tolist())