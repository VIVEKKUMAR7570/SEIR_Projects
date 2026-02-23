import sys
import requests
from bs4 import BeautifulSoup
if(len(sys.argv)<2):
    print("You need to paste url here<ulr>")
    sys.exit()
url=sys.argv[1]
print("URL is " ,url)
responce=requests.get(url)
code=responce.status_code
print(responce.status_code)

print(responce.text)
if (code==200):
    html=responce.text
    print(html)
else:
    print("unable to fetch")
saup= BeautifulSoup(html)
print(saup.title)
print(saup.body)
print(saup.find())
if saup.title:
    print(saup.title.get_text)


if saup.title:
    print(saup.title.get_text())
else:
    print("No title found")

if saup.body:
   
    print(saup.body.get_text().strip())
else:
    print("No body found")


for link in saup.find_all("a"):
    href = link.get("href")
    if href:
        print(href)