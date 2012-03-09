% Initialization
clear ; close all; clc

config();
load('config.mat');

% Load images
fprintf('Loading data from generated images...\n')
[X,y] = processImages(data_folder);
X(:,size(X,2)+1) = y;

% mix row indexes
all_indexed_mixed = randperm(size(X,1));

average_accuracy = 0;
average_accuracy_svm = 0;
number_of_sets = ceil(length(y)/set_size)

for i = 0:number_of_sets-1
	printf('\n===== Starting iteration %i =====\n', i);
	b = min((i+1)*set_size, size(y)); % needed if last set is smaller
	sel = all_indexed_mixed(i*set_size+1 : b); % selecting the current set of row indexes
	
	% define training and test sets
	X_train = X(complement(sel, 1:size(X,1)),1:size(X,2)-1);
	y_train = X(complement(sel, 1:size(X,1)),size(X,2));
	X_val = X(sel, 1:size(X,2)-1);
	y_val = X(sel, size(X,2));

	% neural network
	[Theta1, Theta2] = train(X_train,y_train);
	% accuracy when predicting values of test set
	pred = predict(Theta1, Theta2, X_val);
	acc = mean(double(pred == y_val))*100;
	fprintf('Test Set Accuracy (Neural Network): %f\n', acc);
	average_accuracy += length(y_val)*acc;
	
	% svm
	model = svmtrain(y_train, X_train, "-q");
	fprintf('Test Set Accuracy (SVM): ');
	[predict_label, acc_svm, dec_values] = svmpredict(y_val,X_val,model);
	average_accuracy_svm += length(y_val)*acc_svm(1);	
end
average_accuracy /= size(X,1);
average_accuracy_svm /= size(X,1);
printf('Average accuracy NN: %f\n', average_accuracy);
printf('Average accuracy SVM: %f\n', average_accuracy_svm);