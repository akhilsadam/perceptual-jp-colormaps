import numpy as np

segmentOPT = "_segmented"
path0 = "maps/"
path1 = f'src/jpcm/{path0}'
path = f'../{path0}'
suffix = ".png"


def rgb(r, g, b, a=1):
    arr = np.array([r, g, b])/255
    if a != 1:
        return [arr[0], arr[1], arr[2], a]
    return arr


# list of colors (skytree white not accurate)
transparent = rgb(0, 0, 0, 0)
# whites
aijiro = rgb(235, 246, 247)
aijiro_alpha = rgb(235, 246, 247, 0.15)
sukaitsuri_iro = rgb(220, 240, 250)
mashiro = rgb(255, 255, 255)
zoge_iro = rgb(255, 255, 240)
hakushi = rgb(249, 251, 255)
# blue-greens
mizu_iro = rgb(134, 171, 165)
gunjo_iro = rgb(93, 140, 174)
sora_iro = rgb(77, 143, 172)
chigusa_iro = rgb(49, 117, 137)
benimidori = rgb(120, 119, 155)
kurobeni = rgb(35, 25, 30)
ruri_iro = rgb(58, 36, 59)
rurikon = rgb(27, 41, 75)
konjo_iro = rgb(0, 49, 113)
aoi = rgb(0, 0, 200)
sabi_asagi = rgb(106, 127, 122)
mizu_asagi = rgb(116, 159, 141)
omeshi_onando = rgb(61, 76, 81)
tetsuonando = rgb(43, 55, 54)
mo_egi = rgb(91, 137, 48)
seiji_iro = rgb(129, 156, 139)
# purples
shikon = rgb(43, 32, 40)
kokimurasaki = rgb(58, 36, 59)
kuwazome = rgb(89, 41, 44)
murasaki = rgb(79, 40, 75)
ayame_iro = rgb(118, 53, 104)
# reds
sakuranezumi = rgb(172, 129, 118)
ginshu = rgb(188, 45, 41)
azuki_iro = rgb(103, 36, 34)
akabeni = rgb(195, 39, 43)
shinshu = rgb(143, 29, 33)
karakurenai = rgb(201, 33, 55)
enji_iro = rgb(157, 41, 51)
# browns
benihibata = rgb(111, 48, 40)
# pinks
nakabeni = rgb(201, 55, 86)
# yellows
tomorokoshi_iro = rgb(250, 169, 69)
# greys
haiiro = rgb(91, 90, 92)
# blacks
sumi_iro = rgb(39, 34, 31)
kokushoku = rgb(23, 20, 18)
# list of colormaps

cmaps = \
    {
        'def': [rurikon, chigusa_iro, benimidori, azuki_iro],
        # 'haru' : [],    # warm, bright light : orange, yellow, coral pink, warms
        # 'natsu' : [],   # cool, muted light  : blue-based pink, soft purple, greyed blues, pastels
        # 'aki' : [],     # warm, muted dark   : warm browns, olive/moss greens, teracotta orange, muted reds
        # cool, bright dark  : bright red, dark pink, black, white
        'fuyu': [aijiro, gunjo_iro, mizu_iro, akabeni, murasaki, kokushoku],
        # 'printemps' : [],
        # 'ete' : [],
        # 'automne' : [],
        # 'hiver' : [],
        'ice': [aijiro, gunjo_iro],
        'iron-ice': [sabi_asagi, omeshi_onando],
        'water': [gunjo_iro, mizu_iro, seiji_iro],
        'momiji': [sakuranezumi, ginshu, azuki_iro, enji_iro],
        'sky': [kokushoku, kokimurasaki, sora_iro, aijiro],
        # inspired by cmasher (https://cmasher.readthedocs.io/)
        'sunburst': [kokushoku, enji_iro, akabeni, tomorokoshi_iro, zoge_iro],
        'flamingo': [kokushoku, shinshu, nakabeni, aijiro],
        'tree': [kokushoku, benihibata, mo_egi],
        # nature
        'ocean': [kokushoku, gunjo_iro, omeshi_onando, mizu_asagi],
        'desert': [kokushoku, benihibata, akabeni, tomorokoshi_iro],
        'fire':  [kokushoku, akabeni, sakuranezumi],
    }

vs = vars()
colors = [v for v in vs if v not in ['np', 'segmentOPT', 'path0', 'path1', 'path', 'suffix', 'cmaps', 'rgb'] and v[0] != '_' ]
# print(colors)
solids = [c for c in colors if len(vs[c])==3]
cv = np.array([vs[c] for c in solids]).reshape((len(solids),3))

# print(cv[:5,:])
