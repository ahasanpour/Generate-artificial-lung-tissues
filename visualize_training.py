import h5py
import numpy as np
import imageio
import glob, os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--train_dir', type=str, default="/home/ahp/PycharmProjects/SSGAN-Tensorflow-master/train_dir/default-LUNG_lr_0.0001_update_G5_D1-20180304-104836/")
parser.add_argument('--output_file', type=str, default="/home/ahp/PycharmProjects/SSGAN-Tensorflow-master/figure/result/lung/out18.gif")
parser.add_argument('--h', type=int, default=64)
parser.add_argument('--w', type=int, default=64)
parser.add_argument('--c', type=int, default=1)
parser.add_argument('--n', type=int, default=4)
args = parser.parse_args()

if not args.train_dir or not args.output_file:
    raise ValueError("Please specify train_dir and output_file")

II = []
for file in sorted(glob.glob(os.path.join(args.train_dir, "*.hy")), key=os.path.getmtime):
    print (file)
    f = h5py.File(file, 'r')
    I = np.zeros((args.n*args.h, args.n*args.w, args.c))
    for i in range(args.n):
        for j in range(args.n):
            I[args.h*i:args.h*(i+1), args.w*j:args.w*(j+1), :] = f[f.keys()[0]][i*args.n+j,:,:,:]
    II.append(I)

II = np.stack(II)
print II.shape
imageio.mimsave(args.output_file, II, fps=3)
