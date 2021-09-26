def scramble():
	s1 = "eeessstttt"
	s2 = "testf"
	for i, each in enumerate(sorted(s1)):
		if s2.__contains__(each[i]) == True:
			print("Tere")
		else:
			print("false")
		i += 1

scramble()