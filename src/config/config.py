import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        environment = os.getenv('FLASK_ENV')

        if environment == 'local':
            load_dotenv(dotenv_path='.env.local', override=True)
        elif environment == 'test':
            load_dotenv(dotenv_path='.env.test', override=True)
        else:
            load_dotenv(dotenv_path='.env', override=True)

        self.ENVIRONMENT = environment
        self.APP_NAME = os.getenv('APP_NAME', 'saludtechalpes-medical-history-service')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_NAME = os.getenv('DB_NAME')
        self.BROKER_HOST = os.getenv('BROKER_HOST')
        self.BROKER_PORT = os.getenv('BROKER_PORT')
        self.PULSAR_HOST = os.getenv('PULSAR_HOST')
