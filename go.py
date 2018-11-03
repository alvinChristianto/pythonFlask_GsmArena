from bs4 import BeautifulSoup
import requests

def go_live():
    headerText = []
    url = "https://www.gsmarena.com/apple_iphone_xs-9318.php"
    content = requests.get(url)
   # content = urllib.urlopen(url).read()
    soup = BeautifulSoup(content.text, "html.parser")
    
    headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})
    headerText = headerDiv.find("h1").getText()
   # print headerText
    return headerText
if __name__ == "__main__":
    print(go_live())
    

