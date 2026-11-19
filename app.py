from flask import Flask, render_template, request

app = Flask(__name__)


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
        print(email, mensagem)
        return render_template("contato.html", enviado=True)
    return render_template("contato.html", enviado=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



#def conexao_db():
#    return pymysql.connect(
#    host="ip_publico_maquina_db",
#   user="usuario!=root//root_acessa_local",
#	password="senha_usuário",
#	port=3306,
#	database="nome_do_banco",
#	cursorclass=pymysql.cursors.DictCursor (formatação de tipo de dados, retorna dicionário),
#	connect_timeout=5
#    )
