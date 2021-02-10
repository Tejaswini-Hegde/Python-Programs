print("Available Options\n")
print("1\n2\n3\n4\n5\n")
while True:
    ch=int(input("Enter your choice\n"))
    if ch==1:
        num=int(input("Enter a number\n"))
        for i in range(0,num+1):
            print(i,end=" ")
        print()
    elif ch==2:
        num=int(input("Enter a number\n"))
        for i in range(0,num+1):
            for j in range(0,i+1):
                print(j,end=" ")
            print()
    elif ch==3:
        num=int(input("Enter a number\n"))
        for i in range(1,num+1):
            for j in range(1,i+1):
                print(i*j,end=" ")
            print()
    elif ch==4:
        num=int(input("Enter a number\n"))
        for i in range(0,num):
            for j in range(0,num):
                print(j,end=" ")
            print()
    elif ch==5:
        num=int(input("Enter a number\n"))
        for i in range(1,num+1):
            for j in range(1,i+1):
                print(j,end=" ")
            for k in range(num+1-i,0,-1):
                print(k,end=" ")
            print()
    else:
        print("Invalid Choice...\n")
                
