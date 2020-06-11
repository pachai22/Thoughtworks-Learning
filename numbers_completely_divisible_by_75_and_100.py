
minimum_range,maximum_range = int(input()),int(input()) # 200 and 1500

divisor1 , divisor2 = int(input()),int(input()) # 75 and 100

for number in range(minimum_range,maximum_range+1):
    if number % divisor1 ==  0 and number % divisor2 == 0:
        print(number,end=" ")

#Input :
#        200
#        1500
#         75
#         100
# Output : 300 600 900 1200 1500

