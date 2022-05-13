# smtplib #smtp协议库 发送靠他
# email #生成邮件的库 具体的内容


from email.mime.multipart import MIMEMultipart  # 多个部件组装
from email.header import Header  # 邮件头部 标题 收件人等
from email.mime.text import MIMEText  # 邮件文字

from smtplib import SMTP_SSL  # 安全加密类似https/http

# 先定义好发件人的邮箱地址和密码

user = 'gzquse@163.com'
pwd = 'KXEXSFCZWFEIASLE'  # 'wanmen123123'
# 目标收件人的邮箱地址
target_mail = 'gzquse@163.com'
# 然后定义好我们要使用的邮箱服务
email_server = 'smtp.163.com'
# 建立邮件

# 组合邮件元素到一个主体中
mail = MIMEMultipart()  # 实例化一个对象 -邮件部件组合对象

mail['Subject'] = Header('来自GZQPython自动化的一封信', 'utf-8')  # 邮件显示内容
mail['From'] = Header('来自GZQ', 'utf-8')  # 邮件显示内容
mail['To'] = target_mail  # 邮件显示内容
mail['CC'] = 'abc@aaa.com,ccc@ccc.com'  # 邮件显示内容

mail.attach(MIMEText('你好 我是GZQ！欢迎你的加入！', 'plain', 'utf-8'))  # 邮件显示内容

# 邮件服务器调用发送
smtp = SMTP_SSL(email_server)  # 实例化 对象 带入服务器地址
smtp.login(user, pwd)  # 登录
smtp.sendmail(from_addr=user,to_addrs=target_mail,msg=mail.as_string())  # 操作发送
smtp.quit()  # 完成发送
