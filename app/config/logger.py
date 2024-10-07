import logging
import traceback

class Logger:
    def __init__(self) -> None:
        self.logger = logging.getLogger('MY_MAIL_SERVER')
        self.console_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler('app.log')
        self.formatter = logging.Formatter('%(name)s::%(levelname)s::[%(asctime)s] -> %(message)s\n')
        
        self.logger.setLevel(logging.DEBUG)
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)
            
    def error(self, message = "") -> None:
        self.logger.setLevel(logging.ERROR)
        if message:
            self.logger.error(f'{message}', exc_info=True)
        else:
            self.logger.error(f'\nStack Trace: {traceback.format_exc()}')
            
    def warn(self, message = "") -> None:
        self.logger.setLevel(logging.WARNING)
        if message:
            self.logger.warning(f'{message}',exc_info=True)
    
    def info(self, message = "") -> None:
        self.logger.setLevel(logging.INFO)
        if message:
            self.logger.info(f'{message}')
        
def logger() -> Logger:
    return Logger()
