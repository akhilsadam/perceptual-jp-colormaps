#!/usr/bin/env python3

"""
jpcm | perceptual-jp-colormaps  
  
A perceptually uniform colormap generator for Matplotlib equipped with traditional-ish Japanese colors to serve as a fixed color palette.
"""

import core,load,core.maps

def register(custom_maps=None,datafile=None):
    """
    registers default and custom colormaps (if given), and saves to datafile (is given)
    args: custom_maps (dict) : colormap dictionary of keycolors, datafile (str) : file path to save at 
    """
    cmaps = {}
    cmaps.append(core.maps.cmaps)
    if datafile is not None: cmaps.append(custom_maps)
    mapdata = core.core.gen_cmaps(cmaps, memory_only = True)
    load.jpcm_register(mapdata)
    if datafile is not None: core.core.save(mapdata,datafile)

def load(datafile = f'{core.maps.path}cmaps.txt'):
    """
    registers colormaps given by datafile
    args: datafile (str) : file path containing colormap data
    """
    load.jpcm_register(load.jpcm_load(datafile))