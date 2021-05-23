
while True:
    print("1.Cocatinate\n 2.Size of\n 3.Length\n 4.Append\n 5.Count\n 6.Reverse\n 7.Remove\n 8.Insert\n 9.Pop\n 10.Sort\n")
    print("Enter a list")
    a=[1,2,3,4,5,'RVCE']
    print("Enter another list\n")
    b=[2,5,7,8,9]
    ch=int(input("Enter your choice\n"))
    if ch==1:
        print("Concatition of two tuples\n",a+b)
    elif ch==2:
        print("Size of the size of a \n",sizeof(a))
    elif ch==3:
        print("Length of the list\n",len(a))
    elif ch==4:
        print("Append\n",a.append("MCA"))
    elif ch==5:
        print("Count of b\n",count(b))
    elif ch==6:
        print("Reverse\n",a.reverse(a))
    elif ch==7:
        print("Remove '1' from list a\n",a.remove(5))
    elif ch==8:
        print("Insert '1' to list a\n",a.insert(4))
    elif ch==9:
        print("Pop 4\n",b.pop(5))
    elif ch==10:
        print("Sort the list\n",b.sort())
    else:
        print("Invalid Choice")
