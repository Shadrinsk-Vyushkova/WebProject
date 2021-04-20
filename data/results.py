import sqlalchemy
from .db_session import SqlAlchemyBase


class Result(SqlAlchemyBase):
    __tablename__ = "result"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    result = sqlalchemy.Column(sqlalchemy.String)
    type = sqlalchemy.Column(sqlalchemy.String)
    soc_type = sqlalchemy.Column(sqlalchemy.String)