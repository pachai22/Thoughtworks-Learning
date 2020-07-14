class time_operation():
    time1=[]
    time2=[]
    
    def __init__(self,time1,time2):
        self.total_hour=0
        self.total_mins=0
        self.diff_hour=0
        self.diff_mins=0
        self.time1=time1
        self.time2=time2
        
    def add(self):
        self.total_hour=int(self.time1[0])+int(self.time2[0])
        self.total_mins=int(self.time1[1])+int(self.time2[1])
        if self.total_mins >=60:
            self.total_hour+=1
            self.total_mins-=60
        return "Total time is "+str(self.total_hour)+" hours "+str(self.total_mins)+" minutes"

    def difference(self):
        if int(self.time1[1])>=int(self.time2[1]):
            self.diff_mins= int(self.time1[1])-int(self.time2[1])
            self.diff_hour= int(self.time1[0])-int(self.time2[0])
        else:
            self.diff_mins= (int(self.time1[1])+60)-int(self.time2[1])
            self.diff_hour= (int(self.time1[0])-1)-int(self.time2[0])
        return "Difference in time is "+str(self.diff_hour)+" hours "+str(self.diff_mins)+" minutes"
        
    def minutes(self):
        return "Total time in minutes is "+str((int(self.total_hour)*60)+int(self.total_mins))

time1 = input("1.Enter the hours and minutes separated by space :").split()
time2 = input("2.Enter the hours and minutes separated by space :").split()
time_object = time_operation(time1,time2)
print(time_object.add())
print(time_object.difference())
print(time_object.minutes())

"""
Sample input and output 1:

1.Enter the hours and minutes separated by space :5 50
2.Enter the hours and minutes separated by space :2 15
Total time is 8 hours 5 minutes
Difference in time is 3 hours 35 minutes
Total time in minutes is 485

Sample input and output 2:

1.Enter the hours and minutes separated by space :5 15
2.Enter the hours and minutes separated by space :2 40
Total time is 7 hours 55 minutes
Difference in time is 2 hours 35 minutes
Total time in minutes is 475

"""
