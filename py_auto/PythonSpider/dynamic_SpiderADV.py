import requests
import json

# 先做登录
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'https://mice.mofyi.com/user/login/dologin.html'

data = {
    'username': '18301017108',
    'password': 'Gao123123',
}

sess = requests.Session()
login = sess.post(url=url, data=data, headers=headers)

url_user = 'https://mice.mofyi.com/major/form/ajaxGetPeopleList'

data = {
    'form_id': 200414,
    'search': '',
    'review': '',
    'page': 7,
    'pagesize': 10,
}

result = sess.post(url=url_user, data=data, headers=headers)
print(type(result.text))
res = json.loads(result.text)  # dict to json  json.dumps(resut)
print(res['data'])
print(type(res))
