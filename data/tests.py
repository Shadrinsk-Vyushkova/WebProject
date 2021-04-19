import sqlalchemy
from .db_session import SqlAlchemyBase


class Test(SqlAlchemyBase):
    __tablename__ = "tests"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    test = sqlalchemy.Column(sqlalchemy.String)
    var1 = sqlalchemy.Column(sqlalchemy.String)
    var2 = sqlalchemy.Column(sqlalchemy.String)