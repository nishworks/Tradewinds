from db import db_interface, User, Firm, Address


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
			print user.id
			self.db_session.commit()
		except Exception,e:
			print e.args
			return False	
		return True

	def addFirm(self, params):	
		user_id=self.instance.id
		self.firm_instance=self.db_session.query(Firm).filter_by(user_id=user_id,
			                                                     name=params['name']).first()	
		if self.firm_instance is not None:
			return str("Firm \'" + params['name'] + "\' already exists")
		address_id = self.addAddress(params)
		if not address_id:
			return "Internal Error"	
		self.db_session = db_interface.new_session()	
		firm = Firm(market_licence=params['market_licence'], name=params['name'],
				tin_num=params['tin_num'], pan_num=params['pan_num'],
				tan_num=params['tan_num'], user_id=user_id,
				address_id=address_id)
		try:
			self.db_session.add(firm)
			self.db_session.commit()
		except Exception,e:
			print e.args
			return "Internal Error"	
		return str("Firm \'"+ params['name'] + "\' added successfuly")

	def addAddress(self, params):
		address = Address(street=params['street'], city=params['city'],
					      district=params['district'], phone_num=params['phone'],
					      state=params['state'],email=params['email'])
		try:
			self.db_session.add(address)
			self.db_session.commit()
		except Exception,e:
			print e.args
			return False	
		return address.id	


