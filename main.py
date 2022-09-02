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
    # Este caminho é informado atraves de um texto, informando o nome do arquivo
    con = sqlite3.connect("petshop.db")

    # Por padrão o retorno dos dados é uma lista de tuplas, mas se desejamos uma lista de dicionários o sqlite3 possui uma configuração na conexão para que esse retorno seja feito
    # con.row_factory = sqlite3.Row

    # Após a conexão é necessário estabelecer um caminho de comunicação
    # Este caminho setá chamado de cursor, nele poderemos enviar comandos ao Banco
    # Os comandos do banco de dados utilizando a linguagem SQL.
    cur = con.cursor()

    # Como boa prática, é interessante criar uma variavel texto, contendo a instrução SQl

    sql = """
        SELECT nome From produtos
    """

    # A variável texto criada no passo anterior é passada por parâmetro para o método
    # execute e simplesmente executa o comando SQL
    cur.execute(sql)

    # Para os casos de comandos SELECT, o banco dados deixa disponível o resultado
    # no entanto, este resultado deve ser coletado atrávez de comando de 
    # buscar tudo (fetchall), e após armazenado em uma variável qualquer.
    dados = cur.fetchall()

    print(dados)

    # Quando não é necessário a utilização do bd, é importando que ele 
    # Seja encerrado através do comando close
    con.close()

    # Para  que esta função retorne uma API é necessário que seja retornado  um tipo de coleção
    # Podendo ser ums lista ou dicionário
    return dados