#!/usr/bin/env python

from configparser import ConfigParser
import requests

def createTicket(username,url):
    """formatting HTML payload for service now ticket"""
    parser = ConfigParser()

    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    auth = {"user": parser.get("SERVICE NOW", "user"),
            "pass": parser.get("SERVICE NOW", "pass")}

    message = 'The User: %s has created a ticekt at BITS Stop!\n' % (username)
    body = {'u_requested_for_usr': username,
            'short_description': 'User: %s created a ticket at the bits service desk useing their ID Badge' % (username),
            'assignment_group': 'Service Desk',
            'state': '7',
            'work_notes': message}

    resp = requests.post(url, auth=(auth["user"], auth["pass"]), headers=headers, json=body)

    if resp.status_code == 201:
        print('couldnt make ticket')
    else:
        print('couldnt make ticket')

def main():
    username = 'username'
    url = 'url'
    createTicket(username,url)

if __name__ == "__main__":
    main()
