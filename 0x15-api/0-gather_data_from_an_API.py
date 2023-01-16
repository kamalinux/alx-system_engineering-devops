#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


def display():
    """return API data"""
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    display()
