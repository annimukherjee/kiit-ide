from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'replace_with_random_secret_key'

    @app.route('/ping')
    def ping():
        return "Pong!"

    @app.route('/')
    def home():
        return "Hello, Flask! This is our code submission app."

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
