number = int(input("Enter the length of array :"))
sum = int(input("Enter the sum :"))
number_list = list(map(int,input("Enter the elements:").split()))[:number]
count=0
for i in range(len(number_list)):
    flag =0
    for j in range(i+1,len(number_list)):
        if number_list[i]+number_list[j]==sum:
            flag =1
    if flag ==1:
        count+=1
print("Total number of pairs is ",count)
            
