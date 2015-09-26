from interface import DbInterface
from schema import *
from config import *


# It's a good idea to just have one object of db_interface
db_interface = DbInterface(CONNECTION_STRING, Base)

def setup_and_populate_tables():
    db_interface.setup_tables(delete_existing=True)
    db_interface.populate_tables(User, sample_user_data )

# For setting up one table
# db_interface.setup_table(PublishedArtifact, delete_existing=True)

    