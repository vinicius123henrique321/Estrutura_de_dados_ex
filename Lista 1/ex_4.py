import requests

url = ("https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ordem=ASC&ordenarPor=ano")
dados = requests.get(url).json()

deputado_dict = {}

for d in dados['dados']:
    forn = d['nomeFornecedor']
    valorT = d['valorDocumento']
    deputado_dict[forn] = valorT


valor = sorted(deputado_dict, reverse=True, key= lambda x: deputado_dict[x])    

for val in valor:
    print(deputado_dict[val])
print(valor)