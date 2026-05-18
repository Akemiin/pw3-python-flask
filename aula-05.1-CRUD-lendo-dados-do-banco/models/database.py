
# pip install pymysql # Permite a conexão com o banco de dados MSQL
# # pip install flask-sqlalchemy# Permite a crição dos models

from flask_sqlalchemy import SQLAlchemy # importando o SQLAlchemy
db = SQLAlchemy() # Criando a instância do SQLAlchemy

# Criando a classe para representar a entidade "Games" no banco de dados(tabela = games)
class Game(db.Model):
    id= db.Column(db.Integer, primary_key=True) # id é a chave primária da tabela
    titulo= db.Column(db.String(100)) # Título do jogo
    ano= db.Column(db.Integer) # Ano de lançamento
    categoria= db.Column(db.String(50)) # Categoria do jogo
    plataforma= db.Column(db.String(50)) # Plataforma do jogo
    preco= db.Column(db.Float) # Preço do jogo
    quantidade= db.Column(db.Integer) # Quantidade em estoque
    
    #Método construtor ( atributos da class que serão utilizados pelos objetos)
    def __init__(self,titulo,ano,categoria,plataforma,preco,quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade    
        