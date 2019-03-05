## GIF-Moments

Follow the script below to prepare the GIF-Moments dataset

``` bash
# extract videos
tar -xvf ../download/video2gif_segments.tar

# extract video frames as ground-truth
cd setup_frame/
bash run.sh
cd ../

# compute gif frames using ground-truth images
# modify settings in `generate_gif_image.m` first
cd setup_gif/
matlab < run.m
cd ../

# we provide a pytorch dataset interface
python gif_moments.py
# training set is of 60838 videos
# validation set is of 3578 videos
# test set is of 7159 videos
```

