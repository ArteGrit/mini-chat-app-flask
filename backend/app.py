from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)
    # CORS(app, origins=["https://lovable.dev"])
    # CORS(app, origins=[
    #     "https://lovable.dev",
    #     "https://3aa7b8c360c2.ngrok-free.app"
    # ])
    # Register blueprints here
    from .routes import chat, users, health
    app.register_blueprint(chat.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(health.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)
