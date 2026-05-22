import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('O site pudim não está acessivel no momento')
else:
    print('consegui acessar o site pudim')