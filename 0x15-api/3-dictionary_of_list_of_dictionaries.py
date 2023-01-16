#!/usr/bin/python3
"""
Request from API; Return TODO list progress of all employees
Export this data to JSON
"""
import json
import requests


def all_to_json():
    """return API data"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)


if __name__ == "__main__":
    all_to_json()
