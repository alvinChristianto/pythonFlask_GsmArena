from bs4 import BeautifulSoup
import urllib2

def go_live():
    headerText = []
    url = "https://www.gsmarena.com/apple_iphone_xs-9318.php"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    
    headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})
    headerText = headerDiv.find("h1").getText()
   # print headerText
    return headerText
if __name__ == "__main__":
    print(go_live())
    

