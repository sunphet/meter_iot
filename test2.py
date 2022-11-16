import requests

r = requests.post('http://xn--12c5cbudkbb0yh.com/meter/updatescript.php', data={'id': 123456789, 'key1':'value1', 'key2':'value2'})

print(r.text)