#!/usr/bin/env python3

import requests
import argparse

def check_github(u):
    url = "https://github.com/"
    try:
        resp = requests.get(url + u)
        if resp.status_code == 200 or resp.status_code // 100 == 3:
            print(u, " is on GitHub!", sep="")
        elif resp.status_code == 404:
            print(u, " doesn't seem to be on GitHub.", sep="")
        else:
            print("GitHub: status code ", resp.status_code, ".", sep="")
    except Exception as e:
        print("GitHub request failed.")

def check_reddit(u):
    url = "https://www.reddit.com/user/"
    try:
        resp = requests.get(url + u)
        if resp.status_code == 200 or resp.status_code // 100 == 3:
            print(u, " is on reddit!", sep="")
        elif resp.status_code == 404:
            print(u, " doesn't seem to be on reddit.", sep="")
        else:
            print("Reddit: status code ", resp.status_code, ".", sep="")
    except Exception as e:
        print("Reddit request failed.")

def check_twitter(u):
    url = "https://twitter.com/"
    try:
        resp = requests.get(url + u)
        if resp.status_code == 200 or resp.status_code // 100 == 3:
            print(u, " is on Twitter!", sep="")
        elif resp.status_code == 404:
            print(u, " doesn't seem to be on Twitter.", sep="")
        else:
            print("Twitter: status code ", resp.status_code, ".", sep="")
    except Exception as e:
        print("Twitter request failed.")
        
if __name__ == "__main__":
    username = input("Please input a username: ")
    check_github(username)
    check_reddit(username)
    check_twitter(username)