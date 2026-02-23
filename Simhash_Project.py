import sys
import requests
from bs4 import BeautifulSoup
import re


if len(sys.argv) < 3:
    print("Usage: python main.py <URL1> <URL2>")
    sys.exit()

url1 = sys.argv[1]
url2 = sys.argv[2]


response1 = requests.get(url1)


if response1.status_code != 200:
    print("Unable to fetch URL 1")
    sys.exit()

soup1 = BeautifulSoup(response1.text, "html.parser")

if soup1.body:
    body_text1 = soup1.body.get_text().lower()
else:
    body_text1 = ""


response2 = requests.get(url2)

if response2.status_code != 200:
    print("Unable to fetch URL 2")
    sys.exit()

soup2 = BeautifulSoup(response2.text, "html.parser")

if soup2.body:
    body_text2 = soup2.body.get_text().lower()
else:
    body_text2 = ""


words1 = re.findall(r'[a-z0-9]+', body_text1)
words2 = re.findall(r'[a-z0-9]+', body_text2)

freq1 = {}
for word in words1:
    freq1[word] = freq1.get(word, 0) + 1

freq2 = {}
for word in words2:
    freq2[word] = freq2.get(word, 0) + 1


hash_dict1 = {}
p = 53
m = 2**64

for word in freq1:
    h = 0
    for i in range(len(word)):
        h = (h + (ord(word[i]) + 1) * (p**i)) % m
    bin_h1= bin(h)
    bin_h1=bin_h1[2:]
    if len(bin_h1)<64:
        bin_h1='0'*(64-len(bin_h1))+bin_h1
    hash_dict1[word]=bin_h1

hash_dict2 = {}
for word in freq2:
    h = 0
    for i in range(len(word)):
        h = (h + (ord(word[i]) + 1) *(p**i)) % m
    bin_h2= bin(h)
    bin_h2=bin_h2[2:]
    if len(bin_h2)<64:
        bin_h2='0'*(64-len(bin_h2))+bin_h2
    hash_dict2[word]=bin_h2


arr1 = [0] * 64
for word in hash_dict1:
    h = hash_dict1[word]
    weight = freq1[word]
    for i in range(64):
        if(int(h[i])):
            arr1[i] += weight
        else:
            arr1[i] -= weight


arr2 = [0] * 64
for word in hash_dict2:
    h = hash_dict2[word]
    weight = freq2[word]
    for i in range(64):
        if (int(h[i])):
            arr2[i]+=weight
        else:
            arr2[i] -= weight

string1=""
for i in arr1:
    if i>0:
        string1+="1"
    else :
        string1+="0"
string2=""
for i in arr2:
    if i>0:
        string2+="1"
    else:
        string2+="0"
count = 0
i = 0
j = 0

while i < len(string1) and j < len(string2):
    if string1[i] == string2[j]:
        count += 1
    i += 1
    j += 1

print("comon bit:", count)


        