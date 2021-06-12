import requests
import os
import json
from twitter_utils import *
"""
This is an adaptation from Twitter's developers github sample code
"""
def main():
    bearer_token = auth()

    username_list = ["Ambitocom", "C5N", "clarincom", "cronica", "infobae", 
    "_IPNoticias", "LANACION", "lanacionmas", "pagina12", "todonoticias"]

    url = userid_create_url(username_list)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))

    with open('user_ID.json', 'w') as outfile:
        json.dump(json_response,outfile, indent=4, sort_keys=True,)


if __name__ == "__main__":
    main()