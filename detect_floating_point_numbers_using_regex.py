import re
number=input("Enter the number : ")
if re.search(r"[+-]?(\d)?\.(\d)",number) is None:
    print("False")
else:
    print("True")
