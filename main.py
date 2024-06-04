import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class InternetSpeedTwitterBot:
    
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        #self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,value='//a(contains[@href, "#"])').click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.CLASS_NAME,value='notification-dismiss').click()
        results = self.driver.find_elements(By.XPATH,value='//span(contains[@class, "-large number.result-data-value.download-speed"])')
        self.down = results[0]
        self.up = results[1]
        
    
    # def tweet_at_provider(self):
    #     self.driver.get('https://x.com')
    #     self.driver.find_element(By.XPATH, value="//a(contains[@href, '/login'])").click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(By.NAME, value='text').send_keys()
        
def main():
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
