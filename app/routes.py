from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Professor, Disciplina, Curso

@app.route('/')
def index():
    return render_template('index.html')

# --- Professores ---

@app.route('/professores')
def listar_professores():
    professores = Professor.query.all()
    return render_template('professores.html', professores=professores)

@app.route('/professor/novo', methods=['GET', 'POST'])
def novo_professor():
    if request.method == 'POST':
        nome = request.form['nome']
        departamento = request.form['departamento']
        novo = Professor(nome=nome, departamento=departamento)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('listar_professores'))
    return render_template('novo_professor.html')

# --- Disciplinas ---

@app.route('/disciplinas')
def listar_disciplinas():
    disciplinas = Disciplina.query.all()
    return render_template('disciplinas.html', disciplinas=disciplinas)

@app.route('/disciplina/nova', methods=['GET', 'POST'])
def nova_disciplina():
    if request.method == 'POST':
        nome = request.form['nome']
        nova = Disciplina(nome=nome)
        db.session.add(nova)
        db.session.commit()
        return redirect(url_for('listar_disciplinas'))
    return render_template('nova_disciplina.html')

# --- Cursos ---

@app.route('/cursos')
def listar_cursos():
    cursos = Curso.query.all()
    return render_template('cursos.html', cursos=cursos)

@app.route('/curso/novo', methods=['GET', 'POST'])
def novo_curso():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        novo = Curso(nome=nome, tipo=tipo)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('listar_cursos'))
    return render_template('novo_curso.html')
