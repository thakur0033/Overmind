
import requests
import json

def load_keys():
    with open("config/api_keys.json") as f:
        return json.load(f)

def post_to_twitter(content):
    keys = load_keys()
    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {keys['twitter']}",
        "Content-Type": "application/json"
    }
    payload = {"text": content}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def post_to_devto(content, title="AI Thoughts", tags=["ai", "overmind", "technology"]):
    keys = load_keys()
    headers = {
        "Content-Type": "application/json",
        "api-key": keys["devto"]
    }
    article = {
        "article": {
            "title": title,
            "published": True,
            "body_markdown": content,
            "tags": tags
        }
    }
    response = requests.post("https://dev.to/api/articles", headers=headers, json=article)
    return response.json()
