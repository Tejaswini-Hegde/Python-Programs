'''l1=[]
n=int(input("Enter the number of values for first tuple\n"))
print("Enter values to be entered for tuple\n")
for i in range(0,n):
    ele=(input())
l1.append(ele)
t1=tuple(l1)
l2=[]
m=int(input("Enter the number of values for second tuple\n"))
print("Enter values to be entered for tuple\n")
for i in range(0,m):
    ele=(input())
l2.append(ele)
t2=tuple(l2)'''
t1=(1,2,3,4,5)
print(t1)
t2=(3,3.04,"RVCE")
print(t2)
while True:
    print("1.Concetination\n2.Repetition\n3.Range slicing\n4.Slicing\n5.Iterating Through String\n6.Length\n7.Maximum value of tuple\n8.Minimum value of tuple\n9.Create\n10.Delete\n")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        print("Concatenation of tuples is\n",t1+t2)
    elif ch==2:
        n=int(input("Enter number of repetitions\n"))
        print("Repetition of strings\n",t1*n,t2*n)
    elif ch==3:
        n=int(input("Enter initial range\n"))
        m=int(input("Enter final range\n"))
        print("Slicing of tuples is\n",t1[n:m],t2[n:m])
    elif ch==4:
        print("Slicing of tuples is\n",t1[0:5],t2[0:5])
    elif ch==5:
        for i in t1:
            print(i)
        for i in t2:
            print(i)
    elif ch==6:
        print("Length of the tuples is\n",len(t1),len(t2))
    elif ch==7:
        print("Maximum of tuple 1 is\n",max(t1))
    elif ch==8:
        print("Minimum of tuple 2 \n",min(t1))
    elif ch==9:
        t3=()
    elif ch==10:
        del t1
        del t2
        print("Deleted tuples\n")
    else:
        print("Invalid choice\n")
        break
        
    
