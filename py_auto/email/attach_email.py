# smtplib #smtp协议库 发送靠他
# email #生成邮件的库 具体的内容


from email.mime.multipart import MIMEMultipart  # 多个部件组装
from email.header import Header  # 邮件头部 标题 收件人等
from email.mime.text import MIMEText  # 邮件文字

from email.mime.application import MIMEApplication

from smtplib import SMTP_SSL  # 安全加密类似https/http

# 先定义好发件人的邮箱地址和密码
user = 'gzquse@163.com'
pwd = 'KXEXSFCZWFEIASLE'  # 'wanmen123123'

# 目标收件人的邮箱地址
target_mail = 'gzquse@163.com'

# 然后定义好我们要使用的邮箱服务
email_server = 'smtp.163.com'

# 定义并读取附件
attchment_file = MIMEApplication(open('myfile1111.txt','rb').read())
attchment_file.add_header('Content-Disposition','attchment', filename='myfile1111.txt')

# 构造 html内容
html_content = '''
<html>
    <h1 style="color:blue;margin-left:20px"> 万门大学欢迎你！ </h1>
    <p >欢迎加入我们这个教育的大家庭</p>
    <p>让知识改变人生！</p>
    <a href = "https://www.wanmen.org">更多好课请关注万门大学</a>
    <p><img style = "width:100px" src='https://imgs.wanmen.org/3c8db5220d7cf0dc7b6ef81f524fea60.png'></p>
</html>
'''

# 建立邮件
# 组合邮件元素到一个主体中
mail = MIMEMultipart()  # 实例化一个对象 -邮件部件组合对象
mail['Subject'] = Header('来自万门大学Python自动化的一封信','utf-8')  # 邮件显示内容
mail['From'] = Header('来自正正老师', 'utf-8')  # 邮件显示内容
mail['To'] = target_mail  # 邮件显示内容
mail['CC'] = 'abc@aaa.com,ccc@ccc.com'  # 邮件显示内容

mail.attach(MIMEText(html_content, 'html','utf-8'))  # 邮件显示内容
mail.attach(attchment_file)

# 邮件服务器调用发送
smtp = SMTP_SSL(email_server)  # 实例化 对象 带入服务器地址
smtp.login(user,pwd)  # 登录
smtp.sendmail(from_addr=user,to_addrs=target_mail,msg=mail.as_string())  # 操作发送
smtp.quit()  # 完成发送
