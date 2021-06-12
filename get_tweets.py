import json
from twitter_utils import *

def get_user_id_from_json(path_to_file):
    with open(path_to_file) as f:
        data = json.load(f)
    data_list = data['data']
    ids = []
    for case in data_list:
        ids.append(case['id'])
    return ids


def main():
    data_path = "user_ID.json"
    outfile_path = "tweets.json"
    bearer_token = auth()

    ids_list = get_user_id_from_json(data_path)
    url = tweet_create_url(ids_list)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    #print(json.dumps(json_response, indent=4, sort_keys=True))

    with open(outfile_path, 'w') as outfile:
        json.dump(json_response, outfile, indent=4, sort_keys=True,)


if __name__ == "__main__":
    main()