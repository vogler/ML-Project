function g = sigmoidGradient(z)
	% returns the gradient of the sigmoid function evaluated at z
	% This works regardless if z is a matrix or a vector.
	% Returns gradient for each element in case of z being matrix/vector.
	g = zeros(size(z));
	g = sigmoid(z) .* (1-sigmoid(z));
end
