% Initialization
clear ; close all; clc

if !exist('config.mat')
	config();
endif
load('config.mat');
lambda, maxIter, gamma
fprintf('The following models will be added/overwritten:\n')
use_nn, use_svm, use_lr
if exist(models_file)
    load(models_file);
endif
if (exist("Theta1") && exist("Theta2"))
    disp("nn exists");
endif
if (exist("model"))
    disp("svm exists");
endif
if (exist("Theta"))
    disp("lr exists");
endif

% Load images
cache = sprintf("%s/%s", data_folder, cache_file);
if exist(cache)
    fprintf('Loading generated images (from cache)...\n')
    load(cache);
else
    fprintf('Loading generated images...\n')
    [X,y] = processImages(data_folder);
    save("-mat-binary", cache, "X", "y");
    %save(cache, "X", "y");
endif
X(:,size(X,2)+1) = y;
n_samples = length(y)

% mix row indexes
all_indexed_mixed = randperm(size(X,1));

average_accuracy = 0;
average_accuracy_svm = 0;
average_accuracy_log_reg = 0;
cpu_time_nn = 0;
cpu_time_svm = 0;
cpu_time_lr = 0;
set_size = ceil(length(y)/number_of_sets)

if (do_cross_validation)
	loops = number_of_sets-1;
else
	loops = 0;
endif

for i = 0:loops
	printf('\n===== Starting iteration %i (next training/test set combination) =====\n', i);
	b = min((i+1)*set_size, size(y)); % needed if last set is smaller
	sel = all_indexed_mixed(i*set_size+1 : b); % selecting the current set of row indexes
	
	% define training and test sets
	X_train = X(complement(sel, 1:size(X,1)),1:size(X,2)-1);
	y_train = X(complement(sel, 1:size(X,1)),size(X,2));
	X_val = X(sel, 1:size(X,2)-1);
	y_val = X(sel, size(X,2));

	if (use_nn)
		printf('\n=== neural network in iteration %i\n', i);
		% neural network
		t=cputime;
		[Theta1, Theta2] = nnTrain(X_train, y_train, lambda(1), maxIter);
		cpu_time_nn += cputime-t;
		%printf('Total cpu time for training: %f seconds\n', cputime-t);
		% accuracy when predicting values of test set
		pred = nnPredict(Theta1, Theta2, X_val);
		acc = mean(double(pred == y_val))*100;
		fprintf('Test Set Accuracy (Neural Network): %f\n', acc);
		average_accuracy += length(y_val)*acc;
	endif
	
	if (use_svm)
		printf('\n=== svm in iteration %i\n', i);
		% svm
		t=cputime;
		model = svmtrain(y_train, X_train, sprintf("-q -c %f -t 2 -g %f", lambda(2), gamma));
		cpu_time_svm += cputime-t;
		%printf('Total cpu time for training: %f seconds\n', cputime-t);
		fprintf('Test Set Accuracy (SVM): ');
		[predict_label, acc_svm, dec_values] = svmpredict(y_val,X_val,model);
		average_accuracy_svm += length(y_val)*acc_svm(1);
	endif
	
	if (use_lr)	
		printf('\n=== logistic regression in iteration %i\n', i);
		% logistic regression
		t=cputime;
		Theta = logRegTrain(X_train,y_train, lambda(3), maxIter);
		cpu_time_lr += cputime-t;
		%printf('Total cpu time for training: %f seconds\n', cputime-t);
		p = logRegPredict(Theta,X_val);
		acc = mean(double(p == y_val))*100;
		fprintf('Test Set Accuracy (log reg): %f\n', acc);
		average_accuracy_log_reg += length(y_val)*acc;
	endif
end
if (do_cross_validation)
	if (use_nn)
		average_accuracy /= size(X,1);
		printf('Average accuracy NN: %f\n', average_accuracy);
		printf('Total cpu time for training: %f seconds\n', cpu_time_nn);
	endif
	if (use_svm)
		average_accuracy_svm /= size(X,1);
		printf('Average accuracy SVM: %f\n', average_accuracy_svm);
		printf('Total cpu time for training: %f seconds\n', cpu_time_svm);
	endif
	if (use_lr)
		average_accuracy_log_reg /= size(X,1);
		printf('Average accuracy log reg: %f\n', average_accuracy_log_reg);
		printf('Total cpu time for training: %f seconds\n', cpu_time_lr);
	endif
endif

% save the trained models
printf('saving model...');
save("-mat-binary", models_file, "Theta1", "Theta2", "model", "Theta");