from cred import GetCredentials
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Bot:
    def __init__(self, browser) -> None:
        self.browser = browser

    def login(self, username=GetCredentials.get_username(), password=GetCredentials.get_password()):
        # find username & password input elements
        username_path = 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)'
        username_input = self.browser.find_element(
            By.CSS_SELECTOR, username_path)

        password_path = 'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)'
        password_input = self.browser.find_element(
            By.CSS_SELECTOR, password_path)
        sleep(3)

        username_input.send_keys(username)
        password_input.send_keys(password)

        # find & click on log in button
        login_path = '.L3NKy > div:nth-child(1)'
        login_button = self.browser.find_element(
            By.CSS_SELECTOR, login_path)
        login_button.click()

    def search_for_user(self, user_name) -> None:
        sleep(1)
        search_button_path = 'div.x1iyjqo2 > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)'
        login_button = self.browser.find_element(
            By.CSS_SELECTOR, search_button_path)
        login_button.click()
        sleep(1)

        try:
            search_input_path = '._aauy'
            search_input = self.browser.find_element(
                By.CSS_SELECTOR, search_input_path)
            search_input.send_keys(user_name)
            search_input.send_keys(Keys.ENTER)
        except:
            print('Error: could not search this account.')

        sleep(1)

    def follow_user(self) -> None:
        sleep(2)
        try:
            follow_button_path = 'div._ab9k:nth-child(3) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)'
            self.browser.find_element(
                By.CSS_SELECTOR, follow_button_path).click()
        except:
            print('Error: could not follow this account.')

    def like_posts(self, posts_to_like=0) -> None:
        sleep(2)
        # find & click on first post
        first_post_path = 'div._ac7v:nth-child(1) > div:nth-child(1) > a:nth-child(1)'
        self.browser.find_element(By.CSS_SELECTOR, first_post_path).click()

        counter = 0
        # iterate and like posts
        while counter < posts_to_like:
            sleep(2)
            try:
                # like post
                like_button_path = "._aamw > button:nth-child(1)"
                self.browser.find_element(
                    By.CSS_SELECTOR, like_button_path).click()

                # click on next
                next_button_path = "._aaqg > button:nth-child(1)"
                self.browser.find_element(
                    By.CSS_SELECTOR, next_button_path).click()
                counter += 1
            except:
                counter += 1
                print('Error: could not like one or more posts.')
                continue


if __name__ == "__main__":
    fire_fox = webdriver.Firefox()
    fire_fox.get('https://www.instagram.com/')
    fire_fox.implicitly_wait(5)
    bot = Bot(fire_fox)

    # interact with first account
    bot.login()
    bot.search_for_user('apple')
    bot.search_for_user(Keys.ENTER)
    # bot.follow_user()
    bot.like_posts(10)
    sleep(3)

    # interact with second account
    # fire_fox.get('https://www.instagram.com/')
    # fire_fox.implicitly_wait(5)
    # bot.search_for_user('dachshund')
    # bot.search_for_user(Keys.ENTER)
    # # bot.follow_user()
    # bot.like_posts(10)
    # sleep(2)

    # interact with hashtag
    # fire_fox.get('https://www.instagram.com/')
    # fire_fox.implicitly_wait(5)
    # bot.search_for_user('#f80')
    # bot.search_for_user(Keys.ENTER)
    # bot.like_posts(4)

    # sleep(480)
    # fire_fox.close()
