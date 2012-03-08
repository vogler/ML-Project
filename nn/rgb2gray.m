function gray = rgb2gray (rgb)
	% check if rgb is 3-dimensional
	if (size(size(rgb),2)==3)
		len = size(rgb,3);
		gray = rgb(:,:,1)/len;
		for i=2:len
			gray = gray + rgb(:,:,i)/len;
		end
		%gray = round(mean(rgb,3))
	else
		gray = rgb;
	endif
endfunction