# class student:
#     def __init__(self, name, marks):   
        
#         self.name = name
#         self.marks = marks
#         print("creating object",self.name)                   


# s1 = student("ayush",78)
# s2 = student("piyush",89)

class Student:
    def __init__(self,name,pmarks,cmarks,mmarks):
        self.name=name
        self.pmarks=pmarks
        self.cmarks=cmarks
        self.mmarks=mmarks

    def avg(self):
        print((self.mmarks+self.cmarks+self.pmarks)/3)

s1 = Student("kamalesh", 89,98,90)
s1.avg()