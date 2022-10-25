
# Python/Flask API Endpoint

## API endpoint used to work along with Get Instagram Likes website. 

Currently, API is not deployed and therefore must be ran locally in order for it to interact with POST method send by the Instagram Likes Website (https://main.d1s1ozkoy4xkk0.amplifyapp.com/). 

Flask endpoint (app.py) get_likes() method uses code from class Bot to interact with intagram accounts based on the parameters sent on the POST method. Parameters passed are: username (instagram account to interact with), posts (number of posts to like on the account), and follow (determines is account should be followed as well.)

The Bot class was created using selenium to browse instagram and search for specific components using the CSS Selector path of the components. 
