tup=("www","hackerrank","com","domains","python")
url=""
for i in range(len(tup)):
    if i==1 or i==2 :
        url=(url+"."+tup[i])
    else:
        url=(url+"/"+tup[i])
print(url)
