# Check whether perfect cube or not

import math
number = int(input("Enter the number :"))
cube_number=pow((round(pow(number,1/3))),3)
output = lambda x: "True" if pow((round(pow(x,1/3))),3)==x else "False"
print(output(number))


# Fibonacci series in range of 0 to 15

from functools import reduce
maximum=int(input("Enter the maximum range :"))
fibonacci = list(filter(lambda y : y<=maximum ,reduce(lambda x,_ :x+[x[-1]+x[-2]],range(maximum-2),[0,1])))
print("The fibonacci series is :",fibonacci)
