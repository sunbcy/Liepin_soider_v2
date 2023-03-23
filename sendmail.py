import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header#,header
from email.utils import formataddr
import traceback
import os

class MailSender():
    def __init__(self) -> None:
        # 第三方SMTP服务
        self.mail_host='smtp.qq.com'#邮件服务器地址
        self.mail_user=''#发件人邮箱
        self.mail_pass=''# 填写邮箱授权码
        self.receivers=['saintbcy@163.com']

    def content(self,content=''):
        head="""
        <head>
        <title>MacBot1 Report Of {today}</title>
        </head>""".format(today=time.strftime('%Y%m%d'))
        body="""
        <body>
        <h1>老板:</h1>
        <p>下面是今天更新的内容:</p> 
        <p>{update_of_today}</p>
        </body>""".format(update_of_today=content)
        return """<html>{head}{body}</html>""".format(head=head,body=body)

    def SendMail(self,content='这是一个测试'):
        message=MIMEText(self.content(content),'html','utf-8')#style可以为plain(文本)/html(网页)
        message['From']=Header('Mac_Bot_1','utf-8')#formataddr(["Mac Bot",self.mail_user])#
        message['To']=formataddr(['Master B',self.receivers[0]])#Header('Master B','utf-8')

        subject='MacBot Report Of {today}'.format(today=time.strftime('%Y%m%d'))#邮件主题
        message['Subject']=Header(subject,'utf-8')
        try:
            smtpObj=smtplib.SMTP_SSL(self.mail_host,465)#smtplib.SMTP()非加密方式 25 /smtplib.SMTP_SSL()加密方式 465
            # smtpObj.connect()#
            smtpObj.login(self.mail_user,self.mail_pass)
            smtpObj.sendmail(self.mail_user,self.receivers,message.as_string())
            print('邮件发送成功!')
        except smtplib.SMTPException as e:
            print('Oops~邮件发送失败~~')
            
    def sendMail(self,senderName,to,cc,title,content,attachments=[]):
        senderUser=self.mail_user
        senderPassword=self.mail_pass
        smtpIp=self.mail_host
        smtpPort=465
        m=MIMEMultipart()
        try:
            htmlPart=MIMEText(content,'html','UTF-8')
            m.attach(htmlPart)
            m['Subject']=title
            if senderName and senderName!='':
                m['from']=Header(senderName,'UTF-8').encode()+'<%s>' %senderUser
            else:
                m['from']=senderUser
            m['To']='.'.join(to)
            m['Cc']='.'.join(cc)
            if attachments!=[]:
                for attachment in attachments:
                    obj=MIMEApplication(open(attachment,'rb').read())
                    obj['Content-type']="application/octet=stream"
                    obj.add_header('Content-Disposition','attachment',filename=("UTF-8","",attachment))
                    m.attach(obj)
            svr=smtplib.SMTP_SSL(host=smtpIp,port=smtpPort)
            svr.login(senderUser,senderPassword)
            svr.sendmail(senderUser,to+cc,m.as_string())
            svr.quit()
        except Exception:
            traceback.print_exc()
            print('[ERROR]发送邮件失败')
            return
        print('邮件已发送\n收件人{%s}\n抄送人{%s}\n' % (",".join(to),','.join(cc)))
        

if __name__=='__main__':
    mailsender=MailSender()
    # mailsender.SendMail('发送邮件时间:{}'.format(time.strftime('%Y%m%d %H:%M:%S')))
    
    mailsender.sendMail('MacBot',['saintbcy@163.com'],[],'test',mailsender.content('hhh'),attachments=[i for i in os.listdir() if not i.endswith('.py')])
