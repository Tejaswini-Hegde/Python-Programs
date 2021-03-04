d={}
class Employee:
    def Salary_slip(self,name,address,panno,basic,tds=0,deduct=0):
        self.name=name
        self.address=address
        self.panno=panno
        self.basic=basic
        self.hra=1.157*basic
        self.da=0.25*basic
        self.cca=200
        self.pf=1800
        self.pt=300
        self.tds=tds
        self.deduct=deduct
        netsal=self.basic+self.da+self.hra+self.cca-(self.pf+self.pt+self.tds)
        return  netsal
    def accept(self):
        name=input("\nEnter the Employee name:\n")
        address=input("Enter the address:\n")
        panno=input("Enter PAN no.:\n")
        basic=int(input("Enter basic pay:\n"))
        tds=int(input("Enter TDS:\n"))
        deduct=int(input("Enter deduct amount:\n"))
        self.netsal=self.Salary_slip(name,address,panno,basic,tds,deduct)
    def display(self):
        print("Name : ",self.name)
        print("Address : ",self.address)
        print("PAN no. : ",self.panno)
        print("Basic Pay : ",self.basic)
        print("Net Salary : ",self.netsal)
    def search(self,name):
        for k,v in d.items():
            print("k== ",k)
            print("v== ",v)
            if k==name:
                print(v.name)
                print(v.address)
                print(v.netsal)
while True:
    print("\n1.Enter Employee Details\n2.Display\n3.Update\n4.Search\n5.Exit\n")
    ch=int(input("Enter Your Choice\n"))
    if ch==1:
        print("-----Enter Employee Details----\n")
        e=Employee()
        e.accept()
    elif ch==2:
        print("-----Display-----\n")
        e.display()
    elif ch==3:
        print("----Update the Details-----\n")
        d.update({e.name:e})
        print("-----Updated-----")
        print(d)
    elif ch==4:
        print("-----Search The Details-----\n")
        e.search(input("Enter name\n"))
    elif ch==5:
        break
    else:
        print("Invalid Choice\n")
    
            
