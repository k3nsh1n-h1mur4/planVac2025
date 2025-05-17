from datetime import datetime
from decouple import config
import psycopg2
from sqlalchemy import ForeignKey, func, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from flask_sqlalchemy import SQLAlchemy

USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
PORT = config('PORT')

engine = create_engine('postgresql+psycopg2://postgres:Z4dk13l2017**@localhost/planvac2025', echo=True)

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    createdat: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class WrokerModel(db.Model):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    app: Mapped[str] = mapped_column(nullable=False)
    apm: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    edad: Mapped[int] = mapped_column(nullable=False)
    matricula: Mapped[str] = mapped_column(nullable=False)
    adscripcion: Mapped[str] = mapped_column(nullable=False)
    horario: Mapped[str] = mapped_column(nullable=False)
    categoria: Mapped[str] = mapped_column(nullable=False)
    n_afil: Mapped[str] = mapped_column(nullable=False)
    calle: Mapped[str] = mapped_column(nullable=False)
    no: Mapped[str] = mapped_column(nullable=False)
    colonia: Mapped[str] = mapped_column(nullable=False)
    cp: Mapped[str] = mapped_column(nullable=False)
    mcpio: Mapped[str] = mapped_column(nullable=False)
    tel_t: Mapped[str] = mapped_column(nullable=False)
    tel_p: Mapped[str] = mapped_column(nullable=False)
    tel_c: Mapped[str] = mapped_column(nullable=False)
    createdat: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)


class CModel(db.Model):
    __tablename__ = 'children'

    id: Mapped[int] = mapped_column(primary_key=True)
    app: Mapped[str] = mapped_column(nullable=False)
    apm: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    parentesco: Mapped[str] = mapped_column(nullable=False)
    telefono: Mapped[str] = mapped_column(nullable=False)
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"), nullable=False)
    createdat: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False)