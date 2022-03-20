api_url = "http://10.0.0.17/api/"

username = ""
with open("username", "r") as f:
    username = f.read()

api_url = api_url + username.strip() + "/"


