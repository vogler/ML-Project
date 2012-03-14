function config
	% Setup parameters
	data_folder = '../data';  % folder that contains the generated images
    cache_file  = 'cache.mat';% name of the cache file
	lambda = 1;               % Regularization
	maxIter = 100;            % number of max. iterations

	input_layer_size  = imgSize(data_folder);  % equals resolution of images
	hidden_layer_size = 25;   % 25 hidden units
	num_labels = 9;           % 9 labels, from 1 to 9
	
	set_size = 1125;		  % size of the k sets
	do_cross_validation = false; % if set to false we train only one time (no cross validation)
	
	use_nn = true;
	use_svm = false;
	use_lr = false;
	
	save("-mat-binary", "config.mat");
endfunction