from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='views')

# Lista de doces (memória)
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

# DOCES
@app.route('/doces')
def doces():
    return render_template('doces.html', doces=listaDoces)

# LOCALIZAÇÃO
@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

# FORMULÁRIO (CADASTRO DE DOCES)
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        listaDoces.append({
            'nome': request.form.get('nome'),
            'descricao': request.form.get('descricao'),
            'preco': request.form.get('preco'),
            'imagem': 'pudim.webp'
        })
        return redirect(url_for('formulario'))

    return render_template('formulario.html', listaDoces=listaDoces)

if __name__ == '__main__':
    app.run(debug=True)