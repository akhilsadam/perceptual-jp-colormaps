# inspired / based on https://stackoverflow.com/questions/61487041/more-perceptually-uniform-colormaps

import matplotlib
matplotlib.use('agg')
import logging
import colour
import numpy as np
import json as js
import sys
from scipy.interpolate import CubicSpline
from maps import cmaps

path = "../maps/"
datafile = "../cmaps.txt"
discretization = 20

logging.basicConfig(filename=f'{path}log.txt')
logging.getLogger('matplotlib.font_manager').disabled = True
logger = logging.getLogger(__name__)
logger.level=logging.DEBUG

def linear_segmented_spline(CAM16UCS):
    """
    Creates segmented linear spline between color points.
    """
    n_gradients = len(CAM16UCS) - 1
    RGB_list = []
    for i in range(n_gradients):
        logger.debug("CAMAXIS:{}".format(CAM16UCS[i][np.newaxis]))
        gradient = colour.utilities.lerp(
            CAM16UCS[i][np.newaxis],
            CAM16UCS[i+1][np.newaxis],
            np.linspace(0, 1, discretization)[..., np.newaxis])
        RGB_list.append(colour.convert(gradient, 'CAM16UCS', 'Output-Referred RGB'))
    return np.vstack(RGB_list)

def smooth_spline(CAM16UCS):
    """
    Creates a cubic spline between color points.
    """
    n_points = len(CAM16UCS)
    spline = CubicSpline(list(range(n_points)), CAM16UCS) #, bc_type='natural')
    gradient = spline(np.linspace(0,n_points,(n_points-1)*discretization))
    return colour.convert(gradient, 'CAM16UCS', 'Output-Referred RGB')

def gen_cmaps(cmaps,segmented=False):
    """
    Create colormaps and save individual image as png, and all maps to txt.
    args:   map (dict), segmented (bool) : colormap style
    out:    ../maps/maps.txt
            ../maps/<name>.png
    """

    options = "_segmented" if segmented else ""
    mapdata = {}

    for key in cmaps.keys():
        CAM16UCS = colour.convert(cmaps[key], 'sRGB', 'CAM16UCS')

        logger.debug("CAM16UCS:{}".format(CAM16UCS))

        if segmented:
            RGB = linear_segmented_spline(CAM16UCS)
        else:
            RGB = smooth_spline(np.array(CAM16UCS))

        logger.debug("RGB:{}".format(RGB))

        fig,_ = colour.plotting.plot_multi_colour_swatches(
            [colour.plotting.ColourSwatch(RGB=np.clip(x, 0, 1)) for x in RGB])

        fig.savefig(path+key+options+".png")

        mapdata[key] = RGB.tolist()
        # print(key,colour.convert(RGB, 'Output-Referred RGB', 'Hexadecimal'))

    with open(datafile, 'w') as file:
        file.write(js.dumps(mapdata))

def core():
    gen_cmaps(cmaps,("--segmented" in sys.argv))

if __name__=='__main__':
    core()
