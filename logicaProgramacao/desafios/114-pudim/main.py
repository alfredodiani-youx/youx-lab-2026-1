import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
    print('O site Pudim não está acessível no momento.')
except:
    print('Consegui acessar o site Pudim com sucesso')