#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Login
import requests

headers = {
    'User-Agent': 'AuroraBot/1.0 python-requests/2.21.0', # Puedes dejar este useragent, o cambiarlo a tu gusto
}

def login(urlapi):
    s = requests.Session()
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
        'lgname':"USUARIOBOT",
        'lgpassword':"CONTRASENABOT",
        'lgtoken': LOGIN_TOKEN,
        'format':"json"
    }
    r = s.post(urlapi, data=p1, headers=headers)
    DATA = r.json()
    return s
