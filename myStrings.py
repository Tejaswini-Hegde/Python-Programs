a=input("Enter first string\n")
b=input("Enter second string\n")
while True:
    print("1.Concatenation\n2.UpperCase\n3LowerCase\n4.SwapCase\n5.Reverse\n6.Capitalize\n7.Split\n8.Slicing\n9.Repitition\n10.Length\n11.Slicing Range\n12.Iterating through Strings\n14.Count\n")
    ch=int(input("Enter Your Choice\n"))
    if ch==1:
        print("Concatenateon of two strings is\n",a+b)
    elif ch==2:
        print("UpperCase of strings is\n",a.upper(),b.upper())
    elif ch==3:
        print("LowerCase of strings is\n",a.lower(),b.lower())
    elif ch==4:
        print("SwapCase of strings is\n",a.swapcase(),b.swapcase())
    elif ch==5:
        print("Reverse of strings is\n",a[::-1],b[::-1])
    elif ch==6:
        print("Capitalizing the strings will give\n",a.capitalize(),b.capitalize())
    elif ch==7:
        print("Splitting of strings is\n",a.split(),b.split())
    elif ch==8:   
        print("Slicing of strings is\n",a[5],b[6])
    elif ch==9:
        n=int(input("Enter how many times you want repetition?\n"))
        print("Repitition of strings is\n",a*n,b*n)
    elif ch==10:
        print("Length of strings is\n",len(a),len(b))
    elif ch==11:
        l=int(input("Enter initial range\n"))
        m=int(input("Enter final range\n"))
        print("Slicing of strings is\n",a[l:m],b[l:m])
    elif ch==12:
        for i in a:
            print(i)
        for i in b:
            print(i)
    else:
        print("Invalid Choice\n")
        break
        
