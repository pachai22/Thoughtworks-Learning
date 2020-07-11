# Transpose of student details

students = [['priya','muki','Dhana','mani'],['CSE','Civil','ECE','IT'],[1999,1998,2000,1997]]
print("The given list is",students)
print("The transpose is",[[nested_list[i] for nested_list in students] for i in range(len(students))])



# check even or odd in list

number = int(input("Enter the range : "))
print(["even" if i%2==0 else "odd" for i in range(number) ])
