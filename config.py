import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))



class Config():
    """
        Set Config variables for the flask app.
        Using Environment variables where available otherwise
        create the config variables if not done already.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://postgres:Miscellaneous17!@127.0.0.1:5432/carinven"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 