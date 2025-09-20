username = 'gary'
password = 'gary@123'

def authenticate():
  usr_name = input("Enter username: ")
  pwd = input("Enter password: ")

  if not usr_name == username:
    print('username does not exist')
    return
  elif not pwd == password:
    print('Incorrect password')
    return
  elif usr_name == username and pwd == password:
    print(f"Welcome {username}, you are logged in")
    return
  else:
    print('Some error occurred')
    return

authenticate()
