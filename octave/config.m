% this file contains global settings for python/octave scripts
% ========================= CAUTION =========================
% if you change any value here, you have to call config()
% within octave to regenerate the config.mat file

function config (lambda=[1, 30, 20], maxIter=100, gamma=1)
	% Setup parameters
	data_folder = '../data2';  % folder that contains the generated images
    cache_file  = 'cache.mat'; % name of the cache file
	models_file = 'models.mat'; % contains trained models/parameters of nn/svm/lr
	input_folder = '../input'; % folder that contains all images from the observed sudoku
	%lambda = 1;               % Regularization
	%maxIter = 100;            % number of max. iterations

	input_layer_size  = imgSize(data_folder);  % equals resolution of images
	hidden_layer_size = 25;   % 25 hidden units
	num_labels = 9;           % numbers 1-9
	
	number_of_sets = 4;		  % # of k sets
	do_cross_validation = false; % if set to false we train only one time (no cross validation)
	
	use_nn  = lambda(1) != -1;
	use_svm = lambda(2) != -1;
	use_lr  = lambda(3) != -1;
	
	save("-mat-binary", "config.mat");
endfunction