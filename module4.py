dict = {}
n_size = input("Enter the size of N:\n")
for x in range(int(n_size)):
	n_input = input("Enter numbers in N:\n")
	dict[n_input] = x
for x in range(int(n_size)):
	x_input = input("Enter numbers in X:\n")
	if x_input in dict:
		# print("index of this number is: "+str(x))
		print("index of this number is: "+ str(dict[x_input]+1))
	else:
		print(-1)