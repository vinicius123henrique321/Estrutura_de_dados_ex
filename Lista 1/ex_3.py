import requests

url = ("https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ordem=ASC&ordenarPor=ano")
dados = requests.get(url).json()

partido = str(input("Digite o partido: "))

estado = str(input("Digite o estado: "))

for d in dados['dados']:
     