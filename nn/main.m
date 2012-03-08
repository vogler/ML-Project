%% Initialization
clear ; close all; clc

%% Setup parameters
data_folder = '../data';  % folder that contains the generated images
lambda = 1;               % Regularization
maxIter = 100;            % number of max. iterations

input_layer_size  = imgSize(data_folder);  % equals resolution of images
hidden_layer_size = 25;   % 25 hidden units
num_labels = 10;          % 10 labels, from 1 to 10 (label 0)

% Load images
fprintf('Loading data from generated images...\n')
[X,y] = processImages(data_folder);
m = size(X, 1);

% Randomly display 100 samples
fprintf('Show 100 random samples\n')
sel = randperm(size(X, 1));
sel = sel(1:100);

displayData(X(sel, :));

% Randomly initialize weights
fprintf('Randomly initializing Neural Network Parameters...\n')

initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);

% Unroll parameters
initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];

% Training Neural Network (Backpropagation)...
fprintf('Training Neural Network (Backpropagation)...\n');

% Iterations
options = optimset('MaxIter', maxIter);


fprintf('Using lambda=%f for regularization\n', lambda)

% Create "short hand" for the cost function to be minimized
costFunction = @(p) nnCostFunction(p, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, X, y, lambda);

% Now, costFunction is a function that takes in only one argument (the
% neural network parameters)
[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

% Obtain Theta1 and Theta2 back from nn_params
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));


% Visualize Weights
fprintf('Visualizing Neural Network...\n')

displayData(Theta1(:, 2:end));

% Predict: training set accuracy
pred = predict(Theta1, Theta2, X);

fprintf('Training Set Accuracy: %f\n', mean(double(pred == y)) * 100);