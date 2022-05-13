import base64
import requests

# #印刷识别

# with open('words.jpg', 'rb') as r:
#     b64=base64.b64encode(r.read())
#     print(type(b64))
#     b64 = str(b64).split("'")[1]
# print(b64)
#
#
# data = {
# 'key':'6fa7a7302426dc1f861de855fc1c61e7',
# 'ImageBase64' : b64
# }
#
# res = requests.post(url='http://v.juhe.cn/generalaccurateOcr/index.php' ,data=data )
# print(res.text)




#机票
with open('flight.jpg','rb') as r:
    b64=base64.b64encode(r.read())

    b64 = str(b64).split("'")[1]

data = {
    'key':'982f26c0210a68de638294f49b97a28a',
    'ImageBase64': b64
}

res = requests.post(url='http://v.juhe.cn/flightinvoiceOcr/index',data=data )
print(res.text)

import shelve
shelve.open





