class employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        print(f"role = {self.role}")
        print(f"department = {self.dept}")
        print(f"salary = {self.sal}")

class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age = age
        super().__init__("Engineer", "IT", 60000)


E1 = engineer("shivam", 24)
E1.showDetails()

