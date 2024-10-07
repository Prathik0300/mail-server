from socket import socket
from config.logger import logger
import ssl

class IMAPServer:
    def __init__(self, connection_handler: socket):
        self.connection = connection_handler
    
    def handle_client(self):
        self.connection.send(b'* OK IMAP server ready\r\n')
        
        while True:
            try:
                data = self.connection.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                
                print(f'received data : {data}')
                command = data.split(' ')[1].upper() if len(data.split(' ')) > 1 else None
                
                match command:
                    case 'LOGIN':
                        self.handle_login()
                        break
                    case 'LIST':
                        self.handle_list()
                        break
                    case 'SELECT':
                        self.handle_select(data)
                        break
                    case 'FETCH':
                        self.handle_fetch(data)
                        break
                    case 'LOGOUT':
                        self.handle_logout()
                        break
                    case default:
                        self.connection.send(b'* BAD Unknown command\r\n')
                        break
            except Exception:
                logger().error(f'{Exception}')
        
    def handle_login(self):
        self.connection.send(b'* OK LOGIN completed\r\n')
    
    def handle_list(self):
        self.connection.send(b'* LIST (\\HasNoChildren) "." "INBOX"\r\n')
        self.connection.send(b'0001 OK LIST completed\r\n')

    def handle_select(self, data):
        if 'INBOX' in data:
            self.connection.send(b'* 1 EXISTS\r\n')
            self.connection.send(b'* 1 RECENT\r\n')
            self.connection.send(b'0002 OK [READ-WRITE] SELECT completed\r\n')
 
    def handle_fetch(self, data):
        email_data = self.get_email_content(1)
        response = f'* 1 FETCH (BODY[] {{{len(email_data)}}}\r\n{email_data})\r\n'
        self.connection.send(response.encode('utf-8'))
        self.connection.send(b'0003 OK FETCH completed\r\n')

    def get_email_content(self, email_id):
        return f"From: example@example.com\r\nTo: recipient@example.com\r\nSubject: Test\r\n\r\nThis is a test email.\r\n"

    def handle_logout(self):
        self.connection.send(b'* BYE IMAP server logging out\r\n')
        self.connection.send(b'0004 OK LOGOUT completed\r\n')
