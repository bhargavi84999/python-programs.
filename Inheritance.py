class Person:
    def __init__(self, name, age):
        self.name = name      # assign name attribute
        self.age = age        # assign age attribute

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Employee(Person):
    def __init__(self, name, age, designation, organization, department, location, mode):
        super().__init__(name, age)
        self.designation = designation
        self.organization = organization
        self.department = department
        self.location = location
        self.mode = mode

    def work(self):
        return (
            f"I am a {self.designation} working at {self.organization} "
            f"in the {self.department} department, working from {self.location} "
            f"in {self.mode} mode."
        )


employee1 = Employee(
    "Bhargavi",
    20,
    "Student",
    "GITAM",
    "B.Tech",
    "Proddatur",
    "Open Exams"
)

print("Employee Name:", employee1.name)
print("Employee Age:", employee1.age)
print(employee1.greet())
print(employee1.work())
with open("example.txt","w") as file:
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
with open("example.txt","r") as file:
    file.seek(0)
    contents = file.read()
with open("example.txt","r") as file:
    position=file.tell()
    print(f"Current position: {position}")
with open("example.txt","a") as file:
    file.truncate(10)
with open("example.txt","w") as file:
    file.write("Data")
    file.flush()
with open("example.txt","r") as file:
    print(file.readable())
with open("example.txt","w") as file:
    print(file.writable())
with open("example.txt","r") as file:
    print(file.isatty())
with open("example.txt","r") as file:
    print(file.seekable())
with open("example.txt","r") as file:
    print(file.fileno())
numbers=[1,2,3]
iterator=iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
class Counter:
    def __init__(self,low,high):
        self.current=low
        self.high=high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.high:
            raise StopIteration
        else:
            num=self.current
            self.current+=1
            return num
counter=Counter(1,3)
for num in counter:
    print(num)
def simple_gen():
    yield 1
    yield 2
    yield 3
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
squares=(x*x for x in range(1,4))
for val in squares:
    print(val)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(" Factorial os 5:",factorial(5))
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(" Fibonacci number at positive 6:",fibonacci(6))
add=lambda x,y: x+y
print(" Sum using lambda:",add(3,5))
numbers=[1,2,3,4]
squared=list(map(lambda x:x**2,numbers))
print(" Squared numbers:",squared)
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(" Even numbers:",even_numbers)
def read_write_file(filename):
    try:
         with open(filename,"w")as file:
             file.write(" Trying to write some text to a file with read permission")
             print(" Successfully wrote to the file")
    except PermissionError:
        print(" Error: permission denied to write to the file")
    except Exception as e:
        print(" Error:",e)
    finally:
        print(" File operation completed.")
read_write_file("example.txt")
print("\n")
class NegativeValueError(Exception):
    pass
def check_positive(number):
    if number<0:
        raise NegativeValueError("Negative value entered: {}".format(number))
    else:
        print("Number is positive:",number)
try:
    check_positive(-5)
except NegativeValueError as e:
    print(" Caught user-defined exception:",e)
import re
text="My Fav Dog Breeds Are-Siberian Husky,Shitzu,Chuauo,Pug,ottwReiler."
pattern= "ottwReiler"
mathes=re.findall(pattern,text)
print(" Mathes found:",mathes)
def multi_re_find(patterns,phrase):
    for pattern in patterns:
        print('Searching the phrase using the re check: %r'%pattern)
        print(re.findall(pattern,phrase))
        print("\n")
test_phrase='This is a string wit some numbers 1234567890 and a symbol # hashtag @ at the rate of'
test_patterns=[r'\d+',# sequence of digits
               r'\D+',# non-digits
               r'\s+',# white spaces
               r'\S+',# non-white space
               r'\w+',# alphanumeric
               r'\W+',     # non alphanumeric
               ]
multi_re_find(test_patterns,test_phrase)







