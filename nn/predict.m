function [pNN, pSVM, pLR] = predict(X)
	load('config.mat');
	load(models_file);
	
	m = size(X, 1);
	
	if (exist("Theta1") && exist("Theta2"))
		% predict with NN
		pNN = predictNN(Theta1, Theta2, X);
	endif
	if (exist("model"))
		% predict with SVM		
		%[predict_label, acc_svm, dec_values] = svmpredict(y_val,X_val,model);
		printf("...ignore this output, it is from libsvm...");
		[pSVM,_,_] = svmpredict(ones(m,1),X,model);
	endif
	if (exist("Theta"))
		pLR = predictLogReg(Theta,X);
	endif
	printf("predicted values:\n  NN: %d\n  SVM: %d\n  LR: %d\n", pNN, pSVM, pLR);
end
