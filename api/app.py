from flask import Flask, app, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("paginainicial.html")

@app.route("/sobremim")
def sobremim():
    return render_template("sobre_mim.html")

@app.route("/curriculo")
def curriculo():
    return render_template("trabalhos.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

if __name__ == '__main__':
    app.run(debug = True, port = 5000)