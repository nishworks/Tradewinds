from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, Index

Base = declarative_base()


class User(Base):
    __table__ = Table('user', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('username', String(15), nullable=False, unique=True),
                      Column('name', String(20), nullable=False),
                      Column('password', String(15), nullable=False),
                      Column('phone_num', Integer, nullable=False),
                      Column('email', String(20), nullable=False),
                      mysql_engine='InnoDB',
                      )

class Address(Base):
    __table__ = Table('address', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('street', String(20), nullable=True),
                      Column('city', String(20), nullable=True),
                      Column('district', String(15), nullable=True),
                      Column('state', String(20), nullable=True),
                      Column('email', String(20), nullable=True),
                      Column('phone_num', Integer, nullable=True),
                      mysql_engine='InnoDB',
                      )

class Firm(Base):
    __table__ = Table('firm', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(20), nullable=False),
                      Column('market_licence', String(30), nullable=False),
                      Column('tin_num', String(30), nullable=False),
                      Column('pan_num', String(30), nullable=False),
                      Column('tan_num', String(30), nullable=False),
                      Column('user_id', ForeignKey('user.id')),
                      Column('address_id', ForeignKey('address.id')),
                      mysql_engine='InnoDB',
                      )

class Account_type(Base):
    __table__ = Table('account_type', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('type', String(20), nullable=False),
                      Column('firm_id', ForeignKey('firm.id')),
                      mysql_engine='InnoDB',
                      )

class Account(Base):
    __table__ = Table('account', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(20), nullable=False),
                      Column('tin_num', String(30), nullable=False),
                      Column('pan_num', String(30), nullable=False),
                      Column('firm_id', ForeignKey('firm.id')),
                      Column('type_id', ForeignKey('account_type.id')),
                      Column('address_id', ForeignKey('address.id')),
                      mysql_engine='InnoDB',
                      )

class Transaction(Base):
    __table__ = Table('transaction', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('date', DateTime, nullable=False),
                      Column('amount', Integer, nullable=False),
                      Column('narration', String(30), nullable=False),
                      Column('firm_id', ForeignKey('firm.id')),
                      Column('debit_account', ForeignKey('account.id')),
                      Column('credit_account', ForeignKey('account.id')),
                      mysql_engine='InnoDB',
                      )

class Person(Base):
    __table__ = Table('person', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(20), nullable=False),
                      Column('firm_id', ForeignKey('firm.id')),
                      Column('account_id', ForeignKey('account.id')),
                      Column('address_id', ForeignKey('address.id')),
                      mysql_engine='InnoDB',
                      )

class Company(Base):
    __table__ = Table('company', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(20), nullable=False),
                      Column('firm_id', ForeignKey('firm.id')),
                      Column('account_id', ForeignKey('account.id')),
                      Column('address_id', ForeignKey('address.id')),
                      mysql_engine='InnoDB',
                      )
