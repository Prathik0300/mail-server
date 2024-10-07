import os
import configparser
from config.logger import logger

class Configurator:
    def __init__(self,ENV):
        self.env = ENV
    
    def load_config(self):
        try:
            deployment_env = os.getenv(self.env, 'development')
            config_file = f'{deployment_env}.env'
            config = configparser.ConfigParser()
            config.read(config_file)
            return config[deployment_env]
        except Exception as Argument:
            logger().error()
