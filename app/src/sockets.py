import socket
import ssl

class SocketHandler:
    def __init__(self, config) -> None:
        self.host = config['HOST']
        self.port = config['PORT']
        self.use_ssl = config['USE_SSL']
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f'server socket running on {self.host}:{self.port}')
        
    def accept_connection(self):
        connection, addr = self.server_socket.accept()
        print(f'Connection from {addr}')
        if self.use_ssl:
            connection = self.wrap_ssl(connection)
        
        return connection, addr
    
    def wrap_ssl(self, connection):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        return context.wrap_socket(connection,server_side=True)
    
    def close(self):
        self.server_socket.close()
    
