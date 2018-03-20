#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''邮件'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import requests, json

# 第三方 SMTP 服务
# mail_host = "smtp.mxhichina.com"  # 设置服务器
# mail_user = "account@wxnacy.com"  # 用户名
# mail_pass = "Wxnacy140111"  # 口令
#
# sender = 'account@wxnacy.com'
# receivers = ['371032668@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
# except smtplib.SMTPException as e:
#     print(e)


class Email():
    def __init__(self, host='smtp.mxhichina.com', user='account@wxnacy.com',
            password='Wxnacy140111', sender='account@wxnacy.com',
            sender_name='温总博客'):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(user, password)

            self.client = smtpObj
            self.sender = sender
            self.sender_name = sender_name
        except smtplib.SMTPException as e:
            print(e)

    def send(self, receivers, subject, message):
        message = MIMEText(message, 'html', 'utf-8')
        #  message['From'] = Header(self.sender_name, 'utf-8')
        message['To'] = Header('wen', 'utf-8')
        #  message['Cc'] = Header('wen', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        self.client.sendmail(self.sender, receivers, message.as_string())
        pass

    def send_attch(self, receivers, subject, message):
        message = MIMEMultipart()
        message['From'] = Header("菜鸟教程", 'utf-8')
        message['To'] =  Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain',
         'utf-8'))

        att1 = MIMEText(open('/Users/wxnacy/WebstormProjects/wxnacy.github.io/hexo/db.json', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        message.attach(att1)
        self.client.sendmail(self.sender, receivers, message.as_string())

    def send_image(self, receivers, subject, message):
        msgRoot = MIMEMultipart('parent')
        msgRoot['From'] = Header("菜鸟教程", 'utf-8')
        msgRoot['To'] =  Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgAlternative = MIMEMultipart('son')
        msgRoot.attach(msgAlternative)


        mail_msg = """
           <p>Hello World</p>
           <p><img src="cid:image1"></img></p>
           """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
        fp = open('/Users/wxnacy/WebstormProjects/wxnacy.github.io/hexo/source/images/httpie1.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

# 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        self.client.sendmail(self.sender, receivers, msgRoot.as_string())

class SendCloud():
    pass


if __name__ == '__main__':
    #  e = Email()
    e1 = 'info@gochinatv.com'
    e = Email(user=e1, password='Vegobeijing2017', sender=e1, sender_name=e1)
    emails = ['371032668@qq.com','18311233541@163.com',
            'wenxiaoning@gochinatv.com']
    e.send_image(emails,'邀请您','<div>欢迎您</div>')
    #  e.send_attch(emails,'邀请您','<div>欢迎您</div>')
    #  e.send(emails,'邀请您','<div>欢迎您</div>')

    url="http://api.sendcloud.net/apiv2/mail/send"

# 您需要登录SendCloud创建API_USER，使用API_USER和API_KEY才可以进行邮件的发送。
    #  params = {"apiUser": "wxnacy_test_n8D5XX", \
            #  "apiKey" : "qIfsR43BYe4W8635",\
            #  "from" : e1, \
            #  "fromName" : "wxnacy", \
            #  "to" : emails[0], \
            #  "subject" : "来自SendCloud的第一封邮件！", \
            #  "html": "你太棒了！你已成功的从SendCloud发送了一封测试邮件，接下来快登录前台去完善账户信息吧！", \
            #  }

    #  r = requests.post(url, files={}, data=params)
    #  print(r.text)
