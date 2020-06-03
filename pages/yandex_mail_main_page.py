from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
import os
import pytest
from selenium.webdriver.common.keys import Keys

from .locators import LoginPageLocators
from .locators import MessageSendLocators
from .credential import UsersCredential
from .message_body import PhishingMessage
from .message_body import SpamMessage
from .message_body import MassmailMessage
from .message_body import MalwareMessage
from .message_body import AttachMessage
from .DateToLog import TimeLog




class MainPage(BasePage):


    def go_to_login_page(self):
        
        #SIGN_IN
        
        #login
        self.browser.implicitly_wait(10)
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_link.send_keys(UsersCredential.SENDER_LOGIN)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        time.sleep(3)

        #password
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(UsersCredential.SENDER_PASSWORD)
        password_login_button = self.browser.find_element(*LoginPageLocators.PASSWORD_LOGIN_BUTTON)
        password_login_button.click()

        time.sleep(3)


    def send_phishing_message(self):

        self.browser.implicitly_wait(10)
        write_message_button = self.browser.find_element(*MessageSendLocators.WRITE_MESSAGE_BUTTON)
        write_message_button.click()

        recepient_email_field = self.browser.find_element(*MessageSendLocators.RECEPIENT_EMAIL_FIELD)
        recepient_email_field.send_keys(*UsersCredential.RECEPIENT_EMAIL)

        theme_field = self.browser.find_element(*MessageSendLocators.THEME_FIELD)
        theme_field.send_keys(PhishingMessage.THEME)

        text_field = self.browser.find_element(*MessageSendLocators.TEXT_FIELD)
        text_field.send_keys(PhishingMessage.PH_TEXT)

        send_message_button = self.browser.find_element(*MessageSendLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()

        file = open("logs.txt", "a")
        file.write("TIME: " + TimeLog.DATA + "\t" +"TYPE: "+ PhishingMessage.THEME + "\n")

    
    def send_spam_message(self):

        self.browser.implicitly_wait(10)
        write_message_button = self.browser.find_element(*MessageSendLocators.WRITE_MESSAGE_BUTTON)
        write_message_button.click()
        
        self.browser.implicitly_wait(10)
        recepient_email_field = self.browser.find_element(*MessageSendLocators.RECEPIENT_EMAIL_FIELD)
        recepient_email_field.click()
        recepient_email_field.send_keys(*UsersCredential.RECEPIENT_EMAIL)


        theme_field = self.browser.find_element(*MessageSendLocators.THEME_FIELD)
        theme_field.click()
        theme_field.send_keys(SpamMessage.THEME)

        self.browser.implicitly_wait(10)
        text_field = self.browser.find_element(*MessageSendLocators.TEXT_FIELD)
        text_field.click()
        text_field.send_keys(SpamMessage.SPAM_TEXT)

        send_message_button = self.browser.find_element(*MessageSendLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()

        file = open("logs.txt", "a")
        file.write("TIME: " + TimeLog.DATA + "\t" +"TYPE: "+ SpamMessage.THEME + "\n")
        


    def send_massmail_message(self):

        self.browser.implicitly_wait(10)
        write_message_button = self.browser.find_element(*MessageSendLocators.WRITE_MESSAGE_BUTTON)
        write_message_button.click()

        recepient_email_field = self.browser.find_element(*MessageSendLocators.RECEPIENT_EMAIL_FIELD)
        recepient_email_field.send_keys(*UsersCredential.RECEPIENT_EMAIL)

        theme_field = self.browser.find_element(*MessageSendLocators.THEME_FIELD)
        theme_field.send_keys(MassmailMessage.THEME)

        text_field = self.browser.find_element(*MessageSendLocators.TEXT_FIELD)
        text_field.send_keys(MassmailMessage.MASSMAIL_TEXT)

        send_message_button = self.browser.find_element(*MessageSendLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()

        file = open("logs.txt", "a")
        file.write("TIME: " + TimeLog.DATA + "\t" +"TYPE: "+ MassmailMessage.THEME + "\n")

    
    def send_malware_message(self,choose_status):

        self.browser.implicitly_wait(10)
        write_message_button = self.browser.find_element(*MessageSendLocators.WRITE_MESSAGE_BUTTON)
        write_message_button.click()

        recepient_email_field = self.browser.find_element(*MessageSendLocators.RECEPIENT_EMAIL_FIELD)
        recepient_email_field.send_keys(*UsersCredential.RECEPIENT_EMAIL)

        theme_field = self.browser.find_element(*MessageSendLocators.THEME_FIELD)
        theme_field.send_keys(MalwareMessage.THEME)

        text_field = self.browser.find_element(*MessageSendLocators.TEXT_FIELD)
        text_field.send_keys(MalwareMessage.MALWARE_TEXT)

        current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Malware"

        #choose_status == --attach_type parameter
        file_path = os.path.join(current_dir, MalwareMessage.MALWARE_ATTACH[choose_status])

        self.browser.implicitly_wait(20)
        file_attach = self.browser.find_element(*MessageSendLocators.FILE_ATTACH)
        file_attach.send_keys(file_path)
   
      
        send_message_button = self.browser.find_element(*MessageSendLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()

        file = open("logs.txt", "a")
        file.write("TIME: " + TimeLog.DATA + "\t" +"TYPE: "+ MalwareMessage.THEME + "\n")

    def send_attach_message(self, choose_status,choose_extension):

        self.browser.implicitly_wait(10)
        write_message_button = self.browser.find_element(*MessageSendLocators.WRITE_MESSAGE_BUTTON)
        write_message_button.click()

        recepient_email_field = self.browser.find_element(*MessageSendLocators.RECEPIENT_EMAIL_FIELD)
        recepient_email_field.send_keys(*UsersCredential.RECEPIENT_EMAIL)

        theme_field = self.browser.find_element(*MessageSendLocators.THEME_FIELD)
        theme_field.send_keys(AttachMessage.THEME)

        text_field = self.browser.find_element(*MessageSendLocators.TEXT_FIELD)
        text_field.send_keys(AttachMessage.MALWARE_TEXT)

        if choose_status == "FormatDataDocuments":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Data\Documents"
            file_path = os.path.join(current_dir, AttachMessage.FORMAT_DATA_DOCUMENTS[choose_extension])

        elif choose_status == "FormatDataSpreadsheets":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Data\Spreadsheets"
            file_path = os.path.join(current_dir, AttachMessage.FORMAT_DATA_SPREADSHEETS[choose_extension])
            
        elif choose_status == "FormatDataPresentations":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Data\Presentations"
            file_path = os.path.join(current_dir, AttachMessage.FORMAT_DATA_PRESENTATIONS[choose_extension])

        elif choose_status == "FormatDataSpecialized":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Data\Specialized"
            file_path = os.path.join(current_dir, AttachMessage.FORMAT_DATA_SPECIALIZED[choose_extension])

        elif choose_status == "FormatExecutableFiles":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Executable_files"
            file_path = os.path.join(current_dir, AttachMessage.EXECUTABLE_FILES[choose_extension])       

        elif choose_status == "FormatArchives":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Archives"
            file_path = os.path.join(current_dir, AttachMessage.FORMAT_ARCHIVES[choose_extension])

        elif choose_status == "FormatImagesAnimation":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Images\Animation"
            file_path = os.path.join(current_dir, AttachMessage.ANIMATION[choose_extension])

        elif choose_status == "FormatImagesBitmap":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Images\Bitmap_graphics"
            file_path = os.path.join(current_dir, AttachMessage.BITAMP_IMAGES[choose_extension])

        elif choose_status == "FormatImagesVector":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Images\Vector_graphics"
            file_path = os.path.join(current_dir, AttachMessage.VECTOR_GRAPHICS[choose_extension])

        elif choose_status == "FormatMultimediaVideo":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Multimedia\Video"
            file_path = os.path.join(current_dir, AttachMessage.VIDEO[choose_extension])

        elif choose_status == "FormatMultimediaAudio":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Format\Multimedia\Audio"
            file_path = os.path.join(current_dir, AttachMessage.AUDIO[choose_extension])

        elif choose_status == "Macros":
            current_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+ r"\sources\Attachment_filtering\Macros"
            file_path = os.path.join(current_dir, AttachMessage.MACROS[choose_extension])
        
        self.browser.implicitly_wait(10)    
        file_attach = self.browser.find_element(*MessageSendLocators.FILE_ATTACH)
        file_attach.send_keys(file_path)

        
        time.sleep(3) #to skip captcha
        self.browser.implicitly_wait(10)
        send_message_button = self.browser.find_element(*MessageSendLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()

        file = open("logs.txt", "a")
        file.write("TIME: " + TimeLog.DATA + "\t" +"TYPE: "+ AttachMessage.THEME + "\t" +"EXTENSION: "+ choose_extension +"\n")
    

  

    def check_send_message(self):
        time.sleep(3)
        if self.did_url_chanched("done"):
            send_message_url = self.browser.current_url
            self.browser.implicitly_wait(10)
            assert send_message_url[-4:] == "done", "Message send error"
    