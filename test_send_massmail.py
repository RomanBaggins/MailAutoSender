from .pages.yandex_mail_main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru_suggest-exp&retpath=https%3A%2F%2Fmail.yandex.ru%2F%2F%3Fmsid%3D1562223891.09345.141188.275333%26m_pssp%3Ddomik&backpath=https%3A%2F%2Fyandex.ru"
    page = MainPage(browser, link)   
    page.open()                      
    page.go_to_login_page()
    page.send_massmail_message()          
    page.check_send_message()