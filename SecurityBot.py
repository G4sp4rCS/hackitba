from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.service import Service #librerias
from webdriver_manager.firefox import GeckoDriverManager #instalar esta libreria
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv, find_dotenv
from imap_tools import MailBox, AND
load_dotenv(find_dotenv())


def mailCredentials():

    mail = os.getenv('MAIL')
    password = os.getenv('PASSWORD')
    return mail, password

options = Options()
options.headless = True
service = Service(executable_path=GeckoDriverManager().install())
options= Options()
profile_path = "/home/cristian/.mozilla/firefox/i42mr4f8.default" 
options.set_preference('profile', profile_path)
driver = webdriver.Firefox(service=service, options=options) #firefox_options=options
default_length = 12

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def check_for_recovery_email(mail, password):
    mailbox = MailBox('imap.gmail.com')
    mailbox.login(mail, password, initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg
    last_body = [msg.text for msg in mailbox.fetch(AND(all=True))][-1]
    last_body = last_body.strip().splitlines()
    #print(last_body)
    mailbox.logout()
    for string in range(len(last_body)-1):
        try:
            if last_body[string][0] == ">" and len(last_body[string]) == 10:
                return last_body[string][2:]
        except IndexError:
            continue

class RedbButtom:

    def __init__(self, email = None, services = None):
        self.email = email
        self.services = services
        self.bot = driver
        self.is_logged_in = False


    def forgot(self):
        bot = self.bot
        mail, password = mailCredentials()

        bot.get('https://twitter.com')
        "looks for the sign in buttom and click it"
        time.sleep(5)
        bot.find_element_by_link_text("Sign in").click()
        time.sleep(7)
        new_passwd = get_random_string(default_length)
        print("esta es la contra nueva", new_passwd)
        try:
            bot.find_element_by_link_text("Forgot password?").click()
        except:
            bot.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[7]/div/span/span").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"))).send_keys(mail)
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div"))).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div"))).click()
        time.sleep(5)
        path = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,path))).click() #aca va el next
        time.sleep(7)
        #aca ingresamos codigo
        codigo = check_for_recovery_email(mail, password)
        path_email_code = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,path_email_code ))).send_keys(codigo)
        #aca apretamos el voton de verify
        time.sleep(5)
        path_verify = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,path_verify ))).click()
        #aca ingresamos contrasenias
        path_input_first = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input" #aca va el primer inglreso de nueva contrasenia
        path_input_second = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_input_first))).send_keys(new_passwd)
        time.sleep(7)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_input_second))).send_keys(new_passwd)
        time.sleep(4)
        path_reset_passwd = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_reset_passwd))).click()
        return True
