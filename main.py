# importar o flask que foi instaldo dentro do venv
from flask import (
    Flask,
    # O módulo jsonify é utilizado para converter uma coleção qualquer em um documento no formato json
    jsonify 
)

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

@app.route("/api/servicos")
def servicos():

    con = sqlite3.connect("petshop.db")

    cur = con.cursor()

    sql = """
        SELECT nome From servicos
    """

    cur.execute(sql)

    dados = cur.fetchall()

    print(dados)

    con.close()

    return dados

# Definição da rota através do decorador .route
# A rota que foi criada está utilização o formato dinâmico de definições rota
# A parte dinâmica da rota é identificada pelos simbolos "<" e ">"
# NOTE: as rotas não tem relações entre si
@app.route("/api/produtos/<nome>")
# O parâmetro utilizado na função é o mesmo nome utilizado na parte dinâmica da rota
def produto_detalhes(nome): # View Function(Função de visião)

    # Conexão com o banco de dados
    con = sqlite3.connect("petshop.db")

    # Criação do cursor
    cur = con.cursor()

    # A variável SQL é uma instrução de banco de dados, que é representada com um texto no
    # Python, sendo assim não existe uma validação pelo Python, a validação só acontence 
    # No momento que a consulta é enviada para o Banco de Dados, utilizando o cursor que 
    # no código em questão é representado pela variável 'cur'

    # Para simplificar a codificação do SQL é interessante utilizar as aspas duplas como
    # simbolos para definir textos
    # Uma forma de aplicar um filtro dinâmico na consulta que será enviada, é a utilização
    # de alguma forma de interpolação
    sql = f"""
        SELECT nome, descricao, valor
        FROM produtos
        WHERE nome = '{nome}'
    """

    #Executar a consulta uitlizando o cursor
    cur.execute(sql)

    # Para casos de consulta que retorna somente um registro, o uso do fetchone (busca um registro) é o método mais indicado para este tipo de ação
    # NOTE: o uso do fetchone retorna somente uma tupla, quando for fetchall retorna uma lista de tuplas
    dados = cur.fetchone()

    #fechar a conexão
    con.close()

    # toda função de visão deve ter um retorno
    # No caso que a informação armazenada na variavel "dados" é uma tupla, se faz necessário
    # A utilização ao jsonify
    return jsonify(dados)