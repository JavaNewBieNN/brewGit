"""
使用pytest的时候 cd 到当前目录，会执行当前目录的所有 unit_tests func 类等等

"""

import pytest
import os

if __name__ == "__main__":
# pytest.main(["-vs","test_login.py"]) # only execute test_login.py


    # select ut mark unit_tests cases, and generate allure's data in temps folder
    pytest.main(["-vs", "--alluredir=temps"]) #   [] as the parameter

    # use allure to generate HTML report， need jdk to run
    os.system("/home/linuxbrew/.linuxbrew/bin/allure generate -o report -c temps")





