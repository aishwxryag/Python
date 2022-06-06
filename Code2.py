#Program to print extension of the filenamw input by user

filename = input("Input the Filename: ")
fsplit = filename.split(".")
fext=fsplit[1]

#checking commom extensions
if fext=="py":
    print ("The extension of the file is : Python")
elif fext=="c":
    print ("The extension of the file is : C ")
elif fext=="java":
    print ("The extension of the file is : Java")
else:
        print ("The extension of the file is : " + fext)
