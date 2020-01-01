#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import login

urlapi = "https://es.vikidia.org/w/api.php"
s = login.login(urlapi)

# Get CSRF token
p2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}
r = s.get(url=urlapi, params=p2, headers=login.headers)
d = r.json()
CSRF_TOKEN = d['query']['tokens']['csrftoken']

# Iterate over
listAF = s.get(urlapi + '?action=query&list=abuselog&aflfilter=5&aflprop=ids|user|title&afllimit=10&format=json', headers=login.headers)
listAF = listAF.json()
for i in listAF['query']['abuselog']:
    p3 = {
        "action": "block",
        "user": i['user'],
        "expiry": "infinite",
        "reason": "Aurora: cuenta spam",
        "nocreate": "true",
        "autoblock": "true",
        "token": CSRF_TOKEN,
        "format": "json"
    }

    r = s.post(urlapi, data=p3, headers=login.headers)
    print(r.json())

