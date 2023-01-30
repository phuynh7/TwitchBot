from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from login_details import email, password


class bot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/owner/chromedriver_win32/chromedriver.exe')
    def login(self):
        self.driver.maximize_window()
        self.driver.get('https://www.twitch.com/')
        self.driver.implicitly_wait(20)

        
        login = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div')
        login.click()

    def twitch_login(self):
        # login
        self.driver.implicitly_wait(20)
        user_field = self.driver.find_element("xpath","/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[1]/div/div[2]/input")
        pw_field = self.driver.find_element('xpath','/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input' )
        login_button = self.driver.find_element('xpath','/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button' )

        # enter
        user_field.send_keys(email)
        pw_field.send_keys(password)
        
        login_button.click()
    def clicked(self):
        log = self.driver.find_element("xpath", "/html/body/div[3]/div/div/div/div/div/div/div/div[3]/div[2]/button")
        log.click()
    def xqc_stream(self):
        mute = self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div/div[2]/div/section/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/article/div[1]/div/div[1]/div[1]/a/div/button/h3")
        mute.click()
        




bot = bot()
bot.login()
bot.twitch_login()
bot.clicked()
bot.xqc_stream()