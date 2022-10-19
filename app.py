
from flask import Flask
from flask import request
from time import sleep
from flask import jsonify
from selenium import webdriver
from bot import Bot
from selenium.webdriver.common.keys import Keys


app = Flask(__name__)


@app.route('/getlikes', methods=['GET', 'POST'])
def get_likes():

    username = request.form['username']
    posts = request.form['posts']
    posts = int(posts)
    follow = request.form['follow']

    fire_fox = webdriver.Firefox()
    fire_fox.get('https://www.instagram.com/')
    fire_fox.implicitly_wait(5)
    bot = Bot(fire_fox)
    bot.login()
    bot.search_for_user(username)
    bot.search_for_user(Keys.ENTER)

    if follow == "on":
        bot.follow_user()
    bot.like_posts(posts)

    sleep(3)
    fire_fox.close()

    data = {
        "username": username,
        "posts": posts,
        "follow": follow
    }

    # return 'test'
    return jsonify(data)
