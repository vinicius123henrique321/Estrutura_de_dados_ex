import requests

url = ("https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome")
dados = requests.get(url).json()

partido = str(input("Digite o partido: "))

estado = str(input("Digite o estado: "))

for d in dados['dados']:
    if d['siglaPartido'] == partido and d['siglaUf'] == estado :
        nome = d['nome'].lower()
        print ('Gravando: {nome}')
        f = open(nome + '.png', 'wb')
        foto = requests.get(d['urlFoto']).content
        f.write(foto)
        f.close()