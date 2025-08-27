from flask import Flask
from routes import main_bp, api_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(main_bp)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)
