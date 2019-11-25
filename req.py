import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bewakoof.com/desi-collection/')
#print(req.status_code)
#print(req.content)

bs = BeautifulSoup(req.content,'html.parser')
fp = open('file_name.csv','w')
fp.write('t-shirt name, price, image\n')

for product in bs.find_all('div', {'class': 'productCardBox'}):
    for detail in product.find_all('div', {'class': 'productCardDetail'}):
        print(detail.find_all('h3'))
        fp.write(str(detail.find_all('h3')[0].text))
        fp.write(',')
        print(detail.find_all('b'))
        fp.write(str(detail.find_all('b')[1].text))
        fp.write(',')
        #fp.write(str(detail.find_all('b')[1].text))
    for product in bs.find_all('div', {'class': 'productCardBox'}):
        for box in bs.find_all('div', {'class': 'productCardImg'}):
            for imgs in box.find_all('img'):
                print(imgs.get('src'))
                fp.write(imgs.get('src'))   
                fp.write(',')
                fp.write('\n') 
                break
            #print(detail.find_all('src'))
        #fp.write(str(detail.find_all('div', {'class': 'productCardImg false'})[2].text))
        #fp.write(',')
            break
        break

fp.close()