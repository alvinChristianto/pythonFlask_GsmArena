from bs4 import BeautifulSoup
import requests

#x = raw_input("enter url 1 : ")
#y = raw_input("enter url 2 : ")

url1 = "https://www.gsmarena.com/panasonic_eluga_ray_530-9376.php"
url2 = "https://www.gsmarena.com/apple_iphone_xs-9318.php"
url3 = "https://www.gsmarena.com/apple_iphone_8_plus-8131.php"
url = [url1, url2, url3]
#url = [x, y]

def go_live():
    l = []

    for x in url :

        d = { }
        content = requests.get(x)
        soup = BeautifulSoup(content.text, "html.parser")
        headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})
        d['headerText'] = headerDiv.find("h1").getText()
        headerDivSpec = soup.find("div", {"id": "specs-list"})
        headerTbl = headerDivSpec.find("table")
        headerTr1 =  headerTbl.find("tr")
        headerTh = headerTr1.th.getText()
        d['network_Td1'] = headerTr1.contents[1].getText()
        d['network_Td2'] = headerTr1.contents[3].getText()
        d['network_Td3'] = headerTr1.contents[5].getText()
        
        l.append(d)
    return l
if __name__ == "__main__":
    print(go_live())
    

