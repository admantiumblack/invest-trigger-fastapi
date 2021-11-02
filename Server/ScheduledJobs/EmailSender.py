from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from Server.config.EmailConfig import email_config

class EmailSender():
    def __init__(self):
        
        self.s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        self.s.starttls()
        self.__EMAIL = email_config.get_email()
        self.s.login(self.__EMAIL, email_config.get_password())


    def send_email(self, email, pair, timeframe, indicator1, comparator, indicator2):
        msg = MIMEMultipart()
        content = email_config.get_email_template()
        content = content.substitute(PAIR=pair, TIMEFRAME=timeframe,
                INDICATOR1=indicator1, COMPARATOR=comparator, INDICATOR2=indicator2)
        msg['From'] = self.__EMAIL
        msg['To'] = email
        msg['Subject'] = 'your trigger has been triggered'
        self.s.send_message(msg)
        del msg
