from flask import Flask
from app import routes

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

