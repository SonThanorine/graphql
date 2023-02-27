from typing import Optional, List
import strawberry
from strawberry.fastapi import GraphQLRouter
from database import (
    create_person, get_people, get_organizations, create_organization
)

@strawberry.type
class Organization:
    id: Optional[int]
    name: str
    sector: str
    people: List['Person']

@strawberry.type
class Person:
    id: Optional[int]
    first_name: str
    last_name: str
    age: int
    job_title: str
    Organization: Organization
    linkedin: str


@strawberry.type
class Query:
    all_pessoa: List[Person] = strawberry.field(resolver=get_people)
    all_organnizations: List[Organization] = strawberry.field(resolver=get_organizations)


@strawberry.type
class Mutation:
    create_pessoa: Person = strawberry.field(resolver=create_person)
    create_organizations: Organization = strawberry.field(resolver=create_organization)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)