from http.client import HTTPConnection

#1.연결
connenction = HTTPConnection('www.example.com')

#2. 요청보내기
connenction.request('GET', '/')

#3. 응답 받기
response = connenction.getresponse()
print(response.status, response.reason)

#4. Body 읽어오기
body = response.read()
print(body)

#404 에러 받아보기
#에러 받아보기
connenction.request('GET', '/babo.html')
response = connenction.getresponse()
print(response.status, response.reason)