function generate_gif_image(subset, start, finish)

%% settings
s_down = 1; % spatial downsample factor
gif_N = 32; % size of color pallete
dither_opt = 'nodither'; % dither or not

% src and dst directory
frameRoot = '../frames/size360_div12/';
gifRoot = sprintf('../gifs/size360_div12_s%d_g%d_%s/', s_down, gif_N, dither_opt);
flagRoot = fullfile(gifRoot, 'FLAG');
system(['mkdir -p ', flagRoot]);

%% generate gif images
fh = fopen(sprintf('../split/video_info_%s.txt', subset));
fgets(fh);
tmp = textscan(fh, '%s %s %s %s');
videos = tmp{1};
for i = start : min(finish, length(videos))
    disp(['i = ' num2str(i)]);
    video = videos{i};
    
    flagFile = fullfile(flagRoot, video);
    if exist(flagFile, 'file')
        continue;
    end
    
    frameDir = fullfile(frameRoot, video);
    gifDir = fullfile(gifRoot, video);
    system(['mkdir -p ' gifDir]);

    nFrm = numel(dir(fullfile(frameDir, '*.jpg')));
    assert(nFrm > 0, sprintf('no image in dir: %s', frameDir))
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
    system(['touch ', flagRoot, '/', video]);
end

end
