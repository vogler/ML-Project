% Initialization
%clear ; close all; clc

l = [2^-15, 2^-13, 2^-11, 2^-9, 2^-7, 2^-5, 2^-3, 2^-1, 2^1,  2^3, 2^4, 2^5];

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

size(X)

all_indexes_mixed = randperm(size(X,1));

n_samples = length(y)
set_size = ceil(length(y)/number_of_sets)
acc = [];

for lIt=1:length(l)
	average_accuracy = 0;
	for i = 0:number_of_sets-1
		printf('\n===== Starting iteration %i (next training/test set combination) =====\n', i);
		b = min((i+1)*set_size, size(y)); % needed if last set is smaller
		sel = all_indexes_mixed(i*set_size+1 : b); % selecting the current set of row indexes
		
		% define training and test sets
		X_train = X(complement(sel, 1:size(X,1)),1:size(X,2)-1);
		y_train = X(complement(sel, 1:size(X,1)),size(X,2));
		X_val = X(sel, 1:size(X,2)-1);
		y_val = X(sel, size(X,2));
		
		[Theta1, Theta2] = nnTrain(X_train, y_train, l(lIt), maxIter);
		pred = nnPredict(Theta1, Theta2, X_val);
		acc = mean(double(pred == y_val))*100;
		average_accuracy += length(y_val)*acc;
	end
	average_accuracy /= size(X,1);
	acc(length(acc)+1) = average_accuracy;
end
acc
save("-mat-binary", "gridSearchNNResult.mat", "l", "acc");
