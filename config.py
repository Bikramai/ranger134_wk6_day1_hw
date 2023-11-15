import os #operating system
from dotenv import load_dotenv #allows us to load environment variables to do certain things with our app



# establish our base directory so whenever we use "." to reference any location in our app it knows we are referncing
# abodezen_shop folder 
basedir = os.path.abspath(os.path.dirname(__file__)) #this is establishing our base directory or our root folder


#need to establish where our environment variables are coming from (this file will be hidden from github)
load_dotenv(os.path.join(basedir, '.env')) #this is just pointing us to the direction of our environment variables (located in .env file)


#making this a seperate class we can have many Config classes (aka 1 for development, 1 for production)
class Config():

    """
    Set Config variables for our flask app.
    Using Environment variables where available otherwise
    Create config variables.
    """

    FLASK_APP = os.environ.get('FLASK_APP') #looking for the key of Flask_APP in our .env file 
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Literally whatever you want as long as its a string. Cool Beans'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')


