#GET 방식요청
from urllib.parse import urlencode
from urllib.request import urlopen

#query = urlencode({'name':'둘리','a':10,'b':20})

f =urlopen('http://www.example.com')#+query)
response =f.read()
print(response)