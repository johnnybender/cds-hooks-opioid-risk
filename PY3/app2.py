from flask import Flask
from flask import json

import csv
with open('Fentanyl.csv', 'rb') as f:
    reader = csv.reader(f)
    values = list(reader)

with open('data.json') as json_data:
    x = json.load(json_data)
    number = x['context']['medications'][0]['medicationCodeableConcept']['coding'][0]['code']
    int(number)
    print(number)
    if number in values:
        print("success")
    else:
        print(number)