
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:41:44 2023

@author: ANSHIT
"""

import requests
import json 

response = requests.get('http:/127.0.0.1:8000/Skills/')

print(response.status_code)
print(response.text)

Url = 'http://127.0.0.1:8000/Tests/'

Data = {
    "id": 21,
    "EmployeeName": "Anshit Ransingh",
    "EmployeeId": "BBIIN0001",
    "EmployeeDesignation": "Data Engineer",
    "CurrentProject": "Nameless Wonder",
    "Email": "anshit@test.com",
    "ContactNumber": "1232131230",
    "EmployeeSkills": [
        {
            "SkillName": "Python"
        },
        {
            "SkillName": "SQL"
        }
    ]
}
json_object = json.dumps(Data, indent = 4) 
print(json_object)
print(type(json_object))

response = requests.post(Url, json = Data)
response = requests.get(Url)

response = requests.delete(Url)
print(response.text)
print(response.status_code)

