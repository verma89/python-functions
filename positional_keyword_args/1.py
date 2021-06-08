
#Example of positional argument
def my_func(a, b, c):
	print("a={0}, b={1}, c={2}".format(a, b, c))

my_func(1, 2, 3) #a=1, b=2, c=3
my_func(1,2) #missing last possitional argument. Exception
