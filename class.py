# %%
class Student:
    """Just a student class"""
    total = 0
    def  __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total +=1

    def display(self, phno,Branch):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {Branch}")
        print(f"Phone: {phno}")
        self.total_students()

    @classmethod
    def total_students(cls):
        print(f"Total Students: {cls.total}")

    @classmethod
    def change(cls,n):
        cls.total = n

    @staticmethod
    def just(name, age):
        if len(name) < 10 and age < 18:
            print("Name too short and age must be greater than 18")
        else:
            print("Valid credentials")



s1 = Student("John", 25)
s2 = Student("Michael", 35)
s3 = Student("Bob", 35)

s1.display(2345678,"CSE")
print()
Student.display(s1,5678998765,"CSE")
Student.total_students()
Student.change(20)
s1.change(25)
s1.total_students()
Student.total_students()
Student.just("Michael", 35)
s1.just("Michael", 20)

s1.total += 1
print(s1.total)
print(s2.total)
print(s3.total)
print(Student.total)

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(Student.__dict__)




class Student:
    passing_marks = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(f"{self.name} : pass")
        else:
            print(f"{self.name} : fail")

    @classmethod
    def update(cls,pm):
        cls.passing_marks = pm

    @staticmethod
    def grade_category(m):
        if m >= 90:
            return "A"
        elif m >= 80:
            return "B"
        elif m >= 70:
            return "C"
        elif m >= 60:
            return "D"
        else:
            return "F"


s1 = Student("Jaya simha", 99)
s2 = Student("sohail", 98)
s3 = Student("Ganesh", 35)
s4 = Student("RK", 96)

s1.result()
s2.result()
s3.result()
s4.result()

s3.update(99)
s1.marks = 9
s3.marks = 100
s1.result()
s2.result()
s3.result()
s4.result()


print(s1.grade_category(s1.marks))
# %%
class Employee:
    bonus_rate = 0.1
    def __init__(self,name,salary):
        self.name = name
        self.base_salary = salary

    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)

    @classmethod
    def update_bonus(cls,nb):
        cls.bonus_rate = nb

    @staticmethod
    def valid(sal):
        return sal > 0

e1 = Employee("Amarnath", 5000000)
e2 = Employee("Shiva", 5000001)

print(e1.final_salary())
print(e2.final_salary())
e1.update_bonus(0.2)
print(e1.final_salary())
print(e2.final_salary())






# %%
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        t, a = book_str.split("-")
        if cls.is_valid(t):
            return cls(t, a)
        else:
            return "Invalid book string"

    @staticmethod
    def is_valid(t):
        return len(t) >= 3


bts = "Harry potter - J.K.Rowling"
b1 = Book.from_string(bts)
b2 = Book("The song of Ice and Fire", "R.R.Martin")

# %%
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40

student1 = Student("Bhargavi", 85)
student2 = Student("Rahul", 35)
if student1.is_passed():
    print(student1.name, "has Passed")
else:
    print(student1.name, "has Failed")

if student2.is_passed():
    print(student2.name, "has Passed")
else:
    print(student2.name, "has Failed")
# %%
class Employee:
    company_name = "TechCorp"   # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


emp1 = Employee("Bhargavi")
emp2 = Employee("Rahul")


print("Before Change:")
print(emp1.name, "-", emp1.company_name)
print(emp2.name, "-", emp2.company_name)


Employee.change_company("OpenTech")


print("\nAfter Change:")
print(emp1.name, "-", emp1.company_name)
print(emp2.name, "-", emp2.company_name)
# %%
class MathOps:

    @staticmethod
    def is_even(num):
        return num % 2 == 0
print(MathOps.is_even(10))
obj = MathOps()
print(obj.is_even(7))
# %%
class Car:
    wheels = 4

    def __init__(self, mileage):
        self.mileage = mileage

    def display_specs(self):
        print("Mileage:", self.mileage)
        print("Wheels:", Car.wheels)

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels



car1 = Car(20)
car2 = Car(25)

print("Before changing wheels:")
car1.display_specs()
car2.display_specs()


Car.change_wheels(6)

print("\nAfter changing wheels:")
car1.display_specs()
car2.display_specs()
# %%
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def show_conversion(self):
        fahrenheit = Temperature.to_fahrenheit(self.celsius)
        print("Celsius:", self.celsius, "°C")
        print("Fahrenheit:", fahrenheit, "°F")
temp = Temperature(25)
temp.show_conversion()
# %%
class Course:
    total_students = 0

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students += 1
        print(self.student_name, "enrolled successfully.")

    @classmethod
    def show_total(cls):
        print("Total Students:", cls.total_students)

    @staticmethod
    def is_eligible(age):
        return age >= 18
s1 = Course("Bhargavi")
s2 = Course("Rahul")
s3 = Course("Priya")
s1.enroll()
s2.enroll()
s3.enroll()
Course.show_total()
print("Bhargavi Eligible:", Course.is_eligible(20))
print("Rahul Eligible:", Course.is_eligible(16))
# %%
class BankAccount:
    bank_name = "ABC Bank"
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print("Amount Deposited:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid Deposit Amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0
acc1 = BankAccount("Bhargavi", 5000)
acc2 = BankAccount("Rahul", 3000)
print("Bank Name:", BankAccount.bank_name)
acc1.deposit(1000)
acc2.deposit(-500)
BankAccount.change_bank_name("XYZ Bank")
print("\nUpdated Bank Name:", BankAccount.bank_name)
print(acc1.holder, "Balance:", acc1.balance)
print(acc2.holder, "Balance:", acc2.balance)
# %%
