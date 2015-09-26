from market import db

if __name__ == '__main__':
    print 'This execution will truncate the whole database and recreate tables.'
    print 'Are you sure you want to do this?'
    print "Please type 'I understand' if you want to continue."
    user_input = raw_input('>')
    if user_input == 'I understand':
        db.setup_and_populate_tables()
    else:
        print 'Well run this script again if you want to truncate database.'
