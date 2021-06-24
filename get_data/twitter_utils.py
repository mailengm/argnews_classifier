import requests
import os
import json

def auth():
    """ Get Bearer token from environment variables
    To set your enviornment variables in your terminal run the following line:
    export 'BEARER_TOKEN'='<your_bearer_token>'
    """
    return os.environ.get("BEARER_TOKEN")

def create_headers(bearer_token):
    """ Create header using the bearer token """
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def userid_create_url(usernames_list):
    """
    Create the URL to get the usernames ID
    """
    # Specify the usernames that you want to lookup below
    separator = ","
    usernames = f"usernames={separator.join(usernames_list).casefold()}"
    user_fields = "user.fields=id"

    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url

def tweet_create_url(userid):
    #tweet_fields = "tweet.fields=lang,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    #separator = ","
    #ids = f"ids={separator.join(userid_list)}"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = f"https://api.twitter.com/2/users/{userid}/tweets"
    return url

def search_create_url(username,results=100):
    url = f"https://api.twitter.com/2/tweets/search/recent?query=from%3A{username}&max_results={results}&user.fields=name"
    print(url)
    return url

def connect_to_endpoint(url, headers):
    """ Connect to endpoint and process the request """
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()