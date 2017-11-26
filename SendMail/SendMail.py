#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017.11.24

@author: MaserySen
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

def log(func):
    def wrapper(*arg,**kwarg):
        try:
            func(*arg,**kwarg)
        except Exception as e:
            print(e)
    return wrapper


addr_From = '19260817@angry.com'
password = 'Excited'
server = smtplib.SMTP()

#登陆邮箱，需要提供smtp地址，smtp的port，发件人邮箱，密码
@log
def login(addr_SMTP, port_SMTP, addr_From=addr_From, password=password):
    server.connect(addr_SMTP, port_SMTP)
    server.login(addr_From, password)

#发送邮件，需要提供收件人邮箱，主题，内容，附件（可选）
@log
def sendmail(addr_To,subject,content,addr_att=None):
    msg = MIMEMultipart()
    msg['From'] = addr_From.split('@')[0]+'<'+addr_From+'>'
    msg['To'] = addr_To.split('@')[0]+'<'+addr_To+'>'
    msg['Subject'] = Header(subject,  'utf-8')
    #装载附件
    if addr_att!=None:
        att = MIMEText( open(addr_att,'rb').read() , 'base64','utf-8' )
        att_name=os.path.basename(addr_att)
        att['Content-Type'] = 'application/octet=stream'
        att['Content-Disposition'] = 'attachment; filename=%s' % att_name.encode('utf-8')
    msg.attach( MIMEText(content,'plain','utf-8') )
    msg.attach( att )
    #发送邮件
    server.sendmail(addr_From , addr_To , msg.as_string())
    
if __name__=='__main__':
    login('smtp.angry.com',25)
    sendmail('Wallace@naive.com','Text','Hello,by Python','Greeting.txt')