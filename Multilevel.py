class Student:
    def __init__(self,usn=None,name=None,age=0):
        self.usn=usn
        self.name=name
        self.age=age
    def getData(self):
        self.usn=input("Enter USN\n")
        self.name=input("Enter Name\n")
        self.age=int(input("Enter Age\n"))
    def display(self):
        print("USN :",self.usn)
        print("Name :",self.name)
        print("Age :",self.age)
class Base(Student):
    def __init__(self,sub1=0,sub2=0,sub3=0,sub4=0,sub5=0):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
        self.sub5=sub5
    def readMarks(self):
        self.sub1=int(input("Enter Marks of Subject1\n"))
        self.sub2=int(input("Enter Marks of Subject2\n"))
        self.sub3=int(input("Enter Marks of Subject3\n"))
        self.sub4=int(input("Enter Marks of Subject4\n"))
        self.sub5=int(input("Enter Marks of Subject5\n"))
class Derived(Base):
    def disp(self):
        print("Subject1 Marks :",self.sub1)
        print("Subject2 Marks :",self.sub2)
        print("Subject3 Marks :",self.sub3)
        print("Subject4 Marks :",self.sub4)
        print("Subject5 Marks :",self.sub5)
        total=self.sub1+self.sub2+self.sub3+self.sub4+self.sub5
        avg=total/5
        print("Total=",total)
        print("Avg=",avg)
d=Derived()
d.getData()
d.readMarks()
d.display()
d.disp()
    
