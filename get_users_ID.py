import requests
import os
import json

"""
This is an adaptation from Twitter's developers github sample code
"""

def auth():
    """ Get Bearer token from environment variables
    To set your enviornment variables in your terminal run the following line:
    export 'BEARER_TOKEN'='<your_bearer_token>'
    """
    return os.environ.get("BEARER_TOKEN")


def create_url(usernames_list):
    """
    Create the URL to get the usernames ID
    """
    # Specify the usernames that you want to lookup below
    separator = ", "
    usernames = f"usernames= {separator.join(usernames_list)}"
    user_fields = "user.fields=id"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()