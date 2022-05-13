import zmail

mail_server = zmail.server(username='gzquse@163.com',
                           password='KXEXSFCZWFEIASLE',
                           pop_host='pop.163.com'
                           )
mymail = mail_server.get_latest()
zmail.show(mymail)
# #获取邮箱里的主体内容
print(mymail['Subject'], end="")
print(mymail['From'])
#
# #保存附件
zmail.save_attachment(mail=mymail, target_path=None, overwrite=True)
#
