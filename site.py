from flask import Flask, render_template

app = Flask(__name__)

#route --rota que desejo usar
@app.route('/home')
def home():
	nome = "Luna"
	posts = ["Flask I","Flask II","Flask III"]
	return render_template("index.html", nome=nome,posts=posts)

@app.route('/disciplina')
def disciplina():
	nome = "Luna"
	disc = {'progweb', 'matematica', 'portugues', 'fisica'}
	return render_template("disciplina.html", nome=nome,disc=disc)

@app.route('/aluno')
def aluno():
	nome = "Luna"
	aluno = {'ana', 'davylla', 'luna', 'bruno'}
	return render_template("aluno.htm")(nome=nome,aluno=aluno)

if __name__ == "__main__":
	app.run(debug=True)