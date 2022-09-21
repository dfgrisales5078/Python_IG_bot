from cred import GetCredentials
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Bot:
    def __init__(self, browser) -> None:
        self.browser = browser

    def login(self, username=GetCredentials.get_username(), password=GetCredentials.get_password()):
        # find username & password input elements
        username_input = self.browser.find_element(
            "css selector", "input[name='username']")
        password_input = self.browser.find_element(
            "css selector", "input[name='password']")
        sleep(3)

        username_input.send_keys(username)
        password_input.send_keys(password)

        # find & click on log in button
        login_button = self.browser.find_element(
            "xpath", "//button[@type='submit']")
        login_button.click()

    def search_for_key(self, search_key) -> None:
        sleep(2)
        try:
            search_input = self.browser.find_element(
                "css selector", "input[placeholder='Search']")
            search_input.send_keys(search_key)
            search_input.send_keys(Keys.ENTER)
        except:
            print('Error: could not search this account.')

    def follow_user(self) -> None:
        try:
            sleep(3)
            follow_button_path = "._ab9- > div:nth-child(1)"
            self.browser.find_element(
                By.CSS_SELECTOR, follow_button_path).click()
        except:
            print('Error: could not follow this account.')

    def like_posts(self, amount=15) -> None:
        # find & click on first post
        self.browser.find_element(By.CLASS_NAME, "_aagw").click()
        counter = 0

        # iterate and like posts
        while counter <= amount:
            try:
                sleep(2)
                # like post
                like_button_path = "._aamw > button:nth-child(1)"
                self.browser.find_element(
                    By.CSS_SELECTOR, like_button_path).click()

                # click on next
                next_button_path = "._aaqg > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)"
                self.browser.find_element(
                    By.CSS_SELECTOR, next_button_path).click()
                counter += 1
            except:
                counter += 1
                print('Error: could not like one or more posts.')
                continue

            # like last post
            like_button_path = "._aamw > button:nth-child(1)"
            self.browser.find_element(
                By.CSS_SELECTOR, like_button_path).click()


if __name__ == "__main__":
    fire_fox = webdriver.Firefox()
    fire_fox.get('https://www.instagram.com/')
    fire_fox.implicitly_wait(5)

    bot = Bot(fire_fox)
    bot.login()

    bot.search_for_key('diegofgg7')
    sleep(3)
    bot.search_for_key(Keys.ENTER)
    sleep(2)

    bot.follow_user()

    sleep(2)
    bot.like_posts()

    # browser.get('https://www.instagram.com/')
    # sleep(480)
    # browser.close()
