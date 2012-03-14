function theta = logReg (X,y)
	load('config.mat');
	
	% Some useful variables
	m = size(X, 1);
	n = size(X, 2);
	
	% You need to return the following variables correctly 
	theta = zeros(n + 1,9);

	% Add ones to the X data matrix
	X = [ones(m, 1) X];

	% Add Polynomial Features
	% Note that mapFeature also adds a column of ones for us, so the intercept
	% term is handled
	%X = mapFeature(X(:,1), X(:,2));

	% Initialize fitting parameters
	initial_theta = zeros(n+1, 1);

	% Set regularization parameter lambda to 1 (you should vary this)
	lambda = 1;

	% Set Options
	options = optimset('GradObj', 'on', 'MaxIter', maxIter);	

	for i=1:9
		printf("logistic regression for label %i: \n", i);
		theta(:,i) = fmincg (@(t)(costFunctionReg(t, X, (y == i), lambda)), initial_theta, options);
	end
end


