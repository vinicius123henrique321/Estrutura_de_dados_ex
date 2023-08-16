import requests

url = ("https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ordem=ASC&ordenarPor=ano")
dados = requests.get(url).json()

soma = 0

for d in dados['dados']:
    valorT = d['valorDocumento']
    valorTotal = float(valorT)
    soma += valorTotal
print(soma)