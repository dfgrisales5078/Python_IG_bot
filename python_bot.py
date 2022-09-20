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
        sleep(2)

        username_input.send_keys(username)
        password_input.send_keys(password)

        # find & click on log in button
        login_button = browser.find_element(
            "xpath", "//button[@type='submit']")
        login_button.click()

    def search_for_key(self, search_key) -> None:
        search_input = browser.find_element(
            "css selector", "input[placeholder='Search']")
        search_input.send_keys(search_key)
        search_input.send_keys(Keys.ENTER)

    def follow_user(self) -> None:
        follow_button_path = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button"

        browser.find_element(
            By.XPATH, follow_button_path).click()
        # browser.find_element(
        #     By.CLASS_NAME, "_aacl _aaco _aacw _aad6 _aade").click()

    def like_posts(self, amount=2) -> None:
        # find & click on first post
        browser.find_element(By.CLASS_NAME, "_aagw").click()

        counter = 1
        while counter <= amount:
            sleep(2)
            # TODO like post
            like_button_path = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
            browser.find_element(By.XPATH, like_button_path).click()

            # TODO click on next
            next_button_path = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button"
            browser.find_element(By.XPATH, next_button_path).click()
            counter += 1


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get('https://www.instagram.com/')
    browser.implicitly_wait(5)

    bot = Bot(browser)
    bot.login()

    bot.search_for_key('ragy_cdj')
    sleep(3)
    bot.search_for_key(Keys.ENTER)
    sleep(2)

    try:
        bot.follow_user()
        sleep(2)
    except:
        print('error following user')

    sleep(2)
    bot.like_posts()

    # browser.get('https://www.instagram.com/')
    # sleep(480)
    # browser.close()
