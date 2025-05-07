from urllib.request import urlopen
import gzip
from io import BytesIO

def get_source(url):
    'retorna o conteúdo html de uma página da web'
    response = urlopen(url)
    data = response.read()
    if data[:2] == b'\x1f\x8b':  # se for gzip
        data = gzip.GzipFile(fileobj=BytesIO(data)).read()
    return data.decode('utf-8')

print(get_source('http://bettermotherfuckingwebsite.com/'))