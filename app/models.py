from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# Associação Professor <-> Disciplina
professor_disciplina = db.Table('professor_disciplina',
    db.Column('professor_id', db.Integer, db.ForeignKey('professor.id'), primary_key=True),
    db.Column('disciplina_id', db.Integer, db.ForeignKey('disciplina.id'), primary_key=True)
)

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    disciplinas = db.relationship('Disciplina', secondary=professor_disciplina, back_populates='professores')
    atribuicoes = db.relationship('Aula', back_populates='professor')

class Disciplina(db.Model):
    __tablename__ = 'disciplina'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    professores = db.relationship('Professor', secondary=professor_disciplina, back_populates='disciplinas')
    cursos_assoc = db.relationship("CursoDisciplina", back_populates="disciplina")
    aulas = db.relationship("Aula", back_populates="disciplina")

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    disciplinas_assoc = db.relationship("CursoDisciplina", back_populates="curso")
    aulas = db.relationship("Aula", back_populates="curso")

class CursoDisciplina(db.Model):
    __tablename__ = 'curso_disciplina'
    id = db.Column(db.Integer, primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)

    curso = db.relationship("Curso", back_populates="disciplinas_assoc")
    disciplina = db.relationship("Disciplina", back_populates="cursos_assoc")

class Aula(db.Model):
    __tablename__ = 'aula'
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    horas = db.Column(db.Integer, nullable=False)

    professor = db.relationship("Professor", back_populates="atribuicoes")
    curso = db.relationship("Curso", back_populates="aulas")
    disciplina = db.relationship("Disciplina", back_populates="aulas")