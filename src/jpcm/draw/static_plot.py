import os
import ffmpeg
import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
from einops import rearrange

import jpcm
from jpcm.core.func import to_div

ndiv = np.array([jpcm.maps.rgb(73,30,60),jpcm.maps.rgb(255,49,46),jpcm.maps.rgb(255,175,0),jpcm.maps.rgb(255,255,255)]) # pretty good right now
cmap = to_div(ndiv,rot=1/3,net_rot=0.0,sat_factor=100).reversed()
# cmap = to_div(ndiv,rot=1/3+0.025/3,net_rot=-0.025,sat_factor=100)

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

def mp4(filename, d, fps=2, triplet=True, mn = None, cmap=cmap, clamp=1.0, time=False):
    """Saves a NumPy array of frames as an MP4 video."""
 
    if d.shape[0] > 4000:
        d = d[1000:3000,...]
        
    if type(cmap) == str:
        cmap = plt.get_cmap(cmap)
 
 
    if triplet:
        frames = d #np.stack([ d[:,0,...], d[:,0,...] + d[:,1,...],d[:,1,...]], axis=1).astype(np.float32) # x_err, xhat, x
        print(frames.shape)
        # if time:
        r = np.nanmax(np.abs(frames[:,0]), axis=(0,2,3))[None,None,:,None,None] # B, Y, C, H, W
        # else:
        #     r = np.max(np.abs(frames[:,-1]), axis=(2,3))[:,None,:,None,None]
        nframes = frames / (2 * r * clamp) + 0.5
        nframes = rearrange(nframes,'b y c h w -> b (c h) (y w)')

    else:
        assert mn is not None
        assert d.shape[1] == mn[0] * mn[1]
        frames = d
        r = np.nanmax(np.abs(frames), axis=(0,2,3))[None,:,None,None] # B, C, H, W
        nframes = frames / (2 * r * clamp) + 0.5
        nframes = rearrange(nframes,'b (c d) h w -> b c d h w', c=mn[0], d=mn[1])
        nframes = rearrange(nframes,'b c d h w -> b (d h) (c w)')
        print(np.nanmax(nframes), np.nanmin(nframes))
        
    print(cmap)
    frames = nframes
    n, height, width = frames.shape
    print(frames.shape)
    process = (
        ffmpeg
        .input('pipe:', format='rawvideo', pix_fmt='rgb24', s=f'{width}x{height}', framerate=fps)
        .output(filename, pix_fmt='yuv420p', vcodec='libx264',
        # r=fps,  # Set the frame rate
        **{
            # X264 encoder parameters (use "-x264-params" syntax)
            'x264-params': 'keyint=1:qp=0:no-scenecut=1'
        },
        vsync='passthrough',  # Constant frame rate
        # fps_mode='passthrough',  # Force constant frame rate
        preset='ultrafast',      # Minimize CPU processing
        tune='zerolatency'       # Disable lookahead
        )
        .overwrite_output()
        .run_async(pipe_stdin=True)
    )
    for frame in frames:
        cframe = cmap(frame)[...,:3] * 255
        process.stdin.write(cframe.astype(np.uint8).tobytes())
    process.stdin.close()
    process.wait()


if __name__ == '__main__':    

    names = ['valid','infer']
    directory = 'run/'
    remake = True #False

    print('scan directory')
    gen = fast_scandir(directory)
    for path in tqdm(gen):
        fname = os.path.join(path,'valid.mp4')
        qname = os.path.join(path,'infer.npz')
        if (not os.path.exists(fname) and os.path.exists(qname)) \
              or (os.path.exists(qname) and remake):
            print(path)
            try:
                data = [np.load(os.path.join(path,f"{x}.npz"))['arr_0'] for x in names]    
                for name, d in zip(names, data):
                    fname = os.path.join(path,f'{name}.mp4')
                    mp4(fname, d)
            except Exception as e:
                print(e)

# run this script with 
# conda activate ./sw
# source .venv/bin/activate
# python3 src/ml/runners/basic_plot.pyWW