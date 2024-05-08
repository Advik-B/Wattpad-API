from urllib.parse import urlparse, unquote

url = input("Enter the URL: ")
print(unquote(url))