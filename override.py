class Employee:
    raise_amt=1.04
    def __init__(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay
    def Display(self):
        print("First :",self.first)
        print("Last  :",self.last)
        print("Employee ID :",self.empid)
        print("Before Raising :",self.pay)
class Developer(Employee):
    raise_amt=1.06
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay
class Manager(Employee):
    raise_amt=1.08
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay
while True:
    print("\n1.Developer\n2.Manager\n")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        first=input("Enter First\n")
        last=input("Enter Last\n")
        empid=int(input("Enter employee id\n"))
        pay=int(input("Enter pay\n"))
        d=Developer(first,last,empid,pay)
        print("On applying raise amount",d.apply_raise())
    elif ch==2:
        first=input("Enter First\n")
        last=input("Enter Last\n")
        empid=int(input("Enter employee id\n"))
        pay=int(input("Enter pay\n"))
        m=Manager(first,last,empid,pay)
        print("On applying raise amount",m.apply_raise())
    else:
        print("Invalid Choice\n")
        break
           
           
    
    

     
