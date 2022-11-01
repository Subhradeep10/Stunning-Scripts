import requests
from bs4 import BeautifulSoup

URL = '''https://www.dictionary.com/browse/'''
result_class = 'one-click-content css-nnyc96 e1q3nk1v1'


def find(word2):

    word=''

    for item in word2:
        word+=item


    a=requests.get(URL + word).content
    soup = BeautifulSoup(a, "html.parser")

    try:
        # Checking if the Word Exists or not
        soup.find_all("span",{"class":result_class})[0].get_text()

        # Checking if the word is an Abbreviation or not. If yes, Then retur False
        isType=soup.find_all('span',{"class":'pos'})[0].get_text()

        if('abbreviation' in isType):
            return False

        return True
    except:
        return False


if __name__=='__main__':
    print(find(('t','a','c')))