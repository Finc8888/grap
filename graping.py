from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
from urllib.error import HTTPError
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BS(html.read())
        title = bsObj.find(class_ ="formSelect")
    except AttributeError as e:
        return None
    return title
# title = getTitle("http://pythonscraping.com/pages/page1.html")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)


title2 = getTitle("https://www.kinopoisk.ru/afisha/new/city/431/")
if title2 == None:
    print("Title could not be found")
else:
    for name in title2:

        print(name.get_text(),"\t")
#---------------------------------------------------------------
#Старая версия где неучтено обработка исключения AtributeError при вводе
#несуществующего тега
# try:
#     html = urlopen("http://pythonscraping.com/pages/page1.html")
#     html2 = urlopen()
#     bsObj = BS(html2.read())
#     print(html.read())
#     print(bsObj.h1)
#     print(bsObj.html.h1)  # Одно и тоже что и в верху
# except HTTPError as e:# при этом надо импортировать ошибку из модуля urllib.error
#     print(e)
#------------------------------------------------------------------











