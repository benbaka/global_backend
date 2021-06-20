from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os, sys
engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    try:
        action = sys.argv[1]
    except:
        action = ""
    if action =="reset":
        if os.path.exists("/tmp/test.db"):
            os.remove("/tmp/test.db")

    import models
    Base.metadata.create_all(bind=engine)

init_db()