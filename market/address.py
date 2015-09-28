from db import db_interface, Address

class Addresses(object):
	def __init__(self):
		self.db_session = db_interface.new_session()
		
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