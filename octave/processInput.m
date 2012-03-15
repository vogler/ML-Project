load('config.mat');
% set path
dataPath = sprintf("./%s/", input_folder);
path = regexprep(dataPath, '/', '\\');

X = []; % matrix to store the image vectors
field = []; % vector that stores the corresponding sudoku field of a row in X matrix

files = glob(sprintf('%s%s', path, '*.png'));

for x=1:length(files)
	if(!isdir(files{x}))
		rgbImg = imread(files{x});
		grayImg = rgb2gray(rgbImg);
		grayImgVector = double(grayImg(:)');
		X(size(X,1)+1,:) = grayImgVector/255;
        [dir, name, ext, ver] = fileparts(files{x});
		field(size(field,1)+1,:) = str2num(name);
	endif
end
[pNN, pSVM, pLR] = predict(X);
save("-mat-binary", "inputAndPredictedValues.mat", "X", "field", "pNN", "pSVM", "pLR");