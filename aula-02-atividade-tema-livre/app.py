
from flask import Flask, render_template,url_for

app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente de phyton que tem o nome do módulo atual

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/doces')
def doces():
    return render_template('doces.html')

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


if __name__ == '__main__':
    app.run(debug=True) #Ligando modo de depuração, reinicia automático

