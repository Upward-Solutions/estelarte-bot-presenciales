import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost/test_bot_presenciales"
    TESTING = True

