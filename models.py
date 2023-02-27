from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int
    job_title: str
    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")
    organization: Optional["Organization"] = Relationship(back_populates='people')
    linkedin: str

class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    sector: str
    people: List["Person"] = Relationship(back_populates='organization')