from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

link = 'https://search.brave.com/search?q=cota%C3%A7%C3%A3o+d%C3%B3lar'
headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
print(requisicao)
site = BeautifulSoup(requisicao.text, "html.parser")
dolar = site.find('span', class_='amount t-primary svelte-ygvd8h')
print(dolar.get_text())

#print(requisição)
#print('\n' * 5)
#print(requisição.text)
#print(site.prettify())
#title = site.find('title')
#print(title)

#pesquisa = site.find_all('input')
#print(pesquisa)

#pesquisa2 = site.find_all('input', class_='gLFyf')
#print(pesquisa2)