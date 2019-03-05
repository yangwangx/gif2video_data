%% settings
s_down = 1; % spatial downsample factor
gif_N = 32; % size of color pallete
dither_opt = 'nodither'; % dither or not

% src and dst directory
frameRoot = '../face/expand1.5_size256/';
gifRoot = sprintf('../face_gif_image/expand1.5_size256_s%d_g%d_%s/', s_down, gif_N, dither_opt);

%% generate gif images
videos = dir(fullfile(frameRoot,'*.avi'));
for i = 1 : length(videos)
    disp(['i = ' num2str(i)]);
    video = videos(i).name;
    frameDir = fullfile(frameRoot, video);
    gifDir = fullfile(gifRoot, video);
    system(['mkdir -p ' gifDir]);

    nFrm = numel(dir(fullfile(frameDir, '*.jpg')));
    for j = 1:nFrm
        jpgFile = sprintf('%s/frame_%06d.jpg', frameDir, j);
        gifFile = sprintf('%s/frame_%06d.gif', gifDir, j);
        
        im = imread(jpgFile);
        % spatial downsample
        im = imresize(im, 1.0/s_down);
        % gify 
        [X, map] = rgb2ind(im, gif_N, dither_opt);
        imwrite(X, map, gifFile, 'gif');
    end
end
