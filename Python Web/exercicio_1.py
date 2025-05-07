# Problema Prático 11.1

# Escreva o método news() que aceita um URL de um site Web de notícias e uma lista de tópicos de notícias (ou seja, strings) e calcula o número de ocorrências de cada tópico nas notícias.

from urllib.request import urlopen
import gzip
from io import BytesIO

def news(url):
    'Conta a as aparições das palavras chave em uma página'
    temas= ['saúde', 'clima', 'educação', 'economia', 'política', 'Lula', 'Bolsonaro']
    response = urlopen(url)
    data = response.read()
    if data[:2] == b'\x1f\x8b':  # se for gzip
        data = gzip.GzipFile(fileobj=BytesIO(data)).read()
    data = data.decode('utf-8')
    print(f'Analisando {url}')
    for tema in temas:
        print(f"{tema} aparece {data.count(tema)} vezes")

news('https://www.poder360.com.br/')