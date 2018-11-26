from bs4 import BeautifulSoup
import requests, time

def go_live():
   # url = "https://www.gsmarena.com/samsung_galaxy_a6s-9352.php"
    url = "https://www.gsmarena.com/samsung_galaxy_note9-9163.php"
    #url = "https://www.gsmarena.com/asus_zenfone_max_(m1)_zb556kl-9373.php"
    l = []
    p = { }
   
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})

    headerDivSpec = soup.find("div", {"id": "specs-list"})    

    headerTbl = headerDivSpec.find("table")        
    headerTr1 = headerTbl.findNext("tr")
    p['title'] = headerDiv.find("h1").getText()
    cnt = 1 
    for y in range(1,13) :
       
        for contentCount in range(0,5) :
           
            try :
                p[contentCount] = headerTr1.contents[contentCount].getText()
   
 
            except :
                pass
        
       
        headerTbl = headerTbl.findNext("table")        
        headerTr1 = headerTr1.findNext("tr")


        l.append(sorted(p.iteritems()))      
          
    return l


if __name__ == "__main__":
    print(go_live())
    

