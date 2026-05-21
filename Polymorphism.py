class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

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
        return f"I am a {self.designation} working at {self.organization} in {self.location} ({self.mode})"


employee1 = Employee(
    "Bhargavi", 20, "Student", "GITAMW", "CSE", "Proddatur", "Offline"
)

print(employee1.greet())
print(employee1.work())
