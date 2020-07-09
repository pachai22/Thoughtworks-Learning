import re
pan_number=input("Enter the number :")
if re.search(r"[A-Z]{5}[\d]{4}[A-Z]{1}",pan_number):
    print("True")
else:
    print("False")
