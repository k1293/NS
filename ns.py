import requests
from bs4 import BeautifulSoup

#將此頁面的HTML GET下來
r = requests.get("https://www.ptt.cc/bbs/Gamesale/index.html") 
url="https://www.ptt.cc/bbs/Gamesale/index.html"
#將網頁資料以html.parser
soup = BeautifulSoup(r.text,"html.parser") 

t = "NS"
#往上爬3頁
for i in range(3): 
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    #標題
    sel = soup.select("div.title a") 
    #a標籤
    u = soup.select("div.btn-group.btn-group-paging a") 
    print ("本頁的URL為"+url)
    #上一頁的網址
    url = "https://www.ptt.cc"+ u[1]["href"] 
    #印出網址跟標題
    for s in sel: 
        r=s.text
        #如果標題含有NS在印出
        if r.find(t) !=-1:
            print("https://www.ptt.cc"+s["href"],s.text)