
#Example of positional argument with default value. In this case paramters b and c are optional argument.
def my_func(a, b=10, c=20):
	print("a={0}, b={1}, c={2}".format(a, b, c))

my_func(1, 2, 3) #a=1, b=2, c=3
my_func(1,2) #a=1, b=2, c=20
my_func(1) #a=1, b=10, c=20

