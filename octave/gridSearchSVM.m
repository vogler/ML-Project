% Initialization
%clear ; close all; clc

C = [2^-5,  2^-3,  2^-1,  2^1,  2^3,  2^5,  2^7,  2^9,  2^11, 2^13];
g = [2^-15, 2^-13, 2^-11, 2^-9, 2^-7, 2^-5, 2^-3, 2^-1, 2^1,  2^3];

for cIt=1:length(C)
	for gIt=1:length(g)
		config(C(cIt), 100, g(gIt));
		printf("\n=====> next paramater pair: C = %f, g = %f\n", C(cIt), g(gIt));
		main
	end
end