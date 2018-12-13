from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Smash Bros', 'Luta', 'N64')
jogo2 = Jogo('Zelda - Ocarina of Time', 'RPG', 'N64')
lista = [jogo1, jogo2]


@app.route('/')
def index():
    return render_template('lista.html', titulo="Lista de Jogos", jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
