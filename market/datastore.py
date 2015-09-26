from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import CONNECTION_STRING


class DataStore(object):

	def __init__(self):
		self.Base = automap_base()        
		self.engine = create_engine(CONNECTION_STRING)
		self.Base.prepare(self.engine, reflect=True)
		self.table=self.Base.classes
		self.session = Session(self.engine)

	def authenticate(self, params):
		User = self.table.user
		instance = self.session.query(User).filter_by(username=params['username']).first()
		if instance:
			if params['password'] == instance.password:
				return True, "Login Successful", instance.id
			return False, "Wrong password", None
		return False, "Wrong username", None		

	def addUser(self, params):
		try:
			User = self.table.user 
			instance = self.session.query(User).filter_by(username=params['username']).first()
			if instance:
				return False, "Username already taken"	
			self.session.add(User(username=params['username'],name=params['name'],password=params['password'],phone_num=params['phone'],email_id=params['email']))	
			self.session.commit()
			return True, "Registeration Successful"
		except Exception,e:
			print e.args	

