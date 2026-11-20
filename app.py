import os
import pymysql
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)


def conexao_db():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5,
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")

        conexao = conexao_db()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO contatos (email, mensagem) VALUES (%s, %s)",
                (email, mensagem),
            )
            conexao.commit()
        finally:
            conexao.close()

        return render_template("contato.html", enviado=True)
    return render_template("contato.html", enviado=False)


@app.route("/listar")
def listar():
    conexao = conexao_db()
    try:
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, email, mensagem, criado_em FROM contatos ORDER BY id DESC")
        contatos = cursor.fetchall()
    finally:
        conexao.close()

    return render_template("listar.html", contatos=contatos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
