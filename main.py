from bs4 import BeautifulSoup
import requests

url = 'https://www.sodimac.com.pe/sodimac-pe/product/1665278/mesa-plegable-180x76x74cm-blanco/1665278/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')
print(soup.select('.primary > span:nth-child(2)')[0].text)
