
class PhishingMessage():
    THEME = "this is phishing"
    PH_TEXT = "Here is phishing link www.www.www"

class SpamMessage():
    THEME = "THIS IS SPAM MESSAGE"
    SPAM_TEXT = "DON'T SEND SPAM PLZ"


class MassmailMessage():
    THEME = "this is massmail"
    MASSMAIL_TEXT = "This is massmail"


class MalwareMessage():
    THEME = "this is mlwre"
    MALWARE_TEXT = "Welcome to mlwre world!"
    MALWARE_ATTACH = {"clear": "eicar.test", "malware": "eicar.test"}


class AttachMessage():
    THEME = "this is attach"
    MALWARE_TEXT = "Open attach please"
    
    FORMAT_DATA_DOCUMENTS = {"doc": "test.doc", "docx": "test.docx", "odt": "test.odt", "pdf": "test.pdf", "rtf": "test.rtf", "xxx": "test.xxx"}
    FORMAT_DATA_SPREADSHEETS = {"xls":"test.xls", "xlt":"test.xlt", "xlsx":"test.xlsx","xlsb":"test.xlsb", "xltx": "test.xltx", "xltm": "test.xltm", "xlam":"test.xlam", "ods":"test.ods", "xlsm":"test.xlsm" }
    FORMAT_DATA_PRESENTATIONS = {"pptx":"test.pptx"}
    FORMAT_DATA_SPECIALIZED = {"pub":"test.pub"}
    EXECUTABLE_FILES = {"exe":"test.exe"}
    FORMAT_ARCHIVES = {"zip": "1.zip", "rar":"123.rar"}
    MACROS = {"xlsm":"excel(macros).xlsm", "docm":"word(macros).docm"}
    BITAMP_IMAGES = {"jpg":"test.jpg", "png":"test.png"}
    VECTOR_GRAPHICS = {"eps":"test.eps"}
    ANIMATION = {"swf":"test.swf"}
    VIDEO ={"avi": "test.avi"}
    AUDIO = {"mp3":"test.mp3"}