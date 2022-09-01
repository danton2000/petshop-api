# importar o flask que foi instaldo dentro do venv
from flask import Flask

# Criar e aplicação (motor) para execução da aplicação web
app = Flask(__name__)

# Para que seja possivel conectar-se a um banco de dados é necessário utilizar o DBI
# Neste caso utilizaremos o SGBD SQLite, sendo assim devemos importa o módulo sqlite3
import sqlite3

# Para esta dinamica iremos criar uma rota para listar os produtos
# LEMBRE: a rota é definida dentro da variavel da aplicação
@app.route("/api/produtos")
def produtos():
# A função produtos por estar definida logo após a rota é considerada um função para visões(view function)

    # O primeiro passo para o uso do banco de dados é a conexão
    # Para estabelecer uma conexão é que seja informado o caminho da conexão
    # Este caminho é informado atraves de um texto
    con = sqlite3.connect("petshop.db")

    dic = {
        "Chave1": "valor de teste"
    }
    # Para  que esta função retorne uma API é necessário que seja retornado  um tipo de coleção
    # Podendo ser ums lista ou dicionário
    return dic