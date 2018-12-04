'''
Created on 11 lis 2018

@author: ewelina
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# from PrivateData import privateData as pv


def sendEmail(recipients, subject, message, fileName):
            
    msg = MIMEMultipart()
    msg["From"] = smtpLogin
    msg["To"] = ",".join(recipients)
    msg["Subject"] = subject
        
    msgText = message
    msg.attach(MIMEText(msgText, "plain"))
            
    attachment = open(fileName, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", 'attachment', filename = fileName)
        
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(smtpLogin, smtpPassword)
        
    server.sendmail(smtpLogin, recipients, text)
    server.quit()
