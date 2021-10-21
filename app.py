from flask import Flask, render_template

app = Flask("__name__", template_folder="scr/templates", static_folder="scr/static")

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
