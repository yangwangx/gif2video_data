"""
This script creates 'face_train.txt' and 'face_valid.txt'.
There is NO need to re-run this code! 
You should use the provided '.txt' files.
"""

"""
import glob

# train
with open('../FaceForensics_AVIs/train/rect.txt', 'r') as f:
    with open('face_train.txt', 'w') as newf:
        for line in f.readlines():
            tmp = line.rstrip().split()
            videoID = tmp[0]
            frameDir = '../face/expand1.5_size256/{}/'.format(videoID)
            nFrm = len(glob.glob(frameDir + 'frame_*.jpg'))
            newf.write('{} {}\n'.format(videoID, nFrm))

# valid
with open('../FaceForensics_AVIs/valid/rect.txt', 'r') as f:
    with open('face_valid.txt', 'w') as newf:
        for line in f.readlines():
            tmp = line.rstrip().split()
            videoID = tmp[0]
            frameDir = '../face/expand1.5_size256/{}/'.format(videoID)
            nFrm = len(glob.glob(frameDir + 'frame_*.jpg'))
            newf.write('{} {}\n'.format(videoID, nFrm))
"""
