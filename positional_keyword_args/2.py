
#Example of positional argument with default value.
def my_func(a, b=10, c):
	print("a={0}, b={1}, c={2}".format(a, b, c))

my_func(1, 2, 3) #a=1, b=2, c=3
my_func(1,2) #missing last possitional argument. Exception

"""
On running this example you will get the below error
File "2.py", line 3
    def my_func(a, b=10, c):
               ^
SyntaxError: non-default argument follows default argument
NOTE: This error tels that parameter a is a non default argument which is following a default argument b. As per the notes
once the paramter is defined as default argument then all its following parameter should be default argument in the sequence.
"""
