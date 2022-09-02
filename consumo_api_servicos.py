import requests

url = "http://127.0.0.1:5000/api/servicos"

retorno = requests.get(url)

print(retorno)

dados = retorno.json()

print(dados)