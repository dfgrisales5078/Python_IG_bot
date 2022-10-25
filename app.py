# Diego Grisales & Ragy Costa De Jesus
# CNT - 4104 Project
# Flask API endpoint
# Fall 2022

from bot import Bot
from flask import Flask, request, redirect, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep


# /getlikes is the endpoint API that triggers get_likes() to be executed

app = Flask(__name__)


@app.route('/getlikes', methods=['GET', 'POST'])
def get_likes():

    # get parameters passed to the API endpoint via POST payload
    username = request.form['username']
    posts = request.form['posts']
    posts = int(posts)
    follow = request.form['follow']

    # initialize browser make 'headless'
    options = webdriver.FirefoxOptions()
    options.headless = False
    fire_fox = webdriver.Firefox(options=options)

    # go to instagram.com & login
    fire_fox.get('https://www.instagram.com/')
    fire_fox.implicitly_wait(5)
    bot = Bot(fire_fox)
    bot.login()

    # interact with account based on parameters passed
    bot.search_for_user(username)
    bot.search_for_user(Keys.ENTER)
    if follow == "on":
        bot.follow_user()
    bot.like_posts(posts)

    sleep(3)
    fire_fox.close()

    # redirect back to the website after code is executed
    return redirect('https://main.d1s1ozkoy4xkk0.amplifyapp.com/')
