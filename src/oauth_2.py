import json

import oauth2


# def oauth_req(url, access_key, access_secret, http_method="GET", post_body="", http_headers=None):
#     consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
#     access_token = oauth2.Token(key=access_key, secret=access_secret)
#     url_end_point = "https://api.github.com/repos/Tito251/try_to"
#     client = oauth2.Client(consumer, access_token)
#     resp, content = client.request(url_end_point, method=http_method, body=post_body, headers=http_headers)
#     return content

# consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
# access_token = oauth2.Token(key=access_key, secret=access_secret)
# url_end_point = "https://api.github.com/repos/Tito251/try_to"
# client = oauth2.Client(consumer, access_token)
# resp, content = client.request(url_end_point, method=http_method, body=post_body, headers=http_headers)
#
# repos = json.loads(content)
#
# for rep in repos:
#     print(rep['text'])

