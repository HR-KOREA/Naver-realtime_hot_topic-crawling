import requests
from bs4 import BeautifulSoup

jsonpage = requests.get("https://www.naver.com/srchrank?frm=main").json()
realtime_search = jsonpage.get("data")
f = open("실시간 검색어.txt", 'w+t')

for r in realtime_search:
    rank = r.get("rank")#json페이지의 rank값을 읽어옴
    keyword = r.get("keyword")#json페이지의 keyword값을 읽어옴
    print(rank, keyword)
    f.write(f"{rank}. {keyword}")
    f.write('\n')
f.close()