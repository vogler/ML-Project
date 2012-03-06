%% Machine Learning

function [A, y] = processImages ()
% Initialization
%clear ; close all; clc

% set path
cd ..
dataPath = sprintf("%s/data/", pwd)
cd "octave"
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
			imshow(grayImg)
			grayImgVector = grayImg'(:)';
			A(size(A,1)+1,:) = grayImgVector;
			y(size(y,1)+1,:) = i;
			%imshow(grayImg);
		endif
	end
end
endfunction