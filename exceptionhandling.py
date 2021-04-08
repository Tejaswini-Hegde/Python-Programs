while True:
    print("1.Creating the File names of source and destination file\n2.Opening a file in read and write mode\n3.Writing to the files\n4.Reading from the file\n5.Copying Content to a new file\n6.Closing the file\n")
    ch=int(input("Enter Your Choice\n"))
    if ch==1:
        sname=input("Enter the existing File\n")
        dname=input("Enter new File to be created\n")
        print("Two files created")
    if ch==2:
        try:
            A=open(sname,"r")
            B=open(dname,"w")
            print("Choice two successfull\n")
        except NameError:
            print("Please create file before before opening\n")
        except FileNotFoundError:
            print("Enter the existing file name\n")
        else:
            print("Files are opened\n")
    if ch==3:
        try:
            a=A.read()
            B.write(a)
        except NameError:
            print("Please open the file first\n")
        else:
            print("File copied successfully\n")
            A.close()
            B.close()
    if ch==4:
        try:
            B=open(dname,"r")
            B.read()
            print("Read from existing file\n")
        except (ValueError,IOError) as er:
            print("Please Open the file first\n",er)
    if ch==5:
        try:
            A=open(sname,"r")
            B=open(dname,"w")
            str1=A.read()
            B.write(str1)
        except IOError:
            print("Error:cant find or read data\n")
        else:
            print("File successfully copied\n")
            A.close()
            B.close()
    if ch==6:
        try:
            print(A/B)
        except TypeError:
            print("Type Error Cannot  do this operation\n")
