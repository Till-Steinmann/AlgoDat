def lookup(s):
	j = 0
	
	while t[(h(s) - g(s, j)) mod m] \
			is not None:
		
		if t[(h(s) - g(s, j)) mod m][0] == s:
			return t[(h(s) - g(s, j)) mod m]
		
		j += 1
	
	return None