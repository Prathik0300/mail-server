from src.email import email_service
from config.logger import logger
from config.configurator import Configurator
from src.sockets import SocketHandler
import argparse
from src.smtp_server import run_smtp_server

# def handle_smtp(connection, address):
#     # ... SMTP server logic ...

# def handle_imap(connection, address):
#     # ... IMAP server logic ...

# def handle_pop3(connection, address):
#     # ... POP3 server logic ...

# def main():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('localhost', 25))  # SMTP port
#     server_socket.listen()

#     while True:
#         connection, address = server_socket.accept()
#         thread = threading.Thread(target=handle_connection, args=(connection, address))
#         thread.start()

# def handle_connection(connection, address):
#     # Determine the protocol based on the first line of the greeting
#     greeting = connection.recv(1024).decode()
#     if greeting.startswith('EHLO'):
#         handle_smtp(connection, address)
#     elif greeting.startswith('CAPA'):
#         handle_imap(connection, address)
#     elif greeting.startswith('USER'):
#         handle_pop3(connection, address)
#     else:
#         # Handle other protocols or errors
#         connection.sendall(b'Unsupported protocol\r\n')

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="This is a mail server script")
        parser.add_argument('--env', '-e', choices=['dev','prod'], default='dev', help='Provide environment to run script')

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

        email_service(config).send_email(recipient_email=recipient, subject=subject, body=body)
        
    except Exception:
        logger().error(Exception)