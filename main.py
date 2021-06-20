from flask import Flask
from database import db_session, engine
from sqlalchemy import insert
from models import Todo
from flask import jsonify
DATABASE = '/tmp/test.db'

app = Flask(__name__)

@app.route('/')
def hello():
    todo = Todo()
    stmt = insert(Todo.__table__).values(title='spongebob', description="Spongebob Squarepants")

    con = engine.connect()
    con.execute(stmt)
    print(Todo.query.all())
    all = [{'title':i.title, 'description':i.description} for i in Todo.query.all()]

    return jsonify(all)
