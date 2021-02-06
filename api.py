from flask import Flask

app = Flask(__name__)

@app.route("/")
def hoje():
    return "Olá mundo!"

app.run(port=8080, debug=True)    