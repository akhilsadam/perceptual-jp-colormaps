import jpcm
import numpy as np
import matplotlib
import colour

def to_div(ndiv, rot=0, net_rot=0, sat_factor=1.0, strength=1.0, peak_whiten=1.0, cut=0, invert=False):
  ### Linear Models
  # to REC 706 # need to confirm this is the right space...
  # yc_mat = np.array([[0.2126, 0.7152, 0.0722],
  #                   [-0.1146, -0.3854, 0.5],
  #                   [0.5, -0.4542, -0.0458]])
  # rgb_mat = np.array([[1, 0, 1.5748],
  #                     [1, -0.1873, -0.4681],
  #                     [1, 1.8556, 0]])

  # to REC 2020
  # kr = 0.2627
  # kg = 0.678
  # kb = 0.0593

  # # stupid colormap
  # kr = 1/3
  # kg = 1/3
  # kb = 1/3

  # yc_mat = np.array([[kr, kg, kb],
  #                   [-0.5 * (kr / (1-kb)), -0.5 * (kg / (1-kb)), 0.5],
  #                   [0.5, -0.5 * (kg / (1-kr)), -0.5 * (kb / (1-kr))]])
  
  # rgb_mat = np.array([[1, 0, 2 * (1-kr)],
  #                     [1, -2 * (kb/kg) * (1-kb), -2 * (kr/kg) * (1-kr)],
  #                     [1, 2 * (1-kb), 0]])

  # rgb_mat = np.linalg.inv(yc_mat)

  # nybr = ndiv @ yc_mat.T

  # diff = [nybr[i] - nybr[i-1] for i in range(len(nybr)-1,0,-1)]
  # pybr = np.cumsum([nybr[-1],*diff], axis=0) 
  # pybr[:,0] = np.flip(nybr[:,0])
  # print(nybr,'\n',pybr)

  # pdiv = np.fabs(pybr @ rgb_mat.T)

  ### Nonlinear models

  nhsl = colour.RGB_to_HSL(ndiv)
  # rotate white / black
  sat = nhsl[:,1]
  wh = np.where(sat < 1e-6)
  nhsl[wh,0] = rot % 1

  # adjust all
  nhsl[:,0] = (nhsl[:,0] + net_rot) % 1

  # stretch lighting
  mu = np.mean(nhsl[:,2])
  nhsl[:,2] = np.clip((nhsl[:,2] - mu) * strength  + mu, 0, 1)
  
  # oversaturate
  nhsl[:,1] = np.clip(nhsl[:,1] * sat_factor, 0, 1)

  # peak whiten
  nhsl[-1,2] = np.clip(nhsl[-1,2] * peak_whiten, 0, 1)

  phsl = np.flip(np.copy(nhsl), axis=0) # same lightness and sat.
  diff = [(nhsl[i,0] - nhsl[i-1,0]) for i in range(len(phsl)-1,0,-1)]
  phsl[:,0] = np.cumsum([nhsl[-1,0],*diff], axis=0)
  
  # phsl[:,0] = (0.5 + phsl[:,0]) % 1
#   print(nhsl,'\n-\n',phsl)
  end = len(ndiv)
  ndiv = colour.HSL_to_RGB(nhsl[:end-cut])
  pdiv = colour.HSL_to_RGB(phsl[cut:])

#   print(ndiv,'\n',pdiv)
  if invert:
    ndiv = 1- ndiv


  n_cmp = (jpcm.core.get('div0',cmaps={
      'div0':ndiv
  })[0])

  p_cmp = (jpcm.core.get('div0',cmaps={
    'div0':pdiv
  })[0])

  assert len(n_cmp) == len(p_cmp), f"{len(n_cmp)} != {len(p_cmp)}"

  cmap = matplotlib.colors.ListedColormap([*n_cmp,*p_cmp])
  return cmap
