#Type 1

from urllib.parse import urlparse

url=urlparse("https://www.hackerrank.com/domains/python")

print(url)

print(url.netloc)

print(url.netloc[4:])

#Type 2

import re

url="https://www.hackerrank.com/domains/python"

x=re.findall(r"www.(.*?)/d",url)

print(*x)

