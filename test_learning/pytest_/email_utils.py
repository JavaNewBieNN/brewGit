"""
使用pytest的时候 cd 到当前目录，会执行当前目录的所有 unit_tests func 类等等

"""
import json
import \
    smtplib  # smtplib- a module from Python std lib （don't need to install）发送邮件用的（Simple Mail Transfer Protocol） smtplib 是“负责把这封信送出去的邮递员”。
from email.message import EmailMessage  # 构造邮件内容用的（包括主题、正文、附件等） EmailMessage 是“写邮件的纸和信封”，
from zip_pack import zip_report_folder
r"""
写信封（发件人、收件人、主题）	Email 头	    EmailMessage().['From'] = ...
写正文和附件	                信内容	        msg.set_content(), msg.add_attachment()
投入邮筒寄出	                发邮件	        smtplib.SMTP_SSL(...).send_message(msg)
"""


def send_test_report_email():
    try:
        with open('email_config.json', 'r') as f:
            config = json.load(f)

        # get parameters
        sender = config['sender']
        password = config['password']
        recipients = ", ".join(config['recipients'])

        msg = EmailMessage()  # construct a email object

        # set the email head
        msg['Subject'] = 'Automatic test report'
        msg['From'] = sender
        msg['To'] = recipients

        # set the email content
        msg.set_content(
            'Greeting from Novele Automatic test. This is an automated test message, test report attached '
            'below.')

        r"""
            打开本地文件夹里的 pytest.log 文件（二进制读模式 rb）。 rb: read binary
            用 add_attachment() 把这个文件作为附件附在邮件里。      
            maintype='text', subtype='plain' 表示这是纯文本文件。
            filename 是你希望收件人看到的文件名。
        """
        zip_report_folder()

        with open('logs/pytest.log', 'rb') as log_file, open('report.zip', 'rb') as zip_file:
            msg.add_attachment(log_file.read(), maintype='text', subtype='plain', filename='pytest.log')
            msg.add_attachment(zip_file.read(), maintype='application', subtype='zip', filename='report.zip')

            # 发邮件（用 gmail 为例）
        with smtplib.SMTP_SSL('smtp.gmail.com',
                              465) as smtp:  # SSL protocol sent to gmail server port 465 for ssl, gmail + _SSL
            # smtp.starttls() # TLS encryption for outlook
            smtp.login('cherxnie@gmail.com', password)
            smtp.send_message(msg)
            print("email sending successfully")


    except FileNotFoundError as e:
        print(f"❌ attachment can't be found：{e.filename}")
        return

    except Exception as e:
        print(f"❌ something wrong in reading files：{e}")
        print("email sending failed")
        return


"""
        ✅ 什么是 MIME 类型？
        MIME（Multipurpose Internet Mail Extensions）是“告诉邮箱或浏览器：这个文件是啥格式”的一种方式。

        ➤ 举个例子：
        text/plain → 表示：这个附件是“纯文本”

        text/html → 表示：这个附件是“网页”

        image/png → 表示：这是一个 PNG 图片

        application/pdf → 表示：这是一个 PDF 文件

        ✅ MIME 类型 = maintype/subtype
        maintype：主类型，比如 text、image、application

        subtype：子类型，比如 plain、html、pdf

        你可以类比成：

        arduino
        复制
        编辑
        MIME 类型 = 大分类 / 具体格式
                 =  text    /   html
                 =  image   /   png
                 =  application / zip
        """
