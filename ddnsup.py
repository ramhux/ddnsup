#!/usr/bin/env python3

import base64
import urllib.request as urlreq

def authdict(user, password):
    userpass = bytes(user + ':' + password, 'ascii')
    userpass = base64.b64encode(userpass).decode('ascii')
    d = { 'Authorization': 'Basic ' + userpass }
    return d
    
def updatedns(user, password, domain):
    url = 'https://www.ovh.com/nic/update?system=dyndns&hostname=' + domain
    req = urlreq.Request(url, headers=authdict(user, password))
    r = urlreq.urlopen(req)
    return r
