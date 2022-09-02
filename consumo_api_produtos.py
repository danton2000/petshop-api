# O módulo requests ele é utilizado para executar requisições ao serviços web
# O requests não vem disponivel diretamente nas bibliotecas padrões do Python
# Sendo assim é necessário que seja feita a instalação utilizando o regerenciador de
# pacotes PIP.
# > pip install requests
import requests

# Armazenar em uma váriavel o endereço completo da api
url = "http://127.0.0.1:5000/api/produtos"

# Entretando que a rota em questão utiliza um metodo GET, é necessário que o método GET seja executado 
# o método GET ele vai retornar uma requisição 
retorno = requests.get(url)
print(retorno)

# o método .json() ele captura os dados que chegaram na API no formato de JSON e converte em uma estrutura de coleções do Python
dados = retorno.json()
print(dados)