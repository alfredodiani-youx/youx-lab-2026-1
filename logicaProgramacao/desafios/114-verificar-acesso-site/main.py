import urllib
try:
    s = urllib.request.urlopen("https://google.com")
    print("Site aberto com sucesso!")
except:
    print("Erro: ocorreu um erro ao tentar abrir o site!")