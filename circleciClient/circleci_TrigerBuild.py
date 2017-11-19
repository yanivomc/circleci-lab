import os
import json
import requests
from circleclient import circleclient

token = "f2c6a6d316fac70907638112dea96a3c41d4dbc3"
client = circleclient.CircleClient(token)

#retrive User Data
user = client.user.info()
projects = client.projects.list_projects()

print ("user projects are: ", user['num_projects_followed'])

print ("User projects are: ", projects)

def traverse(obj, path=None, callback=None):
    if path is None:
        path = []

    if isinstance(obj, dict):
        value = {k: traverse(v, path + [k], callback)
                 for k, v in obj.items()}
    elif isinstance(obj, list):
        value = [traverse(elem, path + [[]], callback)
                 for elem in obj]
    else:
        value = obj

    if callback is None:  # if a callback is provided, call it to get the new value
        return value
    else:
        return callback(path, value)



new_data = traverse(user)
# unmark the following to see all user dict key/values

#for key in new_data:
 #  print "key: %s , value: %s" % (key, new_data[key])
