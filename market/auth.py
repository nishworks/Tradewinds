from db import db_interface, User


class AuthUser(object):

	def __init__(self, username):
		self.username = username
		self.db_session = db_interface.new_session()
		self.instance = self.db_session.query(User).filter_by(username=username).first()

	@property
	def exists(self):
		return self.instance is not None

	def authenticate(self, password):
		if not self.exists:
			return None
		print '%s : %s' % (password, self.instance.password)
		if password == self.instance.password:
			return self.instance.id
		return None

	def addUser(self, params):
		if self.exists:
			return False
		user = User(username=self.username, name=params['name'],
					password=params['password'], phone_num=params['phone'],
					email=params['email'])
		try:
			self.db_session.add(user)
			self.db_session.commit()
		except Exception,e:
			print e.args
			return False
		return True
