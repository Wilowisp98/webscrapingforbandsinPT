import sys
sys.path.append("C:\\Users\\Utilizador\\Appdata\\Local\\Packages\\Pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\\Localcache\\local-packages\\Python39\\site-packages")
from bs4 import BeautifulSoup
from urllib.request import urlopen

def teste():
    Concertos = []
    for i in open("bandas.txt").read().splitlines():
        url = "https://www.bol.pt/Comprar/Pesquisa?q=" + i
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        if not soup.find_all(attrs={"class": "botao info"}):
            continue
        for link in soup.find_all(attrs={"class": "botao info"}):
            nexturl = "https://www.bol.pt" + str(link.get('href'))
            nextpage = urlopen(nexturl)
            newhtml = nextpage.read().decode("utf-8")
            newsoup = BeautifulSoup(newhtml, "html.parser")
            date = str(newsoup.find("div", "proxima-sessao").contents[3])[len("<span>"):-len(" </span>")]
            if i + " - " + date in Concertos:
                continue
            Concertos.append(i + " - " + date)
    return Concertos


if __name__ == "__main__":
	print(teste())
