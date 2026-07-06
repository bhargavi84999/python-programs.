#functions
def say_hello():
    print("Welcome to Python!")
say_hello()

def add(a, b):
    return a + b
result = add(10, 20)
print(result)

def show_message():
    print("Hello")
result = show_message()
print(result)

def area_of_rectangle(length, width):
    return length * width
area = area_of_rectangle(6, 4)
print(area)

#parameters
def multiply(a, b, c):
    return a * b * c
print(multiply(2, 3, 4))

def describe_pet(animal, name):
    print("My", animal, "is named", name + ".")
describe_pet("dog", "Tommy")

def add(a, b):
    return a + b
add(10,2)

def power(base, exponent):
    return base ** exponent
print(power(2, 3))

def full_name(first, middle, last):
    return first + " " + middle + " " + last
print(full_name("Bhargavi", "Thallapu", "Reddy"))

#positional arguments
def intro(name, city, hobby):
    print(name, "lives in", city, "and likes", hobby)
intro("Bhargavi", "Hyderabad", "Reading")
intro("Reading", "Bhargavi", "Hyderabad")

def subtract(a, b):
    return a - b
print(subtract(10, 3))
print(subtract(3, 10))

def greet(name, age):
    print(name, age)
greet("Bhargavi", 20)

def bio(first_name, last_name, age):
    print("Name:", first_name, last_name)
    print("Age:", age)
bio("Bhargavi", "Reddy", 20)

def add(a, b):
    return a + b
add(10, 20 )

# keyword arguments
def send_email(to, subject, body):
    print("To:", to,"subject:",subject,"body:",body)
send_email(
    body="Meeting at 10 AM",
    to="abc@gmail.com",
    subject="Meeting"
)

def create_profile(username, email, age):
    print("Username:", username)
    print("Email:", email)
    print("Age:", age)

create_profile(
    age=20,
    username="Bhargavi",
    email="bhargavi@gmail.com"
)

#default perameters
def power(base, exponent=2):
    return base ** exponent
print(power(5))      # One argument
print(power(5, 3))   # Two arguments

def connect(host, port=3306, protocol='TCP'):
    print("Host:", host)
    print("Port:", port)
    print("Protocol:", protocol)

# Using default values
connect("localhost")

# Changing port only
connect("localhost", 8080)

# Changing port and protocol
connect("localhost", 8080, "UDP")

# Using keyword arguments
connect(host="localhost", protocol="HTTP")

def func(age, name='Guest'):
    pass

#arbitory perameters

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_all(2, 3, 4))

def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
display_tags(name="Bhargavi", age=20, city="Hyderabad")

def describe_person(name, *hobbies):
    print("Name:", name)
    print("Hobbies:", hobbies)
describe_person("Bhargavi", "Reading", "Coding", "Music")

def f(*args):
    print(type(args))
f(1, 2, 3)

def create_html_tag(tag, **attributes):
    print("<" + tag, end=" ")
    for key, value in attributes.items():
        print(f"{key}='{value}'", end=" ")
    print(">")
create_html_tag(
    "a",
    href="https://python.org",
    target="_blank"
)

def mixed(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

mixed(
    10, 20,
    30, 40, 50,
    name="Bhargavi",
    city="Hyderabad"
)

#functional reference

count = len
numbers = [10, 20, 30, 40, 50]
print(count(numbers))

def run_twice(func, value):
    return func(func(value))
def add_one(x):
    return x + 1
print(run_twice(add_one, 5))

methods = {
    "upper": str.upper,
    "lower": str.lower,
    "title": str.title
}
text = "hello world"
choice = "title"
print(methods[choice](text))

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply
times3 = make_multiplier(3)
print(times3(5))

def greet():
    print("Hello")
functions = {
    "hi": greet,
    "hello": greet,
    "welcome": greet
}
functions["hi"]()
functions["hello"]()
functions["welcome"]()

#lambda functions
cube = lambda x: x ** 3
print(cube(4))

largest = lambda x, y: x if x > y else y
print(largest(10, 20))

even = lambda n: n % 2 == 0
print(even(8))
print(even(7))

items = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
items.sort(key=lambda x: x[1])
print(items)

def square(x):
    return x * x
result = lambda n: square(n)
print(result(5))

#higher order functions

words = ['banana', 'fig', 'apple', 'kiwi']
print(sorted(words, key=len))

nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, nums))
print(result)

nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, nums)
print(result)

animals = ['cat', 'elephant', 'dog', 'ant']
print(sorted(animals, key=len))

names = ['bhargavi', 'ram', 'sita']
result = list(map(str.upper, names))
print(result)

