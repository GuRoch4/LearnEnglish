import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import random

# Inicializando o aplicativo Flask
app = Flask(__name__, template_folder='templates')


# Variáveis globais para a pontuação e mensagem do jogo
mensagem = None
pontos = 0


# Função para conectar ao banco de dados SQLite
def conectar_bd():
    return sqlite3.connect('words.db')


# Rota inicial que renderiza a página inicial com as opções de tema
@app.route('/')
def tela_inicial():
    global pontos
    pontos = 0

    conn = conectar_bd()  #Estabelece uma conexão com o banco de dados SQLite.
    cursor = conn.cursor() #Cria um cursor para executar operações no banco de dados.

    # Obter os nomes das tabelas no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tabelas = cursor.fetchall() #Obtém todos os resultados da consulta.

    # Formata os nomes das tabelas para exibição na página, convertendo-os para o formato desejado.
    tabelas_formatadas = [(formatar_nome_tabela(tabela[0]), tabela[0]) for tabela in tabelas]

    conn.close()
    # Retorna uma renderização do template 'index.html', passando as tabelas formatadas para exibição na página.
    return render_template('index.html', tabelas=tabelas_formatadas)


# Função para formatar o nome da tabela seguindo um padrão específico
def formatar_nome_tabela(nome_tabela):
    if '_' in nome_tabela:
        nome_parts = nome_tabela.split('_')
        nome_formatado = ' '.join(part.capitalize() for part in nome_parts)
        if len(nome_parts) > 1:
            nome_parts.insert(1, '&')
        nome_formatado = ' '.join(nome_parts)
        return nome_formatado
    else:
        return nome_tabela
    

# Rota para escolher um tema específico e redirecionar para a página do jogo
@app.route('/escolher_tema', methods=['POST'])
def escolher_tema():
    tema_escolhido = request.form['tema']
    if tema_escolhido == 'choose':  # Verifica se o tema escolhido é a opção padrão
        # Adicione aqui o que deseja fazer caso 'Select Theme' seja selecionado
        # Neste exemplo, retorna uma mensagem indicando que nenhum tema foi escolhido
        return redirect(url_for('tela_inicial'))

    # Se um tema válido for escolhido, redireciona para a rota 'jogo'
    return redirect(url_for('jogo', tema=tema_escolhido))

# Rota para iniciar o jogo com um tema selecionado
@app.route('/jogo/<tema>')
def jogo(tema):
    conn = conectar_bd()
    cursor = conn.cursor()

    # Selecionando uma palavra aleatória do tema escolhido
    cursor.execute(f"SELECT word_english, word_portuguese FROM {tema} ORDER BY RANDOM() LIMIT 1")
    word_english, word_portuguese = cursor.fetchone()

    conn.close()

    return render_template('jogo.html', word_english=word_english, word_portuguese=word_portuguese, pontos=pontos)


# Rota para verificar a tradução submetida pelo jogador
@app.route('/verificar_traducao', methods=['POST'])
def verificar_traducao():
    global pontos
    global mensagem

    word_english = request.form['word_english']
    traducao_usuario = request.form['traducao_usuario']
    word_portuguese = request.form['word_portuguese']

    if traducao_usuario.lower() == word_portuguese.lower():
        resultado = {
            "correto": True,
            "mensagem": "Correct! The translation of '{}' is '{}'.".format(word_english, word_portuguese)
        }
        pontos += 1
    else:
        mensagem = "The correct translation of '{}' is '{}'.".format(word_english, word_portuguese)
        return redirect(url_for('recomecar_jogo'))
    
    return jsonify(resultado)


# Rota para reiniciar o jogo e exibir uma mensagem sobre a resposta incorreta
@app.route('/recomecar_jogo', methods=['GET'])
def recomecar_jogo():
    global mensagem
    global pontos

    mensagem = mensagem
    pontos = pontos

    return render_template('recomecar.html', mensagem=mensagem, pontos=pontos)


# Executar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
