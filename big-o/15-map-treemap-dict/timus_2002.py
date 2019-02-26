class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.isLoggedIn = False


# database
db = {}

for _ in range(int(input())):
  cmd = input().split()
  username = cmd[1]

  if cmd[0] == 'register':
    if username in db:
      print('fail: user already exists')
    else:
      db[username] = User(username, cmd[2])
      print('success: new user added')
  elif cmd[0] == 'login':
    if username not in db:
      print('fail: no such user')
    elif db[username].password != cmd[2]:
      print('fail: incorrect password')
    elif db[username].isLoggedIn == True:
      print('fail: already logged in')
    else:
      db[username].isLoggedIn = True
      print('success: user logged in')

  elif cmd[0] == 'logout':
    if username not in db:
      print('fail: no such user')
    elif db[username].isLoggedIn == False:
      print('fail: already logged out')
    else:
      db[username].isLoggedIn = False
      print('success: user logged out')
  else:
    raise Error('Non-supported command')
