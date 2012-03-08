function s = imgSize (dir)
    file = sprintf("./%s/1/1.png", dir);
    img = imread(file);
    s = size(img(:), 1);
endfunction