from flask import Flask
from api.routes import api_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api_bp, prefix="/api")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)