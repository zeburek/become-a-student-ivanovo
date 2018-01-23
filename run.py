# coding: utf-8
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elementium.drivers.se import SeElements
from params import Params
import time

_url = "https://pgu.ivanovoobl.ru/web/guest/favour#procedure:420513/"
_login = "login"
_password = "password"

se = SeElements(webdriver.Chrome(ChromeDriverManager().install()))
se.navigate(_url)
request_button = se.find("#requestButtonId")
request_button.click()
time.sleep(3)

# Login on ESIA
login_field_esia = se.find("#mobileOrEmail")
password_field_esia = se.find("#password")
login_button_esia = se.find(".button-big")
login_field_esia.write(_login)
password_field_esia.write(_password)
login_button_esia.click()

# Reloading page, because of bugs in site
time.sleep(10)
# se.navigate("https://ya.ru")
# se.navigate(_url)
# time.sleep(5)
se.browser.switch_to.frame(se.browser.find_element_by_tag_name("iframe"))
# Begin to fill the fields
def fill(field, text):
    field.clear().write(text)

# 1st block
block = se.find('#applicant_fieldset').find('input')
fill(block.get(0),Params._familiya_zayavitelya)
fill(block.get(1),Params._imya_zayavitelya)
fill(block.get(2),Params._otchestvo_zayavitelya)
fill(block.get(3),Params._SNILS_zayavitelya)

# 2nd block
block = se.find('#applicant_passport_fieldset').find('input')
fill(block.get(0),Params._pasport_seriya)
fill(block.get(1),Params._pasport_nomer)
fill(block.get(2),Params._pasport_data_vidachi)
fill(block.get(3),Params._pasport_kem_vidan)
fill(block.get(4),Params._pasport_kod_podrazdeleniya)

# 3d block
block = se.find('#applicant_address_fieldset').find('input')
fill(block.get(0),Params._index_zayavitelya)
fill(block.get(1),Params._gorod_zayavitelya)
fill(block.get(2),Params._ulitsa_zayavitelya)
fill(block.get(3),Params._dom_zayavitelya)
fill(block.get(4),Params._korpus_zayavitelya)
fill(block.get(5),Params._nomer_kvertiri_zayavitelya)

# 4th block
block = se.find('#applicant_notify_fieldset').find('input')
fill(block.get(0),Params._nomer_telephona)
fill(block.get(1),Params._email)

# 5th block
block = se.find('#child_fieldset').find('input')
fill(block.get(0),Params._SNILS_rebenka)
fill(block.get(1),Params._familiya_rebenka)
fill(block.get(2),Params._imya_rebenka)
fill(block.get(3),Params._otchestvo_rebenka)
se.find("[type='radio']").get(Params._pol_rebenka).click()
fill(block.get(6),Params._data_rozhdeniya_rebenka)

# 6th block
block = se.find('#child_doc_fieldset').find('input')
fill(block.get(0),Params._seriya_sor)
fill(block.get(1),Params._nomer_sor)
fill(block.get(2),Params._data_vidachi_sor)
fill(block.get(3),Params._kem_vidan_sor)
fill(block.get(4),Params._nomer_zapisi_akta_o_rozhdeniya_sor)

# 7th block
block = se.find('#child_address_fieldset').find('input')
fill(block.get(0),Params._index_rebenka)
fill(block.get(1),Params._gorod_rebenka)
fill(block.get(2),Params._ulitsa_rebenka)
fill(block.get(3),Params._dom_rebenka)
fill(block.get(4),Params._korpus_rebenka)
fill(block.get(5),Params._nomer_kvertiri_rebenka)

# 8th block
block = se.find('#father_fieldset').find('input')
fill(block.get(0),Params._familiya_otsa)
fill(block.get(1),Params._imya_otsa)
fill(block.get(2),Params._otchestvo_otsa)
fill(block.get(3),Params._data_rozhdeniya_otsa)
fill(block.get(4),Params._email_otsa)
fill(block.get(5),Params._telephone_otsa)

# 9th block
block = se.find('#mother_fieldset').find('input')
fill(block.get(0),Params._familiya_materi)
fill(block.get(1),Params._imya_materi)
fill(block.get(2),Params._otchestvo_materi)
fill(block.get(3),Params._data_rozhdeniya_materi)
fill(block.get(4),Params._email_materi)
fill(block.get(5),Params._telephone_materi)

print(len(se.find("[name='confirm']")))
se.find("[name='confirm']").click()

time.sleep(5)
