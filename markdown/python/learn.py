#!/bin/python
# -*- coding: utf8 -*-

import hashlib
import time
import json
import urllib.parse
import sys
import requests
import os.path


def join_array(param):
    str_data=''
    sorted_x = sorted(param.items(), key=lambda param : param[0])
    for x in range(len(sorted_x)):
        for i in range(len(sorted_x[x])):
            str_data=str_data+str(sorted_x[x][i])
    return str_data

def md5(str):
    m = hashlib.md5()
    str_bytes = str.encode('utf-8')
    m.update(str_bytes)
    return m.hexdigest()

def set_token(secretkey,param,payload=None):
    token = join_array(param)+secretkey
    if payload:
        token = token+payload
    return md5(token)

def get_url(url, param):
    str_data=""
    for x in param:
        str_data += "&" + x + "=" + str(param[x])
    return url + "?" + str_data[1:]

# def byteify(input):
#     if isinstance(input, dict):
#         return {byteify(key): byteify(value)
#                 for key, value in input.iteritems()}
#     elif isinstance(input, list):
#         return [byteify(element) for element in input]
#     elif isinstance(input, unicode):
#         return input.encode('utf-8')
#     else:
#         return input

if __name__ == '__main__' :
    print ('usage: python3 config.py "version=7002&channel=100"')

    param = {"plat":0, "version":8066, "appid":0, "channel":201, "imei":'860850022243858125452461', "sinceid":0, "encrypt":0, "_t":int(time.time())}
    if len(sys.argv) > 1:
        arg = urllib.parse.parse_qs(sys.argv[1])
        for k in arg:
            if param.has_key(k):
                param[k] = arg[k][0]

    url = 'http://config.mobile.kugou.com/api/v2/config/index'
    secretkey = 'config_ekKZ5v'

    param["sign"]=set_token(secretkey, param)

    url = get_url(url, param)
    # print url
    r = requests.get(url)

    jObj = json.loads(r.text)
    sinceid = jObj["data"]["sinceid"]
    profile = jObj["data"]["profile"]
    profile["sinceid"] = sinceid
    confStr = json.dumps(profile, indent=4, sort_keys=True)

    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config")
    print ("updating file: " + path)

    f = open(path, 'w')
    f.write(confStr)
    f.close()
