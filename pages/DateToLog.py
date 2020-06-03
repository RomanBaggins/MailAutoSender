import datetime

class TimeLog():
    today = datetime.datetime.today()
    DATA = today.strftime("%Y-%m-%d-%H:%M:%S") 

class PhishingLog():
    PHISHING_LOG = "Phishing"

class SpamLog():
    SPAM_LOG = "Spam"
class MassmailLog():
    MASSMAIL_LOG = "Massmail"

class MalwareLog():
    MALWARE_LOG = "Malware"

class AttachLog():
    ATTACH_LOG = "Attach"
