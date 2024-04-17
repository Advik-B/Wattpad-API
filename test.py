import requests

headers = {
    "User-Agent":"insomnia/2023.5.8"
}
r = requests.get(
    "https://www.wattpad.com/v4/parts/1321853334?fields=text_url,group(id,title,description,isPaywalled,url,cover,user(name,username,avatar),lastPublishedPart,parts(id,title,text_url),tags)",
    headers=headers
)

print(r.content)