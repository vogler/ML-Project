function [Theta1, Theta2] = nnTrain(X, y, _lambda, _maxIter)
	load('config.mat');
	
	m = size(X, 1);

	% Randomly display 10 samples
	% fprintf('Show 10 random samples\n')
	% sel = randperm(size(X, 1));
	% sel = sel(1:10);
	% displayData(X(sel, :));

	% Randomly initialize weights
	fprintf('Randomly initializing Neural Network Parameters...\n')

	initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
	initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);

	% Unroll parameters
	initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];

	% Training Neural Network (Backpropagation)...
	fprintf('Training Neural Network (Backpropagation)...\n');

	% Iterations
	options = optimset('MaxIter', _maxIter);

	fprintf('Using lambda=%f for regularization\n', _lambda)

	% Create "short hand" for the cost function to be minimized
	costFunction = @(p) nnCostFunction(p, ...
									   input_layer_size, ...
									   hidden_layer_size, ...
									   num_labels, X, y, _lambda);

	% Now, costFunction is a function that takes in only one argument (the
	% neural network parameters)
	[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

	% Obtain Theta1 and Theta2 back from nn_params
	Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
					 hidden_layer_size, (input_layer_size + 1));

	Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
					 num_labels, (hidden_layer_size + 1));


	% Visualize weights
	fprintf('Visualizing Neural Network...\n')

	%displayData(Theta1(:, 2:end));
endfunction