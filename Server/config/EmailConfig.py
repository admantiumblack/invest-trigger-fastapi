import os
from Server.config.BaseConfig import Singleton
from string import Template
class EmailConfig(metaclass=Singleton):
    def __init__(self):
        self.__email = os.environ.get('EMAIL')
        self.__password = os.environ.get('EMAIL_PASSWORD')
        self.__emailTemplatePath = './Templates/EmailTemplate.txt'
    
    def get_email_template(self):
        emailTemplate = ''
        with open(self.__emailTemplatePath, 'r') as f:
            emailTemplate = '\n'.join(f.readlines())
        return Template(emailTemplate)

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email
email_config = EmailConfig()