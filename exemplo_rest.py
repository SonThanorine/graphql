from fastapi import FastAPI, Request, Depends
from database import get_session
from models import Person, Organization
from sqlmodel import select, Session


app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Bem Vindo!'}


@app.get('/pessoas')
def get_pessoa(request: Request, session: Session = Depends(get_session)):
    query = select(Person)
    result = session.execute(query).scalars().all()
    response = {}

    for person in result:
        response[person.id] = {"First_Name": person.first_name, "Last_Name": person.last_name, "Age": person.age, "Job_Title": person.job_title, "Organnization_Name": person.organization.name, "Linkedin_Profile": person.linkedin}

    return response

@app.get('/organizacoes')
def get_pessoa(request: Request, session: Session = Depends(get_session)):
    query = select(Organization)
    result = session.execute(query).scalars().all()
    response = {}

    for organization in result:
        response[organization.id] = {"Organization_Name": organization.name, "Sector": organization.sector}

    return response


# @app.get('/pessoa-nome')
# def get_pessoa():
#     query = select(Pessoa.nome)
#     with Session(engine) as session:
#         result = session.execute(query).scalars().all()

#     return result


# @app.get('/pessoa/{pessoa_nome}')
# def get_pessoa(pessoa_nome: str):
#     with Session(engine) as session:
#         statement = select(Pessoa).where(Pessoa.nome == pessoa_nome)
#         result = session.execute(statement)
#         pessoa = result.one_or_none()
#         if pessoa is None:
#             return {"error": "Pessoa não encontrada"}
#         return {"id": pessoa.Pessoa.id, "nome": pessoa.Pessoa.nome, "sobrenome": pessoa.Pessoa.sobrenome, "idade": pessoa.Pessoa.idade, "profissao": pessoa.Pessoa.profissao, "linkedin": pessoa.Pessoa.linkedin}