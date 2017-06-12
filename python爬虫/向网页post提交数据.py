import requests
dic = {'key1':'value1', 'key2':'value2'}
r = requests.post("http://httpbin.org/post", data = dic)
r.encoding = r.apparent_encoding
print (r.text)

