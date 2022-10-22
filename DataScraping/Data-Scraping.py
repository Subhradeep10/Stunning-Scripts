import requests
from bs4 import BeautifulSoup
import re
import time


def check_request(url):
    
    print(f'[+] Sending Request to {url}')
    time.sleep(1)  #To avoid load on the server 
    req = requests.get(url)
    
    print(f'[+] Request sent to {url}')
    
    #Checking the status code of the web page
    if req.status_code != 200:
        raise Exception(f'failed to load web page {url} {req.status_code}')
        return -1
    
    print(f'[+] Web Page Loaded Successfully')
    return req.text
    

def url_check(url):
    
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    
    #Checking the url in correct format or not
    if not(re.match(url_pattern, url)):
        
        print(f'ERROR: \"{url}\" URL SHOULD BE IN CORRECT FORMAT[EXAMPLE: https://google.com, https://stackoverflow.com/, ..]')
        return -1

    return 0


def scraping(doc, tag, url):
    
    # Finding all the required the tags in the page
    data_collected = doc.find_all(tag)
    
    if len(data_collected) == 0:
        print(f'[-] There is no present in the given url {url} with {tag} tag')
        return -1
    
    print(f'[+] Data Present in the given url {url} with {tag} tags are: \n')
    for data in data_collected:
        print(data.text) # Printing the data in the tags


def scrap_data(url, tag):
    
    url_check_status = url_check(url)
    if url_check_status == -1:
        print(f'[-] Execution Unsuccessful')
        return
    
    web_content = check_request(url)
    if web_content == -1:
        print(f'[-] Execution Unsuccessful')
        return
    
    doc = BeautifulSoup(web_content, 'html.parser')
    scraping(doc, tag, url)
    print('\n[+] Execution Successfully Completed')

url = input('Enter/Paste The Url: ')
tag = input('Enter the tag you wanna scrape. EX: p, h1, h2....: ')
scrap_data(url, tag)

