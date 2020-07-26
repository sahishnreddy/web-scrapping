import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

import js2py

import inspect

from win10toast import ToastNotifier


while True:
    url = 'https://www.flipkart.com/samsung-galaxy-a51-prism-crush-blue-128-gb/p/itme8079f0fedb33?pid=MOBFZ4AJCTQTDJEB&lid=LSTMOBFZ4AJCTQTDJEBZOZVZI&fm=neo%2Fmerchandising&iid=M_162c89e7-431f-49f8-9e38-0539c24c4a43_7.RW6P9C15MAEJ&ppt=clp&ppn=mobile-phones-store&ssid=pjlzcayyds0000001593678834406&otracker=clp_omu_Latest%2BLaunches_3_7.dealCard.OMU_Latest%2BLaunches_mobile-phones-store_RW6P9C15MAEJ_5&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Latest%2BLaunches_NA_dealCard_cc_3_NA_view-all_5&cid=RW6P9C15MAEJ'
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Chrome/83.0.4103.116'}
    # download the homepage
    response = requests.get(url, headers=headers)
    
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "html.parser")
    
    divs = soup.find('div', attrs= {'class':'_3ors59'})
    
    ratings = divs.find('span',attrs={'class':'_38sUEc'})
    
    spans = ratings.findAll('span')
    
    
    
    for span in spans:
        changes = span.text

    
    if span.text == 335: #335 is noof reviews
        # wait 60 seconds,
        time.sleep(60)


        continue
        
    
    else:
        hr=ToastNotifier()

        hr.show_toast("alarm","message")
        
        
        break
