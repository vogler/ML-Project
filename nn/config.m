function config
	% Setup parameters
	data_folder = '../data';  % folder that contains the generated images
    cache_file  = 'cache.mat';% name of the cache file
	models_file = 'models.mat'; % for saving trained nn/svm/lr models/parameters
	lambda = 1;               % Regularization
	maxIter = 50;            % number of max. iterations

	input_layer_size  = imgSize(data_folder);  % equals resolution of images
	hidden_layer_size = 25;   % 25 hidden units
	num_labels = 9;           % 9 labels, from 1 to 9
	
	set_size = 1125;			  % size of the k sets
	do_cross_validation = false;	% if set to false we train only with one partition of train/validation sets
	
	use_nn = true;
	use_svm = true;
	use_lr = true;
	
	save("-mat-binary", "config.mat");
endfunction