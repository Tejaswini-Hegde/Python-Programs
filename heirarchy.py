class Student:
    def __init__(self,usn=None,name=None,age=0):
        self.usn=usn
        self.name=name
        self.age=age
    def getData(self):
        self.usn=int(input("Enter USN\n"))
        self.name=input("Enter Student Name\n")
        self.age=int(input("Enter Age\n"))
    def display(self):
        print("USN  :",self.usn)
        print("Name :",self.name)
        print("Age  :",self.age)
class UG_Student(Student):
    def __init__(self,sem=0,fees=0,stipend=0):
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
    def UgGetdata(self):
        self.sem=input("Enter Sem\n")
        self.fees=int(input("Enter Fees\n"))
        self.stipend=int(input("Enter stipend\n"))
    def Ugdisplay(self):
        print("SEM :",self.sem)
        print("Fees :",self.fees)
        print("Stipend :",self.stipend)
class PG_Student(Student):
    def __init__(self,sem=0,fees=0,stipend=0):
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
    def PgGetdata(self):
        self.sem=input("Enter Sem\n")
        self.fees=int(input("Enter Fees\n"))
        self.stipend=int(input("Enter stipend\n"))
    def Pgdisplay(self):
        print("SEM :",self.sem)
        print("Fees :",self.fees)
        print("Stipend :",self.stipend)
ug=UG_Student()
pg=PG_Student()
while True:
    print("1.UG Details\n2.PG Details\n")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        ug.getData()
        ug.UgGetdata()
        ug.display()
        ug.Ugdisplay()
    elif ch==2:
        pg.getData()
        pg.PgGetdata()
        pg.display()
        pg.Pgdisplay()
    else:
        print("Invalid Choice\n")
        break
    
        
