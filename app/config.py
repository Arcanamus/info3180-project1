import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = 'C:\\Users\\Arcan\\Documents\\WebDevLab\\info3180-project1\\uploads'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://beeqxzsuxbqloc:b6563457787b0a6fddbccb90bf71772f65411ff8b5fa7bdb2806e934ba0ed5db@ec2-3-216-221-31.compute-1.amazonaws.com:5432/d26uug5dfjq6k1'
).replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed