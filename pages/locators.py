from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#passp-field-login")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#root > div > div > div.passp-flex-wrapper > div > div > div.passp-auth-content > div:nth-child(2) > div > div > div.passp-login-form > form > div.passp-button.passp-sign-in-button > button.control.button2.button2_view_classic.button2_size_l.button2_theme_action.button2_width_max.button2_type_submit.passp-form-button")

    PASSWORD_FIELD = (By.CSS_SELECTOR, "#passp-field-passwd")
    PASSWORD_LOGIN_BUTTON = (By.CSS_SELECTOR, "#root > div > div > div.passp-flex-wrapper > div > div.passp-auth > div.passp-auth-content > div.passp-route-forward > div > div > form > div.passp-button.passp-sign-in-button > button.control.button2.button2_view_classic.button2_size_l.button2_theme_action.button2_width_max.button2_type_submit.passp-form-button")

class MessageSendLocators():

    WRITE_MESSAGE_BUTTON = (By.XPATH, '//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[2]/div[2]/div/div/a/span') 
    RECEPIENT_EMAIL_FIELD = (By.XPATH, '//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/div[1]/label/div[3]/div')
    THEME_FIELD = (By.XPATH, '//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/label/div[3]/input')
    TEXT_FIELD = (By.XPATH, '//*[@id="cke_1_contents"]/div')
    SEND_MESSAGE_BUTTON = (By.XPATH, '//*[@id="nb-12"]/span/span/span')
    FILE_ATTACH = (By.XPATH, '//*[@id="nb-1"]/body/div[2]/div[6]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[4]/div/label/input')                        
    SUCCESS_TEXT = (By.XPATH, '//*[@id="nb-1"]/body/div[2]/div[6]/div/div[3]/div[3]/div[2]/div[5]/div/div/div[1]')


