from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,age,designation,organization,department,location,mode):
        self.name=name
        self.age=age
        self.designation=designation
        self.organization=organization
        self.department=department
        self.location=location
        self.mode=mode
    @abstractmethod
    def func(self):
        pass
class FullStackDeveloper(Employee):
    def work(self):
        return f" I am a {self.designation} at {self.organization} in the {self.department}working at the {self.location} in {self.mode}"
class FullStackDeveloper:
    def __init__(self, role, branch, college, city, country):
        self.role = role
        self.branch = branch
        self.college = college
        self.city = city
        self.country = country

    def work(self):
        return (f"I am a {self.role} from {self.branch} branch, studying at "
                f"{self.college}, located in {self.city}, {self.country}.")


developer1 = FullStackDeveloper("Student", "CSE", "Gitamw", "Proddatur", "India")
print(developer1.work())
