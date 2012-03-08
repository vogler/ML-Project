%% Machine Learning

function [A, y] = processImages ()
% Initialization
%clear ; close all; clc

% set path
cd ..
dataPath = sprintf("%s/data/", pwd)
cd "nn"
path = regexprep(dataPath, '\\', '/')

A = []; % matrix to store the image vectors
y = []; % holds the numbers represented by the image vectors
for i=1:10
	currentDirectory = sprintf("%s%d/", path, i);
	%printf(currentDirectory);
	files = readdir(currentDirectory);
	for x=1:length(files)
		if(!isdir(files{x}))
			currentFile = sprintf("%s%s", currentDirectory, files{x});
			rgbImg = imread(currentFile);
			grayImg = rgb2gray(rgbImg);
			grayImgVector = double(grayImg'(:)');
			A(size(A,1)+1,:) = grayImgVector/255;
			y(size(y,1)+1,:) = i;
			% imshow(grayImg);
            % pause
		endif
	end
end
endfunction