
#Example of keyword arguments or named arguments.
#In keyword argument or named argument the position is irrelevant
def my_func(a, b=10, c=20):
	print("a={0}, b={1}, c={2}".format(a, b, c))

my_func(c=300, b=200, a=100) #a=100, b=200, c=300. In keyword or named argument position of the argument does not matter.
my_func(100, c=300, b=200) #a=10, b=300, c=200
my_func(100, c=300) #a=100, b=10(default value), c=300
