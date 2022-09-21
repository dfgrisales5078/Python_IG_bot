from bot import Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":
    fire_fox = webdriver.Firefox()
    fire_fox.get('https://www.instagram.com/')
    fire_fox.implicitly_wait(5)

    bot = Bot(fire_fox)
    bot.login()
    bot.search_for_user('jeffbezos')
    bot.search_for_user(Keys.ENTER)

    bot.follow_user()
    bot.like_posts(5)

    # interact with another account
    fire_fox.get('https://www.instagram.com/')
    fire_fox.implicitly_wait(5)
    bot.search_for_user('mark zuckerberg')
    bot.search_for_user(Keys.ENTER)
    bot.follow_user()
    bot.like_posts(5)

    # interact with hashtag
    fire_fox.get('https://www.instagram.com/')
    fire_fox.implicitly_wait(5)
    bot.search_for_user('#f80')
    bot.like_posts(5)

    # sleep(480)
    # fire_fox.close()
