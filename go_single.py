from bs4 import BeautifulSoup
import requests

def go_live():
   # url = raw_input("enter single url : ")
    url = "https://www.gsmarena.com/samsung_galaxy_a6s-9352.php"
    l = []
    d = { }
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})
    
    d['1_name'] = headerDiv.find("h1").getText()
    
    headerDivSpec = soup.find("div", {"id": "specs-list"})    
    headerTbl = headerDivSpec.find("table")        
    headerTr1 =  headerTbl.find("tr")

    d['2_network'] = headerTr1.contents[1].getText()
    d['3_network'] = headerTr1.contents[3].getText()
    d['4_network'] = headerTr1.contents[5].getText()
    
    headerTblNext = headerTbl.find_next_sibling("table")
    headerTr2 =  headerTblNext.find("tr")
    d['5'] = headerTr2.contents[1].getText()
    d['6'] = headerTr2.contents[3].getText()
    d['7'] = headerTr2.contents[5].getText()
    headerTr2Next = headerTr2.find_next_sibling("tr")
    d['8'] = headerTr2Next.contents[1].getText()
    d['9'] = headerTr2Next.contents[3].getText()
    d['10'] = headerTr2.th.getText()
    d['11'] = headerTr2.find("td", {"class" : "nfo"}).getText()


    l.append(sorted(d.iteritems()))
    return l


if __name__ == "__main__":
    print(go_live())
    

