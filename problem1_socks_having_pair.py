socks_string = input("Enter the string :")
socks_string_list = list(socks_string)
print(socks_string_list)
socks_string_set = list(set(socks_string_list))

for i in range(len(socks_string_set)):
    count=0
    for sock1 in socks_string_list:
        if socks_string_set[i].lower() == sock1.lower():
            count+=1
    if count%2 == 0:
        continue
    else:
        break

if i == len(socks_string_set)-1:
    print("True")
else:
    print("False")
