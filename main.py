from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "target account"
USERNAME = "your username"
PASSWORD = "your pass"
chrome_driver_path = "chrome driver location"

class InstaFollower:
    def __init__(self):
        s = Service(chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.maximize_window()
        self.driver.get("http://instagram.com/")
        time.sleep(6)
        terms = self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        terms.click()

    def login(self):
        username_input = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(USERNAME)
        username_input.send_keys(Keys.ENTER)
        password_input = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

        time.sleep(4)

        notifications_off = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        notifications_off.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")

        time.sleep(2)


    def follow(self):
        followers_scroll = self.driver.find_elements("xpath",
                                                     '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div')
        time.sleep(5)
        for n in range(20):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_scroll)
            time.sleep(2)

        followers_name = self.driver.find_elements("css selector", 'span div div div a span div')
        follow_button = self.driver.find_elements("css selector", 'div._aano  button._acan._acap._acas._aj1-')
        following_state = self.driver.find_elements("css selector", 'button div ._aade')
        for x in range(10):
            if following_state[x].text != "Following" or following_state[x].text != "Requested":
                print(f'{followers_name[x].text}: Followed now')
                follow_button[x].click()
                time.sleep(2)
            else:
                print(f'{followers_name[x].text}: Already Following')

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
