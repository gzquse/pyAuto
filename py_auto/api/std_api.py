import requests
import json
# 新闻
param = {
 'key':'42149ae7e1d7576f361d9bb0588cbf1',
 'type':'shehui'
}
res = requests.get(url='http://v.juhe.cn/toutiao/index' ,params=param )
# print(type(res.text))
# print(res.text)
# my_res = json.loads(res.text)
# print(my_res['result']['data'])
# for info in my_res['result']['data']:
#     print(info)



#天气预报


param = {

 'APPsecret':'01ec378e6fea5487ac56f403b9745721',
 'cityname':'上海'

}
res = requests.get(url='http://v.juhe.cn/weather/index?key=01ec378e6fea5487ac56f403b9745721&cityname=西安' )
print(type(res.text))
my_res = json.loads(res.text)
print(my_res['result'])






