import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import doc


class Mailing:
    def sendmail(self, attachment_file: str):
        try:
            login = doc.mail_login
            password = doc.mail_password
            email_from = doc.mail_login
            email_to = doc.recipient

            message = MIMEMultipart()
            message['From'] = email_from
            message['To'] = email_to
            message['Subject'] = 'SO'

            text = 'Текст письма'
            message.attach(MIMEText(text, 'plain', 'utf-8'))

            attachment = open(attachment_file, 'rb')
            attachment_part = MIMEApplication(attachment.read(), 'application/octet-stream')
            attachment_part.add_header('Content-Disposition', 'attachment')
            message.attach(attachment_part)

            encoded_message = message.as_bytes()
            server = smtplib.SMTP_SSL(doc.smtp_mail)
            server.login(login, password)
            server.sendmail(email_from, email_to, encoded_message)
            server.quit()
        except server.error as e:
            print("Could not connect to server - is it down? ({0}): {1}".format(e.strerrror))
