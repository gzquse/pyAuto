import requests
import re

url = 'https://www.1905.com/pinglun/?fr=homepc_menu_cmt'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
res = requests.get(url=url,headers = headers )
res.encoding='utf-8'
# #
# print(res.text)
#
patt = '<a href="(.*?)" data-hrefexp=".*?" title="(.*?)" class="list-imgs" target="_blank">'
#
result = re.findall(pattern=patt,string=res.text)
print(result)
print(len(result))