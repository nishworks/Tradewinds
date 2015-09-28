from db import db_interface, Firm
from address import Addresses

class Firms(object):
	def __init__(self, userid, name):
		self.userid = userid
		self.name = name
		self.db_session = db_interface.new_session()
		self.instance = self.db_session.query(Firm).filter_by(user_id=self.userid,
			                                                  name=self.name).first()

	def addFirm(self, params):	
		if not self.instance:
			return str("Firm \'" + params['name'] + "\' already exists")
		address_id = Addresses().addAddress(params)
		if not address_id:
			return "Internal Error"	
		self.db_session = db_interface.new_session()	
		firm = Firm(market_licence=params['market_licence'], name=params['name'],
				tin_num=params['tin_num'], pan_num=params['pan_num'],
				tan_num=params['tan_num'], user_id=self.userid,
				address_id=address_id)
		try:
			self.db_session.add(firm)
			self.db_session.commit()
		except Exception,e:
			print e.args
			return "Internal Error"	
		return str("Firm \'"+ params['name'] + "\' added successfuly")	