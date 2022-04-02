from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.service import Service #librerias
from webdriver_manager.firefox import GeckoDriverManager #instalar esta libreria
import time
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
service = Service(executable_path=GeckoDriverManager().install())
options= Options()
profile_path = "/home/cristian/.mozilla/firefox/i42mr4f8.default" 
options.set_preference('profile', profile_path)
driver = webdriver.Firefox(service=service, options=options) #firefox_options=options


class TwitterBot:

    """
    A Bot class that provide features of:
        - Logging into your Twitter account
        - Liking tweets of your homepage
        - Searching for some keyword or hashtag
        - Liking tweets of the search results
        - Posting tweets
        - Logging out of your account
    ........
    Attributes
    ----------
    email : str
        user email for Twitter account
    password : str
        user password for Twitter account
    bot : WebDriver
        webdriver that carry out the automation tasks
    is_logged_in : bool
        boolean to check if the user is logged in or not
    Methods
    -------
    login()
        logs user in based on email and password provided during initialisation
    logout()
        logs user out
    search(query: str)
        searches for the provided query string
    like_tweets(cycles: int)
        loops over number of cycles provided, scrolls the page down and likes the available tweets on the page in each loop pass
    """
    

    def __init__(self, email):
        self.email = email
        self.bot = driver
        self.is_logged_in = False

    def forgot(self):
        bot = self.bot
        bot.get('https://twitter.com')
        "looks for the sign in buttom and click it"
        time.sleep(5)
        bot.find_element_by_link_text("Sign in").click()
        time.sleep(7)
        try:
            bot.find_element_by_link_text("Forgot password?").click()
        except:
            bot.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[7]/div/span/span").click()
        time.sleep(5)
