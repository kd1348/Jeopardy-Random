from flask import Flask

def create_app():
    app = Flask(__name__) 
    from .jrandom import jrandom
    app.register_blueprint(jrandom)
    return app