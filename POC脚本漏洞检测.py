```
import requests

target_url = 'http://example.com'
payload = '/phpinfo.php'

url = target_url + payload
response = requests.get(url)

if response.status_code == 200 and 'phpinfo' in response.text:
    print('漏洞存在！')
else:
    print('漏洞不存在！')
```