from database import engine
from models import Person, Organization
from sqlmodel import Session, select

def populate():
    with Session(engine) as session:
        organizations = [
            {'id': 1, 'name': 'Itau', 'sector': 'Financeiro'},
            {'id': 2, 'name': 'Ame', 'sector': 'Varejo'},
            {'id': 3, 'name': 'GoAhead', 'sector': 'Servicos'}
        ]
        
        for organization in organizations:
            session.add(Organization(**organization))
        
        session.commit()
        
        itau = session.exec(
            select(Organization).where(Organization.name == 'Itau')
        ).first()

        ame = session.exec(
            select(Organization).where(Organization.name == 'Ame')
        ).first()

        goahead = session.exec(
            select(Organization).where(Organization.name == 'GoAhead')
        ).first()

        # add employees
        people = [
            {
                'id': 1, 
                'first_name': 'Pedro', 
                'last_name': 'Souza', 
                'age': 28, 
                'job_title': 'Cloud Engineer',
                'organization_id': goahead.id,
                'linkedin': 'https://www.linkedin.com/in/pedro-souza-340322123/'

            },
            {
                'id': 2, 
                'first_name': 'Marden', 
                'last_name': 'Lellis', 
                'age': 8, 
                'job_title': 'Coordenador de Engenharia de TI',
                'organization_id': itau.id,
                'linkedin': 'https://www.linkedin.com/in/marden-lelis-00487221/'

            },
            {
                'id': 3, 
                'first_name': 'Wendell', 
                'last_name': 'Barcellos', 
                'age': 8, 
                'job_title': 'SRE',
                'organization_id': ame.id,
                'linkedin': 'https://www.linkedin.com/in/wendell-barcellos/'

            }
        ]

        for person in people:
            session.add(Person(**person))
            session.commit()

if __name__ == '__main__':
    # creates the table if this file is run independently, as a script
    populate()