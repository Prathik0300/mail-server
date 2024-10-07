import argparse
from config.configurator import Configurator
from src.sockets import SocketHandler
from src.smtp_server import run_smtp_server
from src.email import email_service
from config.logger import logger

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="This is a mail server script")
        parser.add_argument(
            '--env',
            '-e',
            choices=['dev','prod'],
            default='dev',
            help='Provide environment to run script'
        )

        namespace_args = parser.parse_args()
        environment =  'development' if namespace_args.env == 'dev' else 'production'
        
        # Load Env config
        config = Configurator(ENV=environment).load_config()
        
        # Initialize Socket
        socket = SocketHandler(config=config)
        
        # Start SMTP Server
        run_smtp_server(config)
        
        # Use Email Service
        recipient = "prathik0300@gmail.com"  # This should be the address you want to send to
        subject = "Test Email"
        body = "Hello, this is a test email sent from Python!"

        email_service(config).send_email(
            recipient_email=recipient,
            subject=subject,
            body=body)
        
    except Exception:
        logger().error(f'{Exception}')