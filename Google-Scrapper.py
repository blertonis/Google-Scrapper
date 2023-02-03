# Google Scrapper - Find Results On Page
# Made by: Blerton 


from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import os.path


def writeCSV(title):
    header = ['Title']
    data = [title]
    if os.path.exists('Data.csv'):
        with open('Data.csv', 'a', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)
    else:
        with open('Data.csv', 'w', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)
        
        
   
      
URL = ''

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", 
           "Accept-Encoding":"gzip, deflate", 
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Connection":"close",
           "Upgrade-Insecure-Requests":"1"}
           
           

def main(search):
    URL = "https://www.google.com/search?q=" + search;
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find_all(class_='DKV0Md');
    for p in title:
        writeCSV(p.getText().strip())
        
 


search = input("Enter keyword:")

main(search)

    


