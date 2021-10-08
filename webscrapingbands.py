import sys
sys.path.append("C:\\Users\\Utilizador\\Appdata\\Local\\Packages\\Pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\\Localcache\\local-packages\\Python39\\site-packages")
from bs4 import BeautifulSoup
from urllib.request import urlopen

def teste():

    Bandas = []
    for i in open("bandas.txt").read().splitlines():
        Bandas.append(i)

    # BOL
    ConcertosBOL = []
    for i in Bandas:
        if " " in i:
            j = i.replace(" ", "+")
            url = "https://www.bol.pt/Comprar/Pesquisa?q=" + j
        else:
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
            if i + " - " + date in ConcertosBOL:
                continue
            ConcertosBOL.append(i + " - " + date)
        Bandas.remove(i)

    # TICKETLINE
    ConcertosTL = []
    for k in Bandas:
        if " " in k:
            j = k.replace(" ", "+")
            url = "https://ticketline.sapo.pt/pesquisa?query=" + j
        else:
            url = "https://ticketline.sapo.pt/pesquisa?query=" + k
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        if not soup.find_all(attrs={"itemprop": "startDate"}):
            continue
        for j in soup.find_all(attrs={"itemprop": "startDate"}):
            date = (str(j).split('content="', 1)[1]).split('"')[0]
            if k + " - " + date in ConcertosTL:
                continue
            ConcertosTL.append(k + " - " + date)
            
    if not (ConcertosBOL or ConcertosTL):
        return "Infelizmente não existem concertos :("

    if ConcertosBOL:
        print("Recolha referente ao site da BOL : ")
        for i in ConcertosBOL:
            print(" -> " + i)
    if ConcertosTL:
        print("Recolha referente ao site da TicketLine : ")
        for i in ConcertosTL:
            print(" -> " + i)

if __name__ == "__main__":
	print(teste())
