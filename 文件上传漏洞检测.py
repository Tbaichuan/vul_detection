
```
import requests

target_url = 'http://example.com/upload.php'
files = {'file': open('test.txt', 'rb')}

response = requests.post(target_url, files=files)

if response.status_code == 200 and 'uploaded' in response.text:
    print('文件上传漏洞存在！')
else:
    print('文件上传漏洞不存在！')
```
