import json

user = json.loads('{"id":100, "name": "홍길동"}')

# print('user name is' + user['name'])
print(f'username is {user["name"]}')

def userinfo(u):
  """사용자 정보를 상세히 보여

  Args:
      u (User): User Json Object

  Returns:
      String: User Information
  """
  id  = u["id"]
  name = u["name"]
  return f'Id is {id}, Name is {name}'

print(f'User Information: {userinfo(user)}')


