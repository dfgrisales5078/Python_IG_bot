from cred import getCredentials
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        browser.find_element("xpath", "//div['Log in']").click()
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


class InteractWithAcount:
    def __init__(self, browser):
        self.browser = browser

    def follow_user(self):
        browser.find_element(
            "xpath", "//div['Follow']").click()
        # browser.find_element(
        #     By.CLASS_NAME, "_aacl _aaco _aacw _aad6 _aade").click()

    def like_posts(self, amount=2):
        browser.find_element(By.CLASS_NAME, "_aagw").click()

        counter = 1
        while counter <= amount:
            sleep(2)
            like_button = browser.find_element(By.CLASS_NAME, "_ab6-")
            browser.execute_script("arguments[0].click();", like_button)

            browser.find_element("xpath", "//svg[@aria-label='Next']").click()
            counter += 1


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    home_page = HomePage(browser)

    login_page = home_page.go_to_login_page()
    login_page.login(getCredentials.get_username(),
                     getCredentials.get_password())

    search = searchBox(browser)
    search.search_for_key('ragy_cdj')
    sleep(3)
    search.search_for_key(Keys.ENTER)
    sleep(2)

    interaction = InteractWithAcount(browser)
    # interaction.follow_user()

    # sleep(15)

    interaction.like_posts()

    browser.get('https://www.instagram.com/')

    # sleep(480)
    # browser.close()


# like button --- class="_abl-" --- class="_aamw"
# next post ---- class="_abl-" ---- class=" _aaqg _aaqh"
