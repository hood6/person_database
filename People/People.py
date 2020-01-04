class Person:
    def __init__(self, name, age, loc):
        # if not isinstance(name, str) or not isinstance(age, int) or not isinstance(loc, str):
            # print("Illegal types introduced.")
            # return
        self.name = name.title()
        self.age = age
        self.loc = loc.title()

    def to_string(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.loc}"


class Student(Person):
    def __init__(self, name, age, loc, stu_id):
        super().__init__(name, age, loc)
        if not isinstance(stu_id, int):
            print("Student ID must be an integer.")
            return
        self.stu_id = stu_id

    def to_string(self):
        return f"{super().to_string()}\nStudent ID: {self.stu_id}"


class Professor(Person):
    def __init__(self, name, age, loc, tenure):
        super().__init__(name, age, loc)
        if not isinstance(tenure, bool):
            print("Tenure must be a boolean statement (True or False).")
            return
        self.tenure = tenure

    def to_string(self):
        return f"{super().to_string()}\nTenure: {self.tenure}"


class Employee(Person):
    def __init__(self, name, age, loc, employer):
        super().__init__(name, age, loc)
        if not isinstance(employer, str):
            print("Employer must be a string object.")
            return
        self.employer = employer

    def to_string(self):
        return f"{super().to_string()}\nEmployer: {self.employer}"
