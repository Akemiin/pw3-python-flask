# Cometário dem Python
# Importando o Flask na aplicação
from flask import Flask, render_template 
#Render template renderiz as paginas HTML
from controllers import route

from models.database import db # Importando o banco de dados para criar as tabelas
# Carregando o Flask em uma variável 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente de phyton que tem o nome do módulo atual

DB_NAME = "thegames" # Definindo o nome do banco de dados
#Passando o nome para o flask
app.config['DATABASE_NAME'] = DB_NAME

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost/{DB_NAME}' 

route.init_app(app) # chamando a função init_app do route.py e passando o app como argumento

# Iniciando o servidor web
if __name__ == '__main__':
    #Passando os dados e criando a conexão com o banco de dados
    connection = pymysql.connect(host='localhost',
                                 user = 'root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

#testando a conexão como banco de dados
    try:
        with connection.cursor() as cursor: #Cria o banco se ele não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Banco de dados '{DB_NAME}' criado ou já existe.")


    except Exception as error:
        print(f"Erro ao criar o banco de dados: {error}")
    finally:
        connection.close() #Fechando a conexão com o banco de dados

    app.run(debug=True) #Ligando modo de depuração, reinicia automático
# .run inicia um servidor
# verificando se o app.py for o arquivo principal, ele inicia o servidor

# Ctrl + " = abre o terminal
# python app.py + enter = running...ip(local)
# Ctrl + clicar no ip -> not found ( navegador)
# porta padrão no python -> :5000
# Ctrl + C -> parar o servidor
