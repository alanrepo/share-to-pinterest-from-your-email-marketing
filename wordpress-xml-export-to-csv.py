import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd

# Carregue o arquivo XML
tree = ET.parse('exported-from-wordpress.xml')
root = tree.getroot()

# Inicialize listas vazias para cada coluna da planilha
titulos = []
links = []
datas = []
usuarios = []

# Percorra os elementos e extraia as informações
for item in root.findall('.//item'):
    title = item.find('./title').text
    link = item.find('./link').text
    pubDate = item.find('./pubDate').text
    creator = item.find('./dc:creator', namespaces={'dc': 'http://purl.org/dc/elements/1.1/'}).text

    # Formate a data
    pubDate = datetime.strptime(pubDate, '%a, %d %b %Y %H:%M:%S %z')
    pubDate = pubDate.strftime('%A, %d %b %Y %H:%M:%S')

    # Adicione os valores às listas
    titulos.append(title)
    links.append(link)
    datas.append(pubDate)
    usuarios.append(creator)

# Crie um DataFrame com os dados
data = {'Título': titulos, 'Link': links, 'Data da publicação': datas, 'Usuário': usuarios}
df = pd.DataFrame(data)

# Exporte o DataFrame para um arquivo CSV
df.to_csv('resultados.csv', index=False, encoding='utf-8')

print('Resultados foram salvos em resultados.csv')


