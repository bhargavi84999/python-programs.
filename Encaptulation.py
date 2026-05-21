class Employee:
    def __init__(self, name, age, designation, organization, department, location, mode):
        self.__name = name
        self.__age = age
        self.__designation = designation
        self.__organization = organization
        self.__department = department
        self.__location = location
        self.__mode = mode

    def get_details(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "designation": self.__designation,
            "organization": self.__organization,
            "department": self.__department,
            "location": self.__location,
            "mode": self.__mode
        }
employee1 = Employee(" Bhargavi",20,"student","gitamw","proddatur","india","cse")
print(employee1.get_details())
