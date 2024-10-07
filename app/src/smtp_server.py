import asyncio
from aiosmtpd.controller import Controller
import ssl

class SMTPServer:
        
    async def handle_DATA(self, server, session, envelope):
        print("Message from:", envelope.mail_from)
        # Print the recipient's email addresses
        print("Message to:", envelope.rcpt_tos)
        
        # Print the raw content of the email
        print("Message data:")
        print(envelope.content.decode())  # Decode bytes to string for readability
        
        # Return a status code to acknowledge receipt of the email
        return '250 Message accepted for delivery'
    
def run_smtp_server(config):
    port = config['SMTP_PORT']
    host = config['SMTP_SERVER_ADDRESS']
    smtp_handler = SMTPServer()
    
    # SSL for TLS
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    
    controller = Controller(smtp_handler, port=port)
    controller.start()
    
    print(f'SMTP server running on {host}:{port}')
    
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()
        print('server stopped')

        