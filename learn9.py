#function decorator
# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in 
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1

# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_use = hello_decorator(function_to_be_used)
# calling the function
function_to_be_use()

# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in 
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1

@hello_decorator
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour

# calling the function
function_to_be_used()

# code for testing decorator chaining 
def decor1(func): 
	def inner(): 
		x = func() 
		return x * x 
	return inner 

def decor(func): 
	def inner(): 
		x = func() 
		return 2 * x 
	return inner 

@decor1
@decor
def num(): 
	return 10

@decor
@decor1 
def num2():
	return 10

print(num()) #decor1(decor(num))
print(num2()) #decor(decor1(num2))

# Python code to illustrate
# Decorators with parameters in Python (Multi-level Decorators)


def decodecorator(dataType, message1, message2):
	def decorator(fun):
		print(message1)
		def wrapper(*args, **kwargs):
			print(message2)
			if all([type(arg) == dataType for arg in args]):
				return fun(*args, **kwargs)
			return "Invalid Input"
		return wrapper
	return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
	st = ''
	for i in args:
		st += i
	return st


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ


print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))

print(summation(19, 2, 8, 533, 67, 981, 119))

