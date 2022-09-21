from cred import getCredentials
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Bot:
    def __init__(self, browser) -> None:
        self.browser = browser

    def login(self, username=getCredentials.get_username(), password=getCredentials.get_password()):
        # find username & password input elements
        username_input = browser.find_element(
            "css selector", "input[name='username']")
        password_input = browser.find_element(
            "css selector", "input[name='password']")
        sleep(3)

        username_input.send_keys(username)
        password_input.send_keys(password)

        # find & click on log in button
        login_button = browser.find_element(
            "xpath", "//button[@type='submit']")
        login_button.click()

    def search_for_key(self, search_key) -> None:
        sleep(2)
        search_input = browser.find_element(
            "css selector", "input[placeholder='Search']")
        search_input.send_keys(search_key)
        search_input.send_keys(Keys.ENTER)

    def follow_user(self) -> None:
        sleep(3)
        follow_button_path = "._ab9- > div:nth-child(1)"

        # private
        # "._abb3 > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)"
        # "div._ab9o:nth-child(1) > button:nth-child(1)"

        browser.find_element(
            By.CSS_SELECTOR, follow_button_path).click()

    def like_posts(self, amount=50) -> None:
        # find & click on first post
        browser.find_element(By.CLASS_NAME, "_aagw").click()

        counter = 0
        # iterate and like posts
        while counter <= amount:
            sleep(2)
            # like post
            like_button_path = "._aamw > button:nth-child(1)"
            browser.find_element(By.CSS_SELECTOR, like_button_path).click()

            # click on next
            next_button_path = "._aaqg > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)"
            browser.find_element(By.CSS_SELECTOR, next_button_path).click()
            counter += 1


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get('https://www.instagram.com/')
    browser.implicitly_wait(5)

    bot = Bot(browser)
    bot.login()

    bot.search_for_key('mark zuckerberg')
    sleep(3)
    bot.search_for_key(Keys.ENTER)
    sleep(2)

    try:
        bot.follow_user()
    except:
        print('error following user')

    sleep(2)
    bot.like_posts()

    # browser.get('https://www.instagram.com/')
    # sleep(480)
    # browser.close()
