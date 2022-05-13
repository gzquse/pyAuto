import requests
import json
#先做登录

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
  'X-Requested-With':'XMLHttpRequest'
   }

params = {
'm': 'converged',
'a': 'comment',
'page': 1,
'pagesize': 20,
}

url = 'https://www.1905.com/api/content/index.php'

res = requests.get(url=url,params=params)
print(type(res.text))
# res = res.text.split('(')[-1].split(')')[0]
#
res = eval(res.text)
print(type(res))
print(res['info'])
for x in res['info']:
    print(x)
# print(res)
# print(type(res))