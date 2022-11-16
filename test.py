import urllib.parse
import httplib2

http = httplib2.Http()

url = 'https://xn--12c5cbudkbb0yh.com/meter/updatescript.php'   
body = {'id': 'foo', 'key1': 'bar'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(body))

print (response)