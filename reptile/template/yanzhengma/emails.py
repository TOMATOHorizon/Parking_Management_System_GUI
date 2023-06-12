import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random


def email_yanzheng(user_email):
    def send_email(receiver, subject, content):
        sender = '1002626613@qq.com'
        password = 'cmtarmtlubvqbcad'

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = Header(sender)
        msg['To'] = Header(receiver)
        msg['Subject'] = Header(subject)

        try:
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(sender, password)
            server.sendmail(sender, [receiver], msg.as_string())
            server.quit()
            print('邮件发送成功')
            verify_code()
        except Exception as e:
            print('邮件发送失败', e)

    def generate_code():
        return ''.join(random.choice('0123456789') for i in range(6))

    def verify_code():
        user_code = input('请输入你收到的验证码：')
        if user_code == code:
            print('验证成功！')
            return True
        else:
            print('验证失败！')
            return False

    code = generate_code()

    receiver = f'{user_email}'  # 收件人邮箱地址
    subject = 'yanzhengma'  # 邮件主题
    content = '你的验证码是：' + code  # 邮件内容


    send_email(receiver, subject, content)  # 调用 send_email 函数发送邮件
