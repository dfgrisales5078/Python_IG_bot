# Diego Grisales & Ragy Costa De Jesus
# CNT - 4104 Project (Api endpoint)
# Python/Selenium code for the Instagram bot
# Fall 2022

from cred import GetCredentials
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

class Botv2:
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
            search_button_xpath = 'div.x1iyjqo2 > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1)'
            search_button = self.browser.find_element(
                By.CSS_SELECTOR, search_button_xpath)
            search_button.click()

            sleep(2)

            search_box_xpath = '._aauy'
            search_input = self.browser.find_element(
                By.CSS_SELECTOR, search_box_xpath)
            sleep(1)

            search_input.send_keys(user_name)

            user_css_path = '._abm4'

            user = self.browser.find_element(
                By.CSS_SELECTOR, user_css_path)

            user.click()

        # if username cannot be searched for print error message
        except:
            print('Error: could not search this account.')
        sleep(1)

    def follow_user(self) -> None:
        sleep(2)

        # try to follow user
        try:
            # search for follow button and click on it if found
            follow_button_path = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div"
            self.browser.find_element(
                By.XPATH, follow_button_path).click()

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


if __name__ == "__main__":

    # initialize browser make 'headless'
    options = uc.ChromeOptions()
    options.headless = False
    driver = uc.Chrome(use_subprocess=True, options=options)

    # go to instagram.com & login
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(5)
    bot = Botv2(driver)
    bot.login()

    # interact with account based on parameters passed
    bot.search_for_user('ragy_cdj')
    bot.search_for_user(Keys.ENTER)

    bot.follow_user()
    bot.like_posts(3)
