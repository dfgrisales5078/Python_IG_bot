from time import sleep
from selenium import webdriver


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


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    home_page = homePage(browser)

    # code
    login_page = home_page.go_to_login_page()
    login_page.login("jeffbezos2023", "8,%w&sWT.87(-)h")
    # endcode

    search = searchBox(browser)
    search.search_for_key('#bmwf80')

    sleep(340)
    browser.close()
