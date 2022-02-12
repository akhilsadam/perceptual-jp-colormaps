#!/usr/bin/env python3
# inspired / based on https://stackoverflow.com/questions/61487041/more-perceptually-uniform-colormaps
import matplotlib
from sympy import true
matplotlib.use('agg')
from matplotlib import pyplot as plt
import logging
import colour
import numpy as np
import json as js
from scipy.interpolate import CubicSpline,interp1d
from pynverse import inversefunc
from savitzky_golay import savitzky_golay
import maps
import readme

prefix = "jp-cm-"
defaultdatafile = f'{maps.path}cmaps.txt'
discretization = 40

baseColorSpace = "sRGB"
colorModel = 'CAM16UCS' # ['CAM16UCS','Jzazbz',...] # 
outputColorModel = 'sRGB'

# spline_type= 'cubic' # ['custom','cubic']
spline_mode = 'natural' # ['natural','clamped','not-a-knot'] (in best-to-worst order)

n_iterations = 1 # number of adjustments # note >1 values cause divergence!

logging.basicConfig(filename=f'{maps.path}log.txt')
logging.getLogger('matplotlib.font_manager').disabled = True
logger = logging.getLogger(__name__)
# logger.level=logging.DEBUG

def linear_segmented_spline(x):
    """
    Creates segmented linear spline between color points.
    """
    n_gradients = len(x) - 1
    RGB_list = []
    for i in range(n_gradients):
        gradient = colour.utilities.lerp(
            x[i][np.newaxis],
            x[i+1][np.newaxis],
            np.linspace(0, 1, discretization)[..., np.newaxis])
        RGB_list.append(gradient)
    return np.vstack(RGB_list)

def smooth_spline(x):
    """
    Creates a cubic spline between color points,
    then adjusts to get a (mostly) perceptually uniform colormap.
    """
    n_keypoints = len(x)
    n_points = (n_keypoints-1)*discretization
    naive_xs = np.linspace(0,n_keypoints-1,n_points)

    spline = CubicSpline(list(range(n_keypoints)), x, bc_type=spline_mode)
    naive = spline(naive_xs)

    adjusted = naive
    adjusted_xs = naive_xs
    for _ in range(n_iterations):
        adjusted_xs = adjust_spline(adjusted, adjusted_xs, n_keypoints)
        adjusted = spline(adjusted_xs)

    # return np.array(
    # [savitzky_golay(adjusted.T[0], 40, 5),
    # savitzky_golay(adjusted.T[1], 40, 5),
    # savitzky_golay(adjusted.T[2], 40, 5)]).T

    return adjusted

def adjust_spline(naive,naive_xs, n_keypoints):
    """
    Adjust spline speed along curve to force perceptual derivative to zero.
    """
    _,local_derivs = fitD(naive)
    difficulty = np.cumsum(local_derivs)
    stepDiff = difficulty[len(difficulty)-1] / (n_keypoints-1)
    diffFunction = interp1d(naive_xs[1:], difficulty,fill_value="extrapolate")
    return inversefunc(diffFunction,y_values = naive_xs * stepDiff)

def delta_ymax(values):
    return max(np.max(values)*1.1, 0)

def fitD(gradient):
    """
    (Lifted from https://github.com/1313e/viscm/blob/master/viscm/gui.py)
    """
    local_deltas = np.sqrt(np.sum(np.diff(gradient, axis=0)**2, axis=-1))
    local_derivs = (len(local_deltas)-1)*local_deltas
    return local_deltas,local_derivs

def calculatePD(gradient, RGB, name):
    """
    Calculate and plot colormap with perceptual derivative.
    """
    n_keys = int(len(gradient)/discretization)

    fig,_ = colour.plotting.plot_multi_colour_swatches(
        [colour.plotting.ColourSwatch(RGB=np.clip(x, 0, 1)) for x in RGB], height = 2*n_keys)
    
    ax = fig.add_subplot(212)

    local_deltas,local_derivs = fitD(gradient)

    ax.plot(local_derivs,c=maps.ginshu)
    arclength = np.sum(local_deltas)
    rmse = np.std(local_derivs)
    ax.text(0.1,0.4,"Perceptual Derivative for Colormap : {}".format(name),transform=ax.transAxes)
    ax.text(0.1,0.1,"Length: %0.1f\nRMS deviation from flat: %0.1f (%0.1f%%)"
            % (arclength, rmse, 100*rmse / arclength),transform=ax.transAxes)
    # print("Perceptual derivative: %0.5f +/- %0.5f" % (arclength, rmse))
    ax.set_ylim(0, delta_ymax(local_derivs))
    ax.get_xaxis().set_visible(False)
    ax.margins(0.0)
    ax.set_facecolor(maps.aijiro_alpha)
    ax.set_aspect(n_keys*8/delta_ymax(local_derivs))
    fig.patch.set_facecolor(maps.transparent)
    return fig

def gen_cmaps(cmaps,memory_only = True):
    """
    Create colormaps and save individual image as png, and all maps to txt.
    args:   map (dict) : colormap dictionary, memory_only (bool) : save flag for colormap details
    out:    ../maps/maps.txt
            ../maps/<name>.png
    """
    

    mapdata = {}

    for i in range(2):
        segmented = (i==0)
        options = maps.segmentOPT if segmented else ""

        for key in cmaps.keys():

            name = prefix+key+options

            x = colour.convert(cmaps[key], 'Output-Referred RGB', colorModel)
            gradient = linear_segmented_spline(x) if segmented else smooth_spline(np.array(x))
            RGB = colour.convert(gradient, colorModel, outputColorModel)

            logger.debug("Perceptual:{}".format(x))
            logger.debug("RGB:{}".format(RGB))

            if not memory_only: calculatePD(gradient, RGB, name).savefig(maps.path+key+options+".png",bbox_inches='tight')

            mapdata[name] = RGB.tolist()
       

    return mapdata

def save(mapdata,datafile=defaultdatafile):
    with open(datafile, 'w') as file:
        file.write(js.dumps(mapdata))

def core():
    save(gen_cmaps(maps.cmaps, memory_only = False))
    readme.generate()
    # gen_cmaps(cmaps,("--segmented" in sys.argv))

if __name__=='__main__':
    core()
