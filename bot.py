# Diego Grisales & Ragy Costa De Jesus
# CNT - 4104 Project (Backend)
# Python/Selenium code for the Instagram bot
# Fall 2022

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
        username_input = self.browser.find_element(
            By.CSS_SELECTOR, "input[name='username']")
        password_input = self.browser.find_element(
            By.CSS_SELECTOR, "input[name='password']")
        sleep(3)

        # type in credentials to username and password input
        username_input.send_keys(username)
        password_input.send_keys(password)

        # find & click on log in button
        login_button = self.browser.find_element(
            By.XPATH, "//button[@type='submit']")
        login_button.click()

    def search_for_user(self, user_name) -> None:
        sleep(2)

        # try to search for username
        try:
            # find search input and enter username information
            search_input = self.browser.find_element(
                "css selector", "input[placeholder='Search']")
            search_input.send_keys(user_name)
            search_input.send_keys(Keys.ENTER)

        # if username cannot be searched for, print error message and quit
        except:
            print('Error: could not search this account.')
            exit(1)
        sleep(1)

    def follow_user(self) -> None:
        sleep(2)

        # try to follow user
        try:
            # search for follow button and click on it if found
            follow_button_path = "._ab9- > div:nth-child(1)"
            self.browser.find_element(
                By.CSS_SELECTOR, follow_button_path).click()

        # print error message if account cannot be followed
        except:
            print('Error: could not follow this account.')

    def like_posts(self, posts_to_like=0) -> None:
        sleep(2)
        # find & click on first post
        self.browser.find_element(By.CLASS_NAME, "_aagw").click()
        counter = 0

        # iterate and like posts while posts_to like > counter
        while counter < posts_to_like:
            sleep(2)

            # try to search for the first post, like it and go to next post
            try:
                # like post
                like_button_path = "._aamw > button:nth-child(1)"
                self.browser.find_element(
                    By.CSS_SELECTOR, like_button_path).click()

                # click on next button to go to next post
                next_button_path = "._aaqg > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)"
                self.browser.find_element(
                    By.CSS_SELECTOR, next_button_path).click()
                counter += 1

            # if a post cannot be found, print error message
            except:
                counter += 1
                print('Error: could not like one or more posts.')
                continue
