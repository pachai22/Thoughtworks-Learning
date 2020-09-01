number = int(input("Enter the length of array :"))
sum = int(input("Enter the sum :"))
number_list = list(map(int,input("Enter the elements:").split()))[:number]
count=0

pairs =[]
for i in range(len(number_list)):
    flag =0
    pair =[]
    for j in range(i+1,len(number_list)):
        if number_list[i]+number_list[j]==sum:
            pair.extend([number_list[i],number_list[j]])
            flag =1
    
    if flag ==1:
        count+=1
        pairs.append(pair)
print("Total number of pairs is ",count)
print("Pairs with sum",sum,"are",pairs)
            
