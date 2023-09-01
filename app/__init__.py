from flask import Flask

app = Flask(__name__)

from app import routes  # Importando as rotas do pacote 'app'
