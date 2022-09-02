# petshop-api
Projeto de Petshop, com criações de API com Python

# API da Petshop

Para que possamos criar uma API é necesserario criar o ambiente virutal (venv), com o seguindo comando

    python -m venv venv

Após é necessario a ativação do uso utilizando o seguindo comando

LEMBRE: o venv muitas vezes não está ativo logo que inicia o terminal, o comando de ativação é necessário toda a vez que forem executar uma aplicação

    venv\Script\activate

Com o ambiante virutal devidamente ativado é necessário instalar o flask, utilizando o gerenciador de pacotes chamado de PIP. Segue o comando para a instalação

    pip install flask

O projeto desenvolvido utiliza o módulo 'requests' que não está presente nos módulos padrões disponíveis no Python, com isso é necessário que seja feita a instalação

    pip install requests

## Execução

Para executar a aplicação flask é necessario executar o seguinte comando

    set FLASK_APP=main

    flask --debug run

NOTE: o comando de definição do módulo é executado somente uma vez no ambiente, sendo assim para seguir na execução basta executar o comando flask run
A sujestão é utilizar o parametro --debug para facilitar e identificar de error no desenvolvimento

- O motor do flask deve ser executado em um terminal indepedente
- A aplicação de consumo da API deve ser executada de maneira indepente, ou seja, em um outro terminal


    python -m consumo_api