% Initialization
%clear ; close all; clc

C = [2^-5,  2^-3,  2^-1,  2^1,  2^3,  2^5,  2^7,  2^9,  2^11, 2^13];
g = [2^-15, 2^-13, 2^-11, 2^-9, 2^-7, 2^-5, 2^-3, 2^-1, 2^1,  2^3];

if !exist('config.mat')
	config();
endif
load('config.mat');
% Load images
cache = sprintf("%s/%s", data_folder, cache_file);
if exist(cache)
    fprintf('Loading generated images (from cache)...\n')
    load(cache);
else
    fprintf('Loading generated images...\n')
    [X,y] = processImages(data_folder);
    save("-mat-binary", cache, "X", "y");
endif

% mix data
X(:,size(X,2)+1) = y;
all_indexes_mixed = randperm(size(X,1));
y = X(all_indexes_mixed, size(X,2));
X = X(all_indexes_mixed,1:size(X,2)-1);
%y(1)
%y(2)
%displayData(X([1,2],:));

acc = [];
for cIt=1:length(C)
	for gIt=1:length(g)
		printf("\n=====> next paramater pair: C = %f, g = %f\n", C(cIt), g(gIt));
		acc(length(acc)+1) = svmtrain(y, X, sprintf("-q -c %f -t 2 -g %f -v 3", C(cIt), g(gIt)));
	end
end
acc
save("-mat-binary", "gridSearchSVMResult.mat", "C", "g", "acc");
