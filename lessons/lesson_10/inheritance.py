class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce_person(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}")


p = Person("Tim", "Thomas")
print(p)
p.introduce_person()

class Employee(Person):
    
    def __init__(self, first_name, last_name, job_type):
        super().__init__(first_name, last_name)
        self.job_type = job_type

    def work(self):
        print(f"{self.first_name} is working as a {self.job_type}")

    def introduce_person(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} working as a {self.job_type}")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __eq__(self, other_object):
        if isinstance(other_object, Employee):
            return self.first_name == other_object.first_name and self.last_name == other_object.last_name
        return False


e = Employee("Timmy", "Thom", "developer")
print(e)
e.introduce_person()
e.work()
print("---------------")
print(e)
print(e.__str__())



e1 = Employee("Timmy", "Thom", "developer")
e2 = Employee("Timmy", "Thom", "student")
print(e1==e2)