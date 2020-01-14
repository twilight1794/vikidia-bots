#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Login
import requests

headers = {
    'User-Agent': 'AuroraBot/1.0 python-requests/2.21.0',
}

def login(urlapi):
    s = requests.Session()
    n = open('user','r')
    nn = n.read()[:-1]
    p = open('password','r')
    pp = p.read()[:-1]
    p0 = {
        'action':"query",
        'meta':"tokens",
        'type':"login",
        'format':"json"
    }
    r = s.get(url=urlapi, params=p0, headers=headers)
    d = r.json()
    LOGIN_TOKEN = d['query']['tokens']['logintoken']
    p1 = {
        'action':"login",
        'lgname':nn,
        'lgpassword':pp,
        'lgtoken': LOGIN_TOKEN,
        'format':"json"
    }
    r = s.post(urlapi, data=p1, headers=headers)
    DATA = r.json()
    return s
