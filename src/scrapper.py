import requests
from bs4 import BeautifulSoup as bs
#import urllib3
import wget
import os

head = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"#,
        #"X-Requested-With": "XMLHttpRequest"
}

url = "https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD"

req = requests.get(url, headers=head)
req.raise_for_status()  #throw exception if failure
soup = bs(req.text, 'html.parser')

#TODO generalize this to include any value inside class for links
fichero = soup.find_all(class_="asociada-link ico-csv")

#Loop to iterate all items and download files with csv
#HACK the href are incomplete, it needs before the link https://datos.madrid.es
links = []
for i in fichero:
    links.append('https://datos.madrid.es'+i['href'])

# To download csv files, that are text based, it is better to use wget
# Apparently requests lib downloads files in a binary format, and it is not
# clear to me how to transform that to text.
for elink in links:
    #TODO implement a check to see if the file was already downloaded. Using SQL?
    #wget.download(elink, os.path.join('/home/victor/development/calidad_aire/downloaded-data', os.path.basename(elink)))
    # Let's try for windows
    wget.download(elink, os.path.join('D:\Proyectos\Programming to study\Python Data Science\calidad_aire\downloaded-data', os.path.basename(elink)))

