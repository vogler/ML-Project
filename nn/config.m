function config
	% Setup parameters
	data_folder = '../data';  % folder that contains the generated images
	lambda = 1;               % Regularization
	maxIter = 100;            % number of max. iterations

	input_layer_size  = imgSize(data_folder);  % equals resolution of images
	hidden_layer_size = 25;   % 25 hidden units
	num_labels = 10;          % 10 labels, from 1 to 10 (label 0)
	
	set_size = 100;			  % size of the k sets
	
	% libsvm_path = "./";
	% addpath(libsvm_path);
	
	save("config.mat");
endfunction