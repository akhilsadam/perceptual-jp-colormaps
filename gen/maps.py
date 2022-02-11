import numpy as np

def rgb(r,g,b):
    return np.array([r,g,b])/255

# list of colors from js
aijiro = rgb(235, 246, 247)
sukaitsuri_iro = rgb(220, 240, 250)
# skytree white not accurate
mashiro = rgb(255, 255, 255)
zoge_iro = rgb(255, 255, 240)
hakushi = rgb(249, 251, 255)
mizu_iro = rgb(134, 171, 165)
gunjo_iro = rgb(93, 140, 174)
sora_iro = rgb(77, 143, 172)
chigusa_iro = rgb(49, 117, 137)
benimidori = rgb(120, 119, 155)
rurikon = rgb(27, 41, 75)
omeshi_onando = rgb(61, 76, 81)
tetsuonando = rgb(43, 55, 54)
sakuranezumi = rgb(172, 129, 118)
ginshu = rgb(188, 45, 41)
azuki_iro = rgb(103, 36, 34)
# list of colormaps
cmaps = \
{
    'def' : [rurikon,chigusa_iro,ginshu]
}