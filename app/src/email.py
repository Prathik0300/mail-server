import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.logger import logger

class Email:
    def __init__(self, config):
        self.sender_email = config['SENDER_EMAIL_ADDRESS']
        self.smtp_server = config['SMTP_SERVER_ADDRESS']
        self.smtp_port = config['SMTP_PORT']
        
    def send_email(self, recipient_email, subject, body):
        print(self.sender_email, self.smtp_port, self.smtp_server)
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        message.attach(MIMEText(body, 'plain'))
        try:
            print('inside send email')
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.sendmail(self.sender_email, recipient_email, message.as_string())
                print("Email sent from {} to {}.".format(self.sender_email, recipient_email))
        except Exception:
            logger().error(f'{Exception}')

def email_service(config):
    return Email(config)