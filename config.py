import os #operating system
from dotenv import load_dotenv #allows us to load environment variables to do certain things with our app




basedir = os.path.abspath(os.path.dirname(__file__)) #this is establishing our base directory or our root folder

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
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Nana nana boo boo, you'll never guess this" #just needs to be present 
  