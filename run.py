from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elementium.drivers.se import SeElements
from params import Params
import time

_url = "https://pgu.ivanovoobl.ru/web/guest/favour#filter:/page:1/query:&#209;&#130;&#208;µ&#209;&#129;&#209;&#130;/procedure:420513/"
_login = input("Логин для ГосУслуг: ")
_password = input("Пароль для ГосУслуг: ")


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
time.sleep(5)
se.navigate("https://ya.ru")
se.navigate(_url)
time.sleep(5)
se.browser.switch_to.frame(se.browser.find_element_by_tag_name("iframe"))
# Begin to fill the fields
def fill(field, text):
    se.find(field).clear().write(text)

# 1st block
fill("#a_surname",Params._familiya_zayavitelya)
fill("#a_name",Params._imya_zayavitelya)
fill("#a_middlename",Params._otchestvo_zayavitelya)
fill("#a_snils",Params._SNILS_zayavitelya)

# 2nd block
fill("#a_p_series",Params._pasport_seriya)
fill("#a_p_numeral",Params._pasport_nomer)
fill("#a_p_issue_date",Params._pasport_data_vidachi)
fill("#a_p_issuer",Params._pasport_kem_vidan)
fill("#a_p_code",Params._pasport_kod_podrazdeleniya)

# 3d block
fill("#a_a_zip",Params._index_zayavitelya)
fill("#a_a_city",Params._gorod_zayavitelya)
fill("#a_a_street",Params._ulitsa_zayavitelya)
fill("#a_a_house",Params._dom_zayavitelya)
fill("#a_a_building",Params._korpus_zayavitelya)
fill("#a_a_flat",Params._nomer_kvertiri_zayavitelya)

# 4th block
fill("#a_phone",Params._nomer_telephona)
fill("#a_email",Params._email)

# 5th block
fill("#snils",Params._SNILS_rebenka)
fill("#surname",Params._familiya_rebenka)
fill("#name",Params._imya_rebenka)
fill("#middle_name",Params._otchestvo_rebenka)
se.find("[name='gender']").get(Params._pol_rebenka).click()
fill("#birthday",Params._data_rozhdeniya_rebenka)

# 6th block
fill("#c_d_series",Params._seriya_sor)
fill("#c_d_numeral",Params._nomer_sor)
fill("#c_d_issue_date",Params._data_vidachi_sor)
fill("#c_d_issuer",Params._kem_vidan_sor)
fill("#c_d_issue_doc",Params._nomer_zapisi_akta_o_rozhdeniya_sor)

# 7th block
fill("#c_a_zip",Params._index_rebenka)
fill("#c_a_city",Params._gorod_rebenka)
fill("#c_a_street",Params._ulitsa_rebenka)
fill("#c_a_house",Params._dom_rebenka)
fill("#c_a_building",Params._korpus_rebenka)
fill("#c_a_flat",Params._nomer_kvertiri_rebenka)

# 8th block
fill("#f_surname",Params._familiya_otsa)
fill("#f_name",Params._imya_otsa)
fill("#f_middlename",Params._otchestvo_otsa)
fill("#f_birthday",Params._data_rozhdeniya_otsa)
fill("#f_email",Params._email_otsa)
fill("#f_phone",Params._telephone_otsa)

# 9th block
fill("#m_surname",Params._familiya_materi)
fill("#m_name",Params._imya_materi)
fill("#m_middlename",Params._otchestvo_materi)
fill("#m_birthday",Params._data_rozhdeniya_materi)
fill("#m_email",Params._email_materi)
fill("#m_phone",Params._telephone_materi)

print(len(se.find("[name='confirm']")))
se.find("[name='confirm']").click()

time.sleep(5)
