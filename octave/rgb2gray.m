function gray = rgb2gray (rgb)
	% check if rgb is 3-dimensional
	if (size(size(rgb),2)==3)
		gray = rgb(:,:,1)/3+rgb(:,:,2)/3+rgb(:,:,3)/3;
	else
		gray = rgb
	endif
endfunction