import os, glob
import numpy as np
import cv2

try:
    cwd = os.path.dirname(os.path.abspath(__file__)) + '/'
except:
    cwd = ''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--subset', default='all', type=str, choices=['all', 'train', 'valid', 'test'], help='which subset')
parser.add_argument('--start', default=1, type=int, help='the start video to process')
parser.add_argument('--finish', default=10, type=int, help='the finish video to process')
opts = parser.parse_args()

def mkdir_p(path):
    try:
        os.makedirs(path)
    except Exception as e:
        pass

def extract_frames(videoPath, dest, pattern='frame_%06d.jpg', image_size=360, image_div=12):
    assert os.path.exists(videoPath)
    videoID = os.path.basename(videoPath)
    mkdir_p(os.path.join(dest, videoID))

    destPattern = os.path.join(dest, videoID, pattern)
    cap = cv2.VideoCapture(videoPath)
    count = 0
    while cap.isOpened():
        count += 1
        ret, frame = cap.read()
        if ret:
            if count == 1:
                h, w = frame.shape[0], frame.shape[1]
                scale = float(image_size) / min(h, w)
                h = int(round(h * scale)) // image_div * image_div
                w = int(round(w * scale)) // image_div * image_div
            frame = cv2.resize(frame, (w, h))
            cv2.imwrite(destPattern%(count), frame)
        else:
            break
    cap.release()

# get a list of videos and infos
videos = []
infos = []
with open(cwd + '../split/video_info_{}.txt'.format(opts.subset), 'r') as f:
    f.readline()
    for line in f.readlines():
        tmp = line.rstrip().split()
        videos.append(tmp[0])
        infos.append(list(map(float, tmp[1:])))
infos = np.array(infos)

# start -> finish
videos = videos[opts.start-1:opts.finish]
infos = infos[opts.start-1:opts.finish]

# extract frames
image_size = 360
image_div  = 12
videoRoot = cwd + '../segments/'
frameRoot = cwd + '../frames/size%d_div%d/'%(image_size, image_div)
mkdir_p(frameRoot + '/FLAG/')
for i, video in enumerate(videos):
    print('%d/%d'%(i+1, len(videos)))
    if not os.path.exists(frameRoot + '/FLAG/' + video):
        extract_frames(os.path.join(videoRoot, video), frameRoot, image_size=image_size, image_div=image_div)
        os.system('touch {}/FLAG/{}'.format(frameRoot, video))
print('Done!')
