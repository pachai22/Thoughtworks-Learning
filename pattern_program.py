
#Type 1 (Using 2 for loop)

no_of_rows = int(input("Enter the no of rows : "))
if no_of_rows%2 != 0:
    for i in range(1,no_of_rows,2):
        print("*"*i)

    for j in range(no_of_rows,0,-2):
        print("*"*j)

else:
    print("Please enter the odd number of rows")
print()

#Type 2(Using 1 for loop)

no_of_times=1
if no_of_rows % 2 != 0:
    symbol = input("Enter the symbol : ")
    for i in range(1,no_of_rows+1):
        if i < ((no_of_rows//2)+1):
            print(symbol*no_of_times)
            no_of_times+=2
        else:
            print(symbol*no_of_times)
            no_of_times-=2
else:
    print("Please enter the odd number of rows !")
            

''' Input : 5

    Output :

 *
 ***
 *****
 ***
 *

  Input : 7

  Output :

 *
 ***
 *****
 *******
 *****
 ***
 *

'''
