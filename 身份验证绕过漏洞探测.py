
```
import requests

target_url = 'http://example.com/admin'
payload = {'username': 'admin', 'password': '123456'}

response = requests.post(target_url, data=payload)

if response.status_code == 200 and 'admin panel' in response.text:
    print('身份验证成功！')
else:
    print('身份验证失败！')
```
