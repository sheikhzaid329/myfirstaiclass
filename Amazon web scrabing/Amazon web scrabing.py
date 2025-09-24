import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
products=[] 
 
table = soup.find('div',attrs={'data-card-metrics-id':'content-grid-card_apb-browse_1'})
 
for row in table.find_all('div',
                         attrs = {'class':'_Y29ud_bxcGridColumn_J5gfU _Y29ud_bxcGridColumn1Of5_UoKNf'}):
    productss = {}
    productss['img'] = row.img['src']
    productss['product'] = row.img['alt']
    products.append(productss)
 
filename = 'Amazon web scrabing/Amazon_products.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['img'])
    w.writeheader()
    for productss in products:
        w.writerow(products)