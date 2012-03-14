function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% Cost of a particular choice of theta
J = 1/m * (((-y')*log(sigmoid(X*theta))) - (1-y)'*log(1-sigmoid(X*theta)));
J = J + (lambda/(2*m) * sum(theta(2:length(theta)).^2));

% setting grad to the partial derivatives of the cost w.r.t. each parameter in theta
lambdaV = ones(size(theta))*lambda;
lambdaV(1) = 0;
grad = 1/m * (X'*(sigmoid(X*theta) - y) + lambdaV.*theta);

end
