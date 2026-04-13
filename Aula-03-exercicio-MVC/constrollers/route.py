# Importando do flask
from flask import render_template, request, redirect, url_for

# Criando a função para receber o flask(app)
def init_app(app):

    # Lista de doces (substitui listaGames)
    listaDoces = [
        {
            "nome": "Pudim",
            "descricao": "Delicioso e cremoso!",
            "preco": "3,50",
            "imagem": "pudim.webp"
        },
        {
            "nome": "Beijinho",
            "descricao": "Com coco fresquinho!",
            "preco": "3,50",
            "imagem": "peti.jpg"
        }
    ]

    # HOME
    @app.route('/')
    def home():
        return render_template('index.html')


    # DOCES (substitui /games)
    @app.route('/doces')
    def doces():
        return render_template('doces.html', doces=listaDoces)


    # LOCALIZAÇÃO (substitui consoles)
    @app.route('/localizacao')
    def localizacao():
        return render_template('localizacao.html')


    # CADASTRO DE DOCES (substitui cadgames)
    @app.route('/caddoces', methods=['GET', 'POST'])
    def caddoces():
        if request.method == 'POST':
            listaDoces.append({
                'nome': request.form.get('nome'),
                'descricao': request.form.get('descricao'),
                'preco': request.form.get('preco'),
                'imagem': request.form.get('imagem')
            })
            return redirect(url_for('caddoces'))

        return render_template('caddoces.html', listaDoces=listaDoces)