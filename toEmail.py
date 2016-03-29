#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText  
from email.utils import parseaddr, formataddr #解析email
import smtplib

class Email():
    def __init__(self, from_addr, from_pass, from_user, from_server, to_addr, to_user, encode = 'utf-8', ):
        self.encode = encode
        self.from_addr = from_addr
        self.from_pass = from_pass
        self.from_user = from_user
        self.from_server = from_server
        self.to_addr = to_addr
        self.to_user = to_user

    def formates(self,s):
        name,addr = parseaddr(s)
        return formataddr((Header(name, self.encode).encode(),addr))

    def editor(self, subject = '无主题', word = '无内容', type = 'text'):
        msg = MIMEText(word, type, self.encode)
        msg['From'] = self.from_user + ' ' + self.formates(u'<%s>' %( self.from_addr))
        msg['To'] = self.to_user + ' ' + self.formates(u'<%s>' %(self.to_addr))
        msg['Subject'] = Header(subject, 'utf-8').encode()
        return msg

    def login(self):
        try:
            self.smtp = smtplib.SMTP(self.from_server, 25)
            self.smtp.starttls()
            self.smtp.set_debuglevel(1)
            if self.smtp.login(self.from_addr, self.from_pass):
                return True
            else:
                return False
        except:
            print('验证异常')

    def send(self, msg):
        try:
            if self.login(): 
                print('登录成功')
                self.smtp.sendmail(self.from_addr, self.to_addr, msg.as_string())
            else:
               print('登录失败')
        except:
            print('发送异常')
        finally:
            self.smtp.quit()
def index():

    from_addr = 'zcyazx@163.com'
    from_pass = 'zcy.304907240'
    from_user = 'MyPyhton'
    from_server = 'smtp.163.com'
    to_addr = '304907240@qq.com'
    to_user = '毛毛雨'

    from_subject = 'MyPyhton'
    from_content = "我的第一个stmp邮件"

    email = Email(from_addr, from_pass, from_user, from_server, to_addr, to_user, 'utf-8')
    email.send(email.editor(from_subject, from_content, 'html'))
    
if __name__ == '__main__':
    index()