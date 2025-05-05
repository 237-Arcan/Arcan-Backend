from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return "Bienvenue sur ton serveur Flask PRO !"
