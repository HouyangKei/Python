'''
Created on 2018年8月22日
SMTP发送邮件
@author: hy
'''
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage


my_sender = '1028430719@qq.com'    # 发件人邮箱账号
my_pass = 'dxnmdlbaawpvbbje'              # 发件人邮箱密码
my_user = '257212404@qq.com'      # 收件人邮箱账号，我这边发送给自己


def email():
    try:
        con = """
            <p>Python 邮件发送测试...</p>
            <p><a href="http://www.runoob.com">这是一个链接</a></p>
            """
        # 创建消息容器
        msg = MIMEMultipart()
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["侯杨", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["收件人", my_user])
        # 邮件的主题，也可以说是标题
        msg['Subject'] = "HTML邮件"
        # html：网页   plain：文本 base64:文件
        msg.attach(MIMEText(con, 'html', 'utf-8'))
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("邮件发送失败")


def emailFiLe():
    # 创建消息容器
    msg = MIMEMultipart()
    # 发件人邮件昵称
    msg["From"] = Header("小仙女", 'utf-8')
    # 收件人昵称
    msg["To"] = Header("大坏蛋", 'utf-8')
    # 邮件标题
    msg["Subject"] = "带附件的Email"
    # 设置正文内容
    msgcon = "带附件的Email正文哦"
    msg.attach(MIMEText(msgcon, "plain", "utf-8"))
    # 构造附件
    file = MIMEApplication(open(r"D:\\data\\7-16-青岛.xls", "rb").read())
    basename = "7-16-青岛.xls"
    file.add_header(
        'Content-Disposition', 'attachment', filename=('gbk', '', basename))
    msg.attach(file)

    try:
        # 创建服务 发件人邮箱中的SMTP服务器
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, my_user, msg.as_string())
        # 关闭连接
        server.quit()
        print("发送成功")
    except Exception as e:
        print("发送失败" + e)


def emailImg():
    # 邮件类型为"multipart/alternative"的邮件包括纯文本正文（text/plain）和超文本正文（text/html）。
    # 邮件类型为"multipart/related"的邮件正文中包括图片，声音等内嵌资源。
    # 邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型。
    # 创建消息容器
    msg = MIMEMultipart("related")
    # 发件人邮件昵称
    msg["From"] = Header("小仙女", 'utf-8')
    # 收件人昵称
    msg["To"] = Header("大坏蛋", 'utf-8')
    # 邮件标题
    msg["Subject"] = "带附件的Email"
    # 设置正文内容
    msgcon = '<img src="cid:image" style="width:300px"/>'
    msg.attach(MIMEText(msgcon, "html", "utf-8"))

    # 读取图片
    fp = open("E:\\html页面\\微立印\\images\\2.png", "rb")
    msgImg = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImg.add_header("Content-ID", "<image>")
    msg.attach(msgImg)
    try:
        # 创建服务 发件人邮箱中的SMTP服务器
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, my_user, msg.as_string())
        # 关闭连接
        server.quit()
        print("发送成功")
    except Exception as e:
        print("发送失败" + e)

emailImg()
