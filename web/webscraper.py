import requests
from bs4 import BeautifulSoup

#for element in elements:
   # title_element = element.find('h2', class_='post-title entry-title')
   # print(title_element.text.strip())
  #  print("!!!-------------------------------------------!!!")

def functionpublicacion():
  url = 'https://blog.facialix.com/category/cupones/'
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find(id='grid-wrapper')
  elements = results.find_all('div',class_='post-inner post-hover')
  for element in elements:
    title_element = element.find('h2', class_='post-title entry-title')
    return title_element.text.strip()

ultimapublicacion = functionpublicacion()