from cred import getCredentials
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = browser.find_element(
            "css selector", "input[name='username']")
        password_input = browser.find_element(
            "css selector", "input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element(
            "xpath", "//button[@type='submit']")
        login_button.click()
        sleep(5)


class homePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element("xpath", "//div['Log in']").click()
        sleep(2)
        return LoginPage(self.browser)


class searchBox:
    def __init__(self, browser):
        self.browser = browser

    def search_for_key(self, search_key):
        search_input = browser.find_element(
            "css selector", "input[placeholder='Search']")
        search_input.send_keys(search_key)
        search_input.send_keys(Keys.ENTER)


# class="_ac7v _aang"
class searchResults:
    def __init__(self, browser):
        self.browser = browser

    def click_on_first_post(self):
        post = browser.find_element(
            "css selector", "a[role='link']").click()


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    home_page = homePage(browser)

    login_page = home_page.go_to_login_page()
    login_page.login(getCredentials.get_username(),
                     getCredentials.get_password())

    search = searchBox(browser)
    search.search_for_key('#bmwf80')
    sleep(1)
    search.search_for_key(Keys.ENTER)

    post = searchResults(browser)
    post.click_on_first_post()

    sleep(360)
    browser.close()
