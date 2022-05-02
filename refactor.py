import email
import smtplib
import imaplib
import os
from email.message import EmailMessage


class MailHandler():

    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def sendMessage(self, text: str, subject: str,
                    recepients: list, port=587):

        msg = EmailMessage()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.set_content(text)

        ms = smtplib.SMTP(self.GMAIL_SMTP, port)  # send message
        ms.ehlo()                                 # identify ourselves to smtp gmail client
        ms.starttls()                             # secure our email with tls encryption
        ms.ehlo()                                 # re-identify ourselves as an encrypted connection
        ms.login(self.login, self.login)
        ms.sendmail(self.login, ms,
                    msg.as_string())
        ms.quit()

    def recieveMessage(self, header):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    login = os.getenv('login')      # 'login@gmail.com'
    password = os.getenv('password')   # 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'

    mail = MailHandler(login, password)
