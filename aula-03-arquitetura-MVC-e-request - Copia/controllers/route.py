# Importando o remder_Template do flask
from flask import render_template

# Criando a função para receber o flask(app)

def init_app(app):
    # A partir daqui virão as rotas
# Criando a rota principal do site 
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        # criando uma variável
        titulo = "Silk song"
        ano = 2025
        categoria = "Metroidvania"
        
        # Criando um objeto python (dicionário) para representar as propriedades de um jogo
        
        game = {
            "titulo": "Minecraft",
            "ano": 2012,
            "categoria": "Sandbox"
        }
        
        
        jogadores = ["Eduardo", "Vitor", "André", "Caio"]
        return render_template('games.html',
                            titulo=titulo,
                            ano=ano, 
                            categoria=categoria,
                            jogadores=jogadores,
                            game=game
                            )


    @app.route('/consoles')
    def consoles():
        
        titulo = "Consoles"
        consoles = ["switch", "Playstation5", "Xbox", "Pc"]
        return render_template('consoles.html', titulo=titulo, consoles=consoles)
    # def serve para criar funções no pythone home é o nome da função

