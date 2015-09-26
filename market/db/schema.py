from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, Index

Base = declarative_base()


class RevisionType(Base):
    __table__ = Table('revision_types', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('value', String(40), nullable=False),
                      mysql_engine='InnoDB',
                      )


class ResultType(Base):
    __table__ = Table('result_types', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('value', String(20), nullable=False),
                      mysql_engine='InnoDB',
                      )


class Revision(Base):
    __table__ = Table('revisions', Base.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('uuid', String(60), primary_key=True, unique=True),
                      Column('rb', Integer),
                      Column('start_time', DateTime),
                      Column('end_time', DateTime),
                      Column('revision_type', ForeignKey('revision_types.id')),
                      Column('product_revision_end', String(60)),
                      Column('execution_num', Integer),
                      Column('build_num', String(12)),
                      Column('result', ForeignKey('result_types.id')),
                      Column('submitter', String(40)),
                      Column('flags', String(60)),
                      Column('revert_revision_uuid', String(60), nullable=True),
                      Column('pre_commit_start_time', DateTime),
                      Column('pre_commit_end_time', DateTime),
                      Index('ix_uuid', 'uuid'),
                      Index('ix_start_time', 'start_time'),
                      Index('ix_pre_commit_start_time', 'pre_commit_start_time'),
                      mysql_engine='InnoDB'
                      )
