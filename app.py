# from bot import Bot
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from flask import Flask

app = Flask(__name__)


@app.route('/getlikes/', methods=['GET'])
def get_likes():
    return {"test": "hello world"}


if __name__ == "__main__":
    app.run(debug=True)
