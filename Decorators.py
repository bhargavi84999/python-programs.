def func():
    return 1
print(func())
s= 'Global variable'
def func():
    print(locals())
print(globals())
print(globals().keys())
print(globals()['s'])
func()
def hello(name='Jose'):
    print(' The hello() function has been executed')
    def greet():
        return '\t This is inside the greet() function'
    def welcome():
        return '\t This is inside the welcome() function'
    print(greet())
    print(welcome())
    print(" Now we are back inside the hello() function")
hello()
def hello(name='Jose'):
    print(' The hello() function has been executed')
    def greet():
        return '\t This is inside the greet() function'
    def welcome():
        return '\t This is inside the welcome() function'
    if name == 'Jose':
       return greet
    else:
      return welcome
x=hello()
print(x())
greet=hello
print(greet())
def hello():
    return 'Hi Bhargavi!'
def other(func):
    print(' Other code would go here')
    print(func())
other(hello)
def new_decorator(func):
    def wrap_func():
       print(" Code would be here, before executing the func")
       func()
       print(" Code here will execute after the func()")
    return wrap_func
def func_needs_decorator():
    print(" This function is in need of a Decorator")
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
@new_decorator
def func_needs_decorator():
     print(" This function is in need of a Decorator")
func_needs_decorator()

def func_needs_decorator():
    print(" This function is in need of a Decorator")
import time
def time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f" Execution Time:{end_time-start_time:.4f}seconds")
    return wrapper
@time_decorator
def slow_function():
    time.sleep(2)
    print(" Slow function finished")
slow_function()



