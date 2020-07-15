class time_operation():
    def __init__(self,hour,minute):
        self.hour=hour
        self.minute=minute

def add(time1_object,time2_object):
    total_hour = time1_object.hour+time2_object.hour
    total_minutes = time1_object.minute+time2_object.minute
    if total_minutes>=60:
        total_hour+=1
        total_minutes-=60
    return "Total time is "+str(total_hour)+" hours "+str(total_minutes)+" minutes"

def difference(time1_object,time2_object):
    if time1_object.minute >= time2_object.minute:
        diff_hour = time1_object.hour - time2_object.hour
        diff_minute = time1_object.minute - time2_object.minute
    else:
        diff_hour = (time1_object.hour-1)-time2_object.hour
        diff_minute = (time1_object.minute+60)-time2_object.minute
    return "Difference in time is "+str(diff_hour)+" hours "+str(diff_minute)+" minutes "

def total_minutes(time1_object,time2_object):
    return "Total time taken in minutes is "+str((time1_object.hour*60)+time1_object.minute+(time2_object.hour*60)+time2_object.minute)

    



time1 = input("1.Enter the hours and minutes separated by space : ").split()
time2 = input("2.Enter the hours and minutes separated by space : ").split()
time1_object = time_operation(int(time1[0]),int(time1[1]))
time2_object = time_operation(int(time2[0]),int(time2[1]))
print(add(time1_object,time2_object))
print(difference(time1_object,time2_object))
print(total_minutes(time1_object,time2_object))

"""
Sample input and output 1:

1.Enter the hours and minutes separated by space :5 50
2.Enter the hours and minutes separated by space :2 15
Total time is 8 hours 5 minutes
Difference in time is 3 hours 35 minutes
Total time taken in minutes is 485

Sample input and output 2:

1.Enter the hours and minutes separated by space :5 15
2.Enter the hours and minutes separated by space :2 40
Total time is 7 hours 55 minutes
Difference in time is 2 hours 35 minutes
Total time taken in minutes is 475

"""
