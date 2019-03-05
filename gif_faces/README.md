## GIF-Faces

Follow the script below to prepare the GIF-Faces dataset

``` bash
# extract videos
tar -xvf ../download/FaceForensics_AVIs.tar

# display a video, or the face track in it
python setup/play_face_video.py
python setup/play_face_video.py --faceonly --expand 1.5

# extract face frames as ground-truth
python python setup/extract_face_frames.py

# compute gif frames using ground-truth images
# modify settings in `generate_gif_image.m` first
cd setup
matlab < generate_gif_image.m
cd ../

# we provide a pytorch dataset interface
python gif_faces.py
# training set is of 457788 frames
# test set is of 104 videos
```
