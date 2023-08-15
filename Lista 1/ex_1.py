import requests

url = ("https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome")
dados = requests.get(url).json()

partido = str(input("Digite o partido: "))

estado = str(input("Digite o estado: "))

for d in dados['dados']:
    if d['siglaPartido'] == partido and d['siglaUf'] == estado :
        print(d['nome'])