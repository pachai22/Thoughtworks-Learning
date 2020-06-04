tup=("www","hackerrank","com","domains","python")
str=""
for i in range(len(tup)):
    if i==1 or i==2 :
        str=(str+"."+tup[i])
    else:
        str=(str+"/"+tup[i])
print(str)
