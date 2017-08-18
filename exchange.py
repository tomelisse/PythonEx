import requests
from bs4 import BeautifulSoup

def get_data(soup, class_name):
    ''' gets the data '''
    t = soup.select(class_name)[0]
    i = t.text.find('=') + 1 
    e = t.text.rfind(' ')
    return float(t.text[i:e])


def convert():
    ''' converts euros <-> PLN '''
    url = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=PLN'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    eur_to_pln = get_data(soup, '.uccResultUnit')
    pln_to_eur = get_data(soup,'.uccInverseResultUnit')
    d = {'eur' : (eur_to_pln, 'pln'), 'pln' : (pln_to_eur, 'eur')}
    how_many, what = input().split()
    print('{:.2f} {}'.format(int(how_many)*d[what][0], d[what][1]))

if __name__ == '__main__':
    convert()
