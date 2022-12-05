
# Python/Flask API Endpoint

## API endpoint used to work along with Get Instagram Likes website. 

Currently, API is not deployed and therefore must be ran locally in order for it to interact with the POST request sent by the Instagram Likes Website (https://main.d1s1ozkoy4xkk0.amplifyapp.com/). The web page is currently deployed using AWS Amplify. 

Flask endpoint get_likes() function in app.py uses code from class Bot to interact with intagram accounts based on the parameters sent on the POST method. Parameters passed are: username (instagram account to interact with), posts (number of posts to like on the account), and follow (determines is account should be followed as well.)

The Bot class was created using selenium to browse instagram and search for specific components using the CSS Selector path of the components. 


## Demo:

https://user-images.githubusercontent.com/54412831/205727587-2359263b-4e08-4df3-bae4-bb314158b6a0.mp4


