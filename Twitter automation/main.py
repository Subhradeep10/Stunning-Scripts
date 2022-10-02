from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "YOUR PATH"
TWITTER_USERNAME = "YOUR USERNAME"
TWITTER_PASSWORD = "YOUR PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = 0.0
        self.up = 0.0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.LINK_TEXT, 'GO')
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                           '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             ' 3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A"
                        "%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
        time.sleep(4)
        username = self.driver.find_element(By.CSS_SELECTOR, 'input')
        username.send_keys(TWITTER_USERNAME)
        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                               '2]/div[2]/div[1]/div/div/div[6]')
        next_button.click()

        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                      '3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
        login_button.click()

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when " \
                f"I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? (It is bot, Using it for Testing Purpose.) "
        tweet_a_tweet = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_a_tweet.send_keys(tweet)
        self.driver.quit()


internet_speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed_twitter_bot.get_internet_speed()
if float(internet_speed_twitter_bot.up) < PROMISED_UP or float(internet_speed_twitter_bot.down) < PROMISED_DOWN:
    internet_speed_twitter_bot.tweet_at_provider()
