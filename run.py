# coding: utf-8
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elementium.drivers.se import SeElements
from params import Params
import time

_url = "https://pgu.ivanovoobl.ru/web/guest/favour#src:s02/procedure:155901"
_login = "login"
_password = "pwd"

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
block = se.find('input')
fill(block.get(0),Params._familiya_zayavitelya)
fill(block.get(1),Params._imya_zayavitelya)
fill(block.get(2),Params._otchestvo_zayavitelya)
fill(block.get(3),Params._SNILS_zayavitelya)

# 2nd block
fill(block.get(4),Params._pasport_seriya)
fill(block.get(5),Params._pasport_nomer)
fill(block.get(6),Params._pasport_data_vidachi)
fill(block.get(7),Params._pasport_kem_vidan)
fill(block.get(8),Params._pasport_kod_podrazdeleniya)

# 3d block
fill(block.get(9),Params._index_zayavitelya)
fill(block.get(10),Params._gorod_zayavitelya)
fill(block.get(11),Params._ulitsa_zayavitelya)
fill(block.get(12),Params._dom_zayavitelya)
fill(block.get(13),Params._korpus_zayavitelya)
fill(block.get(14),Params._nomer_kvertiri_zayavitelya)

# 4th block
fill(block.get(15),Params._nomer_telephona)
fill(block.get(16),Params._email)

# 5th block
fill(block.get(17),Params._SNILS_rebenka)
fill(block.get(18),Params._familiya_rebenka)
fill(block.get(19),Params._imya_rebenka)
fill(block.get(20),Params._otchestvo_rebenka)
se.find("[type='radio']").get(Params._pol_rebenka).click()
fill(block.get(23),Params._data_rozhdeniya_rebenka)

# 6th block
fill(block.get(24),Params._seriya_sor)
fill(block.get(25),Params._nomer_sor)
fill(block.get(26),Params._data_vidachi_sor)
fill(block.get(27),Params._kem_vidan_sor)
fill(block.get(28),Params._nomer_zapisi_akta_o_rozhdeniya_sor)

# 7th block
fill(block.get(29),Params._index_rebenka)
fill(block.get(30),Params._gorod_rebenka)
fill(block.get(31),Params._ulitsa_rebenka)
fill(block.get(32),Params._dom_rebenka)
fill(block.get(33),Params._korpus_rebenka)
fill(block.get(34),Params._nomer_kvertiri_rebenka)

# 8th block
fill(block.get(35),Params._familiya_otsa)
fill(block.get(36),Params._imya_otsa)
fill(block.get(37),Params._otchestvo_otsa)
fill(block.get(38),Params._data_rozhdeniya_otsa)
fill(block.get(39),Params._email_otsa)
fill(block.get(40),Params._telephone_otsa)

# 9th block
fill(block.get(41),Params._familiya_materi)
fill(block.get(42),Params._imya_materi)
fill(block.get(43),Params._otchestvo_materi)
fill(block.get(44),Params._data_rozhdeniya_materi)
fill(block.get(45),Params._email_materi)
fill(block.get(46),Params._telephone_materi)

print(len(se.find("[name='confirm']")))
se.find("[name='confirm']").click()

time.sleep(5)
