import requests

#1. Scrapping
url = "http://www.kric.go.kr/jsp/industry/rss/citystapassList.jsp?q_org_cd=A010010021&q_fdate=2021"

html_text = requests.get(url).text
print(html_text)

#2. Parsing
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_text, "html.parser")
print(soup)

#3. Manipulation
tab = soup.find("table", {"class":"listtbl_c100"})
print(tab)

trs = tab.find('tbody').find_all('tr')
trs[1]

tdcols = trs[1].find("td", {"class":"tdcol"})
print(tdcols)

tds = trs[1].find_all('td')
print(tds)

tds[0]
tds[0].text
tds[2].text
tds[3].text

stationpassengers = []
# trs = tab.find('tbody').find_all('tr')
# trs[1:] trs list의 0번째를 제외한 모든 데이터
for tr in trs[1:]:
  dic = {}
  tds = tr.find_all('td')
  dic['station'] = tds[0].text
  dic['ride'] = tds[2].text
  dic['alight'] = tds[3].text
  stationpassengers.append(dic)
  
print(stationpassengers)
