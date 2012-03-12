function config
	% Setup parameters
	data_folder = '../data';  % folder that contains the generated images
    cache_file  = 'cache.mat';% name of the cache file
	lambda = 1;               % Regularization
	maxIter = 200;            % number of max. iterations

	input_layer_size  = imgSize(data_folder);  % equals resolution of images
	hidden_layer_size = 25;   % 25 hidden units
	num_labels = 10;          % 10 labels, from 1 to 10 (label 0)
	
	set_size = 100;			  % size of the k sets
	
	% libsvm_path = "./";
	% addpath(libsvm_path);
	
	use_nn = true;
	use_svm = true;
	use_lr = true;
	
	save("config.mat");
endfunction