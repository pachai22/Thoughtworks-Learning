from urllib.parse import urlparse

url=urlparse("https://www.hackerrank.com/domains/python")

print(url)

print(url.netloc)

print(url.netloc[4:])
