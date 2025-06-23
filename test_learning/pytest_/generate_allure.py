"""
使用pytest的时候 cd 到当前目录，会执行当前目录的所有 unit_tests func 类等等
password: smal nond dpdg asjw
"""

import pytest
import os
import time

from open_and_send_report import send_test_report_email

r"""
写信封（发件人、收件人、主题）	Email 头	    EmailMessage().['From'] = ...
写正文和附件	                信内容	        msg.set_content(), msg.add_attachment()
投入邮筒寄出	                发邮件	        smtplib.SMTP_SSL(...).send_message(msg)
"""

if __name__ == "__main__":
    # pytest.main(["-vs","test_login.py"]) # only execute test_login.py

    # select ut mark unit_tests cases, and generate allure's data in temps folder
    pytest.main(["-vs", "--alluredir=temps"])  # [] as the parameter

    # use allure to generate HTML report， need jdk to run
    os.system("/home/linuxbrew/.linuxbrew/bin/allure generate -o report -c temps")

    time.sleep(5)

