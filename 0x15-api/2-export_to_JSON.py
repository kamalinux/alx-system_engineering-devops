#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to JSON
"""
import json
import requests
import sys


def to_json():
    """return API data"""
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)


if __name__ == "__main__":
    to_json()
