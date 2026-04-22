# Importando o remder_Template do flask
from flask import render_template, request, redirect, url_for

# Criando a função para receber o flask(app)
def init_app(app):

    listaGames = [{"titulo": "Minecraft", "ano": 2012, "categoria": "Sandbox"}]
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
    
    #Rota de cadastro de jogos
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            listaGames.append({'titulo': request.form.get('titulo'),'ano': request.form.get('ano'),'categoria': request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html', listaGames=listaGames)
