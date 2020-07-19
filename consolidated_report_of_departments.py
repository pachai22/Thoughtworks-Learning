class Department:
    def __init__(self,dep_name,students,subjects):
        self.dep_name = dep_name
        self.students = students   # list - nested lists that contains each student's id,name,nested list of subjects taken
        self.subjects = subjects
        
def fetch_students_list(department_objects,department):
    for department_object in department_objects:
        if (department_object.dep_name).lower() == department.lower():
            print("The students in",department_object.dep_name," department :")
            students_list = department_object.students
            for student in students_list:
                print(student[1])

def department_name(department_objects,department):    
    for department_object in department_objects:
        students_list = department_object.students
        for student in students_list:
            if len(student[2]) >= 3:
                dep_list.append(department_object.dep_name)
    print("\nDepartment list where student take more than 3 courses : ",set(dep_list))   
            
def overlap_subjects(ece,it,mechanical):
    ece_subjects = set(ece.subjects)
    it_subjects = set(it.subjects)
    mechanical_subjects = set(mechanical.subjects)
    print("The overlap subjects between departments are : ",ece_subjects.intersection(it_subjects,mechanical_subjects))

dep_list = []
ece = Department("ECE",[[1,"Pachai",["SS","Dsp","Python"]],[2,"Dharani",["EC","Dsp","DLC"]],[3,"Paramu",["Dsp","DLC"]],[4,"Niki",["EC","Pom"]]],["Dsp","Pom","SS","EC","Python","DLC"])
it = Department("IT",[[1,"Poorni",["MC","Python"]],[2,"Vishalini",["Python"]],[3,"Menaga",["DS","Pom"]],[4,"Niranj",["DC","AI"]]],["DS","Python","Pom","MC","DC","AI"])
mechanical = Department("Mechanical",[[1,"Sathya",["Python","Thermodynamics","Pom"]],[2,"Santhosh",["Fluid Mechanics"]],[3,"Yogesh",["Aircraft"]]],["Python","Pom","Thermodynamics","Fluid Mechanics","Aircraft"]) 
overlap_subjects(ece,it,mechanical)
department = input("Enter the department to print students list : ")
fetch_students_list([ece,it,mechanical],department)
department_name([ece,it,mechanical],department)

