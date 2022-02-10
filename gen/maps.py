# inspired / based on https://stackoverflow.com/questions/61487041/more-perceptually-uniform-colormaps

import colour
import numpy as np

CAM16UCS = colour.convert(['#ff0000', '#00ff00'], 'Hexadecimal', 'CAM16UCS')
gradient = colour.utilities.lerp(
    CAM16UCS[0][np.newaxis],
    CAM16UCS[1][np.newaxis],
    np.linspace(0, 1, 20)[..., np.newaxis])
RGB = colour.convert(gradient, 'CAM16UCS', 'Output-Referred RGB')

colour.plotting.plot_multi_colour_swatches(
    [colour.plotting.ColourSwatch(RGB=np.clip(x, 0, 1)) for x in RGB])

print(colour.convert(RGB, 'Output-Referred RGB', 'Hexadecimal'))