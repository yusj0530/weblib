#POST 방식요청

from urllib.parse import urlencode
from urllib.request import Request, urlopen

data = urlencode({'name':'둘리','a':10,'b':20})
data = data.encode('UTF-8')

request = Request('http://www.example.com/join', data)
request.add_header('Content-Type', 'text/html')

f=urlopen(request)
response = f.read()

print(response)