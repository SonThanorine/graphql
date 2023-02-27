from sqlmodel import SQLModel, Session, create_engine, select
from sqlalchemy.orm import joinedload
from models import Person, Organization

DB_FILE = 'database.db'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True, connect_args={"check_same_thread": False})

def create_tables():
    """Create the tables registered with SQLModel.metadata (i.e classes with table=True).
    More info: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """ Dependency function - yields Session object to FastAPI routes """
    with Session(engine) as session:
        yield session

def create_organization(titulo: str, pessoa_id: int):
    organization = Organization(titulo=titulo, pessoa_id=pessoa_id)

    with Session(engine) as session:
        session.add(organization)
        session.commit()
        session.refresh(organization)

    return organization

def get_organizations():
    query = select(Organization).options(joinedload('*'))
    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def create_person(idade: int, nome: str):
    person = Person(nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)

    return person

def get_people(
    id: int = None,
    idade: int = None,
    limit: int = 5,
):
    query = select(Person)

    if id:
        query = query.where(Person.id == id)
    if idade:
        query = query.where(Person.idade == idade)
    if limit:
        query = query.limit(limit)

    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result

if __name__ == '__main__':
    # creates the table if this file is run independently, as a script
    create_tables()