import getpass


def check_user(user, password):
    if user == 'luofangbing' and password == '1234':
        print('UserName:%s;Password:%s' % (user, password))
        return True
    else:
        return False


op = True
while __name__ == "__main__" and op:
    usr = getpass.getuser()
    pwd = getpass.getpass('Enter your password:')
    if check_user(usr, pwd):
        print('OK')
        op = False
    else:
        print('ERROR and try again')
