x = 10
y = 20
# In the above two lines of code x and y are pointing to values 10 and 20 in the memory location. x and y are not assigned with any memory address, however in python they are pointing to the values which
# which are assigned memory address. Hence in python the values are assigned memory address and the variables in which they are assined are pointer to those memory address.

def demo_func(param1, param2):
	"""
	param1 and param2 are the parameters of function demo_func.
	"""
	print(param1, param2)

demo_func(x, y) # x and y are the arguments passed to the demo_func.

