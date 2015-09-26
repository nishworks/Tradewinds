import os
import logging
import logging.handlers

from sqlalchemy.schema import CreateTable, DropTable
from sqlalchemy import create_engine
from sqlalchemy import orm

current_dir = os.path.dirname(os.path.realpath(__file__))

# Create log directory if not exists
LOG_DIR='../../logs/sqlalchemy'
if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

# create formatter and add it to the handlers
_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s',
                               '%Y-%m-%d %H:%M:%S')

# SqlAlchemy logging
_sqlalchemy = logging.getLogger('sqlalchemy')
_sqlalchemy.setLevel(logging.DEBUG)

_sql_h_fh = logging.handlers.RotatingFileHandler(os.path.join(current_dir, LOG_DIR, 'engine.log'), maxBytes=500000, backupCount=5)
_sql_h_fh.setLevel(logging.DEBUG)
_sql_h_fh.setFormatter(_formatter)

_sqlalchemy.addHandler(_sql_h_fh)
_sqlalchemy.debug('SqlAlchemy Logger initialized...')


class DbInterface:
    def __init__(self, db_url, base_object):
        self.engine = None
        self.Base = base_object
        self.connection = None
        self.create_engine(db_url)
        self.session_maker = orm.sessionmaker(bind=self.engine, autoflush=True, autocommit=False,
                                              expire_on_commit=True)
        self.scoped_session = orm.scoped_session(self.session_maker)

    @property
    def session(self):
        """
            This method returns an already created session
        """
        return self.scoped_session()

    def new_session(self):
        """
            This method returns a new session object which is a good idea
            if you want to do queries in parallel
        """
        return self.session_maker()

    def create_engine(self, db_url):
        print 'DB URL: %s' % db_url
        try:
            self.engine = create_engine(db_url)
        except Exception as e:
            print e
            print 'Could not create db engine'

    def connect(self):
        try:
            self.connection = self.engine.connect()
        except Exception as e:
            print 'Could not connect to the database'
            print e

    def execute_sql(self, query):
        self.connect()
        tx = self.connection.begin()
        try:
            # print 'Executing %s' % query
            rs = self.connection.execute(query)
            tx.commit()
        except:
            tx.rollback()
            # print 'Execution failed for %s' % query
            raise
        self.connection.close()
        return rs

    def setup_tables(self, delete_existing=False):
        """
            This method will create all the tables that are bound to 'BASE'
            in schema.py

        """
        self.Base.metadata.bind = self.engine
        if delete_existing:
            print 'Deleting existing tables...'
            self.Base.metadata.drop_all()
        print 'Creating tables...'
        self.Base.metadata.create_all(checkfirst=True, )
        print "Table creation done."

    def setup_table(self, table, delete_existing=False):
        self.Base.metadata.bind = self.engine
        if delete_existing:
            print 'Deleting existing table...'
            self.engine.execute(DropTable(table.__table__))
        print 'Creating table...'
        self.engine.execute(CreateTable(table.__table__))
        print "Table creation done."

    def populate_tables(self, table, table_data):
        """
        This method truncates the table and then populates it with the table_data
        :param table: sqlalchemy Table object
        :param table_data: List of dictionaries, each dictionary has table row
        :return:
        """
        self.connect()
        tx = self.connection.begin()
        try:
            self.connection.execute(table.__table__.delete())
            print 'Populating table %s...' % table.__name__
            self.connection.execute(table.__table__.insert(), table_data)
            tx.commit()
        except:
            tx.rollback()
            raise
