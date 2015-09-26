mysql_config = {
    'dialect': 'mysql',
    'driver': 'pymysql',
    'username': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': '8889',
    'database': 'mandi',
}

CONNECTION_STRING = '%(dialect)s+%(driver)s://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s' % mysql_config

sample_user_data = [
    {'id': 1, 'username': 'ankur', 'name': 'ankur', 'password': 'ankur', 'phone_num': '3652314', 'email': 'ankur@gmail.com' },
]
