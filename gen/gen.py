# inspired / based on https://stackoverflow.com/questions/61487041/more-perceptually-uniform-colormaps

import colour
import numpy as np
from maps import colors,cmaps

def gen_cmaps(cmaps):
    """
    Create colormaps and save individual image as png, and all maps to txt.
    args:   map (dict)
    out:    ../maps/maps.txt
            ../maps/<name>.png
    """
    for key in cmaps.keys():
        CAM16UCS = colour.convert(cmaps[key], 'Hexadecimal', 'CAM16UCS')
        gradient = colour.utilities.lerp(
            CAM16UCS[0][np.newaxis],
            CAM16UCS[1][np.newaxis],
            np.linspace(0, 1, 20)[..., np.newaxis])
        RGB = colour.convert(gradient, 'CAM16UCS', 'Output-Referred RGB')

        # colour.plotting.plot_multi_colour_swatches(
        #     [colour.plotting.ColourSwatch(RGB=np.clip(x, 0, 1)) for x in RGB])

        print(key,colour.convert(RGB, 'Output-Referred RGB', 'Hexadecimal'))

def core():
    gen_cmaps(cmaps)

core()
