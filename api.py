from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        return "Você está acessando via outro verbo!"

@app.route("/<int:id>")
def Home_id(id):
    return str(id + 1)

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")


app.run(port=8080, debug=True)    