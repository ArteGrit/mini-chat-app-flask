from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints here
    from .routes import chat, users, health
    app.register_blueprint(chat.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(health.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
