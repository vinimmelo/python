from flask import Flask, render_template

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Super Smash Bros', 'Luta', 'N64')
    jogo2 = Jogo('Zelda - Ocarina of Time', 'RPG', 'N64')
    lista = [jogo1, jogo2]
    return render_template('lista.html', titulo="Lista de Jogos", jogos=lista)


if __name__ == '__main__':
    app.run(port=8080)
