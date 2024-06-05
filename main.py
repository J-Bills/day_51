from config import credential_dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN_SPEED = 100
PROMISED_UP_SPEED = 13
class InternetSpeedTwitterBot:
    
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        #self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0
        self.scammed = None
        self.speed_tweet = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN_SPEED} down/{PROMISED_UP_SPEED} up?"
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,value='//a(contains[@href, "#"])').click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.CLASS_NAME,value='notification-dismiss').click()
        results = self.driver.find_elements(By.XPATH,value='//span(contains[@class, "-large number.result-data-value.download-speed"])')
        self.down = float(results[0])
        self.up = float(results[1])
        if self.down <= PROMISED_DOWN_SPEED and self.up <= PROMISED_UP_SPEED:
            self.scammed = True
    
    def tweet_at_provider(self):
        #Logging In
        self.driver.get('https://x.com')
        self.driver.find_element(By.XPATH, value="//a(contains[@href, '/login'])").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, value='username').send_keys(credential_dict.get('username'))
        self.driver.find_element(By.XPATH, value="//span[text()='Next']//ancestor::button").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.NAME, value='password').send_keys(credential_dict.get('password'))
        self.driver.find_element(By.XPATH, value="//span[text()='Log in']//ancestor::button").click()
        self.driver.implicitly_wait(10)
        
        #sending the tweet
        self.driver.find_element(By.XPATH, value="//div(contains[@role, 'textbox'])").send_keys(self.speed_tweet)
        self.driver.find_element(By.XPATH, value="//span[text()='Post']//ancestor::button").click()
        
def main():
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    if (bot.scammed):
        bot.tweet_at_provider()
    else:
        print('Not Scammed')
