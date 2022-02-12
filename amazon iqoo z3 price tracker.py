from bs4 import BeautifulSoup
import requests
import time

def find_price():
    html_text=requests.get('https://www.amazon.in/Renewed-iQOO-Storage-Processor-FlashCharge/dp/B09FGPMS7S/ref=sr_1_1?crid=JMO2SMAB3RP1&keywords=iqooz35g6gbramblue&qid=1644632481&sprefix=iqooz35g6gbramblu%2Caps%2C936&sr=8-1').text
    soup=BeautifulSoup(html_text,'lxml')
    phone_name=soup.find('title',class_='a-size-large product-title-word-break').text
    price=soup.find('span',class_='a-offscreen').text
    with open(f'price_tracker/amazon/iqooz3/5g.txt','w') as fl:
      fl.write(f"Phone Name:{phone_name}\n")
      fl.write(f"Price:{price}\n")
    print("File saved successfully")

if __name__=='__main__':
    find_price()
    time_wait=1
    print(f'Waiting {time_wait} minutes')
    time.sleep(time_wait*60)