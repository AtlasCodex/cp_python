import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 设置邮件信息
sender = 'xxxxxx@163.com' # 发送者邮箱地址
receiver = 'xxxx@outlook.com' # 接收者邮箱地址
password = 'DxxxxxxxxKITDP' # 发送者邮箱密码或授权码


def send_email(subject,body):
    '''
    构造html模版
    接受主题和内容
    构造模版
    '''
    html_template = """
    <html>
      <head>
        <style>
      /* 居中图片 */
      .center {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
      }}
      /* 标题文字 */
      h1 {{
        text-align: center;
      }}
      /* 段落文字 */
      p {{
        text-align: justify;
      }}
    </style>
      </head>
      <body>
        <h3 >{subject}</h3>
        <p>{body}</p>
        <img src="{image_url}" class="center">
      </body>
    </html>
    """.format(subject=subject, image_url="https://img.alicdn.com/i3/1087939746/O1CN012LriWbkUd8XXJPf_!!1087939746.jpg_400x400q90", body=body)

    semail(html_template,subject)


def semail(html_template,subject):
    # 设置邮件信息
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(html_template, 'html', 'utf-8'))

    # 发送邮件
    try:
        smtpObj = smtplib.SMTP('smtp.163.com', 25) # SMTP服务器地址和端口号
        smtpObj.starttls() # 使用TLS加密通信
        smtpObj.login(sender, password) # 登录邮箱账号
        smtpObj.sendmail(sender, receiver, msg.as_string()) # 发送邮件
        print("邮件发送成功！")
    except smtplib.SMTPException as e:
        raise e
    finally:
        smtpObj.quit()
