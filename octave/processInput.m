load('config.mat');
% set path
dataPath = sprintf("./%s/", input_folder);
path = regexprep(dataPath, '\\', '/');

X = []; % matrix to store the image vectors
field = []; % vector that stores the corresponding sudoku field of a row in X matrix

files = readdir(path);
for x=1:length(files)
	if(!isdir(files{x}))
		currentFile = sprintf("%s%s", path, files{x});
		rgbImg = imread(currentFile);
		grayImg = rgb2gray(rgbImg);
		grayImgVector = double(grayImg(:)');
		X(size(X,1)+1,:) = grayImgVector/255;
		field(size(field,1)+1,:) = str2num(strsplit(files{x},"."){1});
	endif
end
[pNN, pSVM, pLR] = predict(X);
field
save("-mat-binary", "inputAndPredictedValues.mat", "X", "field", "pNN", "pSVM", "pLR");