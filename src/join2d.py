def join2d(arr2d, joiner1, joiner2):#arr is a list of a list of strings
	"""
	arr2d = [
		["1", "2", "3"],
		["4", "5", "6"],
		["7", "8", "9"] < vertical_depth: 2
	]          ^
	  horizontal_depth: 1
	"""
	outp = []
	for horizontal_depth in range(len(arr2d[0])):
		vertical_arr = []
		for vertical_depth in range(len(arr2d)):
			vertical_arr.append(arr2d[vertical_depth][horizontal_depth])
		outp.append(joiner1.join(vertical_arr))
	
	return joiner2.join(outp)
