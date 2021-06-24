import json
import os
from twitter_utils import *

def get_user_id_from_json(path_to_file):
    with open(path_to_file) as f:
        data = json.load(f)
    data_list = data['data']
    ids = []
    names = []
    for case in data_list:
        ids.append(case['id'])
        names.append(case['username'])
    return ids, names


def main():
    data_path = "user_ID.json"
    
    bearer_token = auth()
    headers = create_headers(bearer_token)
    ids_list, username_list = get_user_id_from_json(data_path)
    #sername_list = ["Ambitocom", "clarincom", "C5N", "LANACION", "cronica", "infobae", "pagina12"]
    if not os.path.exists('data'):
        os.makedirs('data')
        
    for username in username_list:

        url = search_create_url(username, results=100)
        json_response = connect_to_endpoint(url, headers)

        with open(f"data/{username}_tweets.json", 'w') as outfile:
            json.dump(json_response, outfile, indent=4, sort_keys=True,)


if __name__ == "__main__":
    main()