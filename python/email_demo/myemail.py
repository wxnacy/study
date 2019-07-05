#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 发送邮件

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import traceback

class Email():
    def __init__(self, smtp_host, smtp_port, user, password, sender,
            sender_name, **kwargs):
        kw = locals()
        kw.pop('self')
        for k, v in kw.items():
            setattr(self, k, v)

    def connect(self):
        '''建立连接'''
        try:
            smtpObj = smtplib.SMTP()
            #  smtpObj.set_debuglevel(1)
            smtpObj.connect(self.smtp_host, self.smtp_port)
            smtpObj.login(self.user, self.password)

            self.client = smtpObj
            self.sender = self.sender
            self.sender_name = self.sender_name
        except smtplib.SMTPException as e:
            traceback.print_exc(e)

    def send(self, receivers,  subject, message, maintype='plain', cc=[]):
        '''
        发送邮件
        '''
        self.connect()
        message = MIMEText(message, maintype, 'utf-8')
        message['From'] = Header(self.sender_name, 'utf-8')
        message['To'] = Header(','.join(receivers), 'utf-8')
        if cc:
            message['Cc'] = Header(','.join(cc), 'utf-8')
        #  message['Bcc'] = Header(','.join(receivers), 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        receivers.extend(cc)
        try:
            self.client.sendmail(self.sender, receivers,
                message.as_string())
            self.client.quit()
            return True
        except Exception as e:
            traceback.format_exc(e)
            self.client.quit()
            return False

if __name__ == '__main__':
    # 以阿里邮箱为例
    smtp_host = 'smtp.mxhichina.com'    # smtp 地址
    smtp_port = 25                      # smtp 端口
    user = '<send_email>'               # 发送方邮箱
    password = '<send_email_password>'  # 发送方密码
    sender = '<send_email>'             # 发送方邮箱
    sender_name = '<send_name>'         # 发送方名称

    e = Email(**locals())
    receivers = ['<rece_email']         # 接收方邮箱
    subject = '主题'
    msg = '信息'
    e.send(receivers, subject, msg)

