file_object = open("new_file.txt","w")
file_object.write("Name : K.Pachaiammal \nDOB : 22-05-1999\n")
file_object.close()
file_object = open("new_file.txt","a")
file_object.write("Degree : B.E-ECE")
file_object.close()
file_object = open("new_file.txt","r")
print(file_object.read())


