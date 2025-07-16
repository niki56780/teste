from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


def conectar():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='JCjoias'
    )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login_usu():
    nome = request.form['nome']
    senha = request.form['senha']

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        comando = "INSERT INTO login (nome, senha) VALUES (%s, %s)"
        dados = (nome, senha)
        cursor.execute(comando, dados)
        conexao.commit()
        cursor.close()
        conexao.close()
        return redirect('/')  
    except Exception as i:
        return f"Erro ao cadastrar produto{i}"
    
@app.route('/cadastro')
def form_cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    senha = request.form['senha']
    cpf = request.form['cpf']
    email = request.form['email']

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        comando = "INSERT INTO usuario (nome, senha, cpf, email) VALUES (%s, %s, %s, %s)"
        dados = (nome, senha, cpf, email)
        cursor.execute(comando, dados)
        conexao.commit()
        cursor.close()
        conexao.close()
        return redirect('/')  
    except Exception as e:
        return f"Erro ao cadastrar: {e}"

@app.route('/produto')
def produto():
    return render_template('produto.html')

@app.route('/produto', methods=['POST'])
def produto_add():
    id = request.form['idProduto']
    nome_produto = request.form['nomeProduto']
    describe = request.form['descricaoProduto']
    valor = request.form['valorProduto']
    salvar =- request.form['btnCancelar']

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        comando = "INSERT INTO produtos (id, nome, descricao, valor) VALUES (%s, %s, %s, %s, %s)"
        dados = (id,nome_produto, describe , valor, salvar)
        cursor.execute(comando, dados)
        conexao.commit()
        cursor.close()
        conexao.close()
        return redirect('/')  
    except Exception as a:
        return f"Erro ao cadastrar produto{a}"
 

@app.route('/sobre')
def sobre():
    return "<h1>Sobre a empresa JC Joias</h1><p>Conteúdo sobre a empresa.</p>"


@app.route('/teste')
def teste():
    return "<h1>Teste de Produto</h1>"






if __name__ == '__main__':
    app.run(debug=True)