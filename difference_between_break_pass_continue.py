# Break statement example

N=int(input())
print("Answer for break statement :",end=" ")
for i in range(N):
    if i==6:
        break
    print(i,end=" ")
print()

# Input : 10
# Output : 0 1 2 3 4 5

# Continue statement example

print("Answer for continue statement :",end=" ")
for i in range(N):
    if i==6:
        continue
    print(i,end=" ")
print()

# Input : 10
# Output : 0 1 2 3 4 5 7 8 9


# Pass statement example

if(N % 2 == 0):
    pass                # Functionality can be added later
else:
    print("N is odd")

# Input : 10
# Output : No output will be printed

# Input : 9
# Output : N is odd
