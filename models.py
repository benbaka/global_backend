from sqlalchemy import Column, Integer, String
from database import Base

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(50) )
    description = Column(String(120))

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return f'<Todo {self.title!r}>'