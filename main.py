# importar o flask que foi instaldo dentro do venv
from flask import Flask

# Criar e aplicação (motor) para execução da aplicação web
app = Flask(__name__)

# Para esta dinamica iremos criar uma rota para listar os produtos
# LEMBRE: a rota é definida dentro da variavel da aplicação
@app.route("/api/produtos")
def produtos():
# A função produtos por estar definida logo após a rota é considerada um função para visões(view function)

    dic = {
        "Chave1": "valor de teste"
    }

    return dic