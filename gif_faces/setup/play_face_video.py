import os, glob, cv2

# get cwd: current working directory
try:
    cwd = os.path.dirname(os.path.abspath(__file__)) + '/'
except:
    cwd = ''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--video', type=str, default=cwd+'../FaceForensics_AVIs/train/rIiQLEa8iZ0_0_rI7GbgEhwoY_1.avi', help='path to .avi file')
parser.add_argument('--faceonly', action='store_true', default=False, dest='faceonly', help='only show face region')
parser.add_argument('--expand', type=float, default=1.5, help='expand factor of the face region')
opts = parser.parse_args()

def expand_region(region, factor):
    x1, y1, x2, y2 = region
    h, w = y2 - y1 + 1, x2 - x1 + 1
    xc, yc = (x2 + x1)/2.0, (y2 + y1)/2.0
    y1, y2 = yc - h*factor/2.0, yc + h*factor/2.0
    x1, x2 = xc - w*factor/2.0, xc + w*factor/2.0
    region = list(map(lambda x: max(0, int(x)), [x1, y1, x2, y2]))
    return region

def square_region(region):
    x1, y1, x2, y2 = region
    h, w = y2 - y1 + 1, x2 - x1 + 1
    hw = max(h, w)
    x2, y2 = x1 + hw - 1, y1 + hw - 1
    return [x1, y1, x2, y2]

# get face region from rect.txt
if opts.faceonly:
    dirname, filename = os.path.split(opts.video)
    vid = filename[:-4]
    rectfile = os.path.join(dirname, 'rect.txt')
    with open(rectfile, 'r') as f:
        for line in f.readlines():
            tmp = line.rstrip().split()
            if tmp[0][:-4] == vid:
                region = list(map(int, tmp[1:]))
                x1, y1, x2, y2 = square_region(expand_region(region, factor=opts.expand))

cap = cv2.VideoCapture(opts.video)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if opts.faceonly:
            frame = frame[y1:y2+1, x1:x2+1, :]
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
    else:
        break
cap.release()
cv2.destroyAllWindows()
