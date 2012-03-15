function [pNN, pSVM, pLR] = predict(X)
	m = size(X, 1);
	pNN = ones(m,1)*(-1);
	pSVM = ones(m,1)*(-1);
	pLR = ones(m,1)*(-1);
	load('config.mat');
	load(models_file);
	
	
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
	pNN
	pSVM
	pLR
	%printf("predicted values (-1 means that model was not trained):\n  NN: %d\n  SVM: %d\n  LR: %d\n", pNN, pSVM, pLR);
end