import re
url=input("Enter the url : ")
match = re.search(r"[\w]+\.[a-zA-Z]{2,3}$",url)
print("Domain name : "+match.group(0))
