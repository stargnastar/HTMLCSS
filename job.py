import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url="https://www.jobkorea.co.kr/starter/?chkSubmit=1&schCareer=1&schLocal=I000,B000,K000&schPart=10031&schMajor=&schEduLevel=5&schWork=1&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0"
res=urlopen(url)
html=res.read()
soup=BeautifulSoup(html, 'html.parser')


# print(soup)

# soup.findAll('li')

# print(res.text)
jobs=soup.find_all("div", attrs={"class":re.compile("^info")})
print(jobs[0]['button'])


# jobs=soup.find_all("li", attrs={"class":re.compile("^calendar-item")})
# print( jobs[0].find("div", attrs={"class":"company-name"}))