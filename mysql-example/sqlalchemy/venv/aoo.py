from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()



class Union(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    unionname = Column('unionname', String, unique=True)



    engine = create_engine('mysql:///union.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    # creating our first user this code should be removed 
    # after script's first run
    
    union = Union()
    union.id = 0
    union.unionname = "SCCU"

    session.add(union)
    session.commit()

# all encompassing query that says give us every single user and print it.
    union = session.query(Union).all()
    for union in unions:
        print("Unions with Union Name= %s and id= %d"union.unionname, union.id)

    session.close()