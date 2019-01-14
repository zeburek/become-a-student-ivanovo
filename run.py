# coding: utf-8
import time

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

from params import Params


# Begin to fill the fields
def fill(field, text):
    field.clear()
    field.fill(text)


_url = "https://pgu.ivanovoobl.ru/favour-card#id:419754"
_login = ""
_password = ""

se = Browser("chrome",
             executable_path=ChromeDriverManager().install())
se.visit(_url)
login = se.find_by_css("#signin-url")
login.click()

# Login on ESIA
login_field_esia = se.find_by_css("#mobileOrEmail")
password_field_esia = se.find_by_css("#password")
login_button_esia = se.find_by_css(".button-big")
login_field_esia.fill(_login)
password_field_esia.fill(_password)
login_button_esia.click()

request_button = se.find_by_css(".right-info .apply-btn")
request_button.click()
with se.get_iframe(0)as iframe:
    # 1st block
    block = iframe.find_by_css('input')
    time.sleep(2)
    append = 0
    for i, k in enumerate(Params.params.keys()):
        while not block[i + append].visible:
            append += 1
        if k == "pol_rebenka":
            iframe.find_by_css("[type='radio']")[Params.params[k]].click()
            append += 1
        else:
            fill(block[i + append], Params.params[k])

    print(len(se.find_by_css("[name='confirm']")))
    se.find_by_css("[name='confirm']").click()
    se.find_by_css("[name='norobotsallowed']").click()

time.sleep(5)
