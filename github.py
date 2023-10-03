# Acesso a API do Github
# Python Requests Docs: http://docs.python-requests.org/en/master/

import requests
url = 'https://api.github.com/users/carlosbazilio'
dados = requests.get(url)
print (dados.content)
