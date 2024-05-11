#!/usr/bin/python3

import requests
import json
import sys

url = 'https://jsonplaceholder.typicode.com'
employee_id = sys.argv[1]
response = requests.get(f'{url}/users?id={employee_id}')

data = response.json()

for item in data:
    name = item.get('name')


tasks = requests.get(f'{url}/users/{employee_id}/todos')
todos = tasks.json()
my_list = []
completed = 0
total = 0

for item in todos:
    total += 1
    if item['completed']:
        completed += 1

print(f'Employee {name} is done with tasks {completed}/{total}')

for item in todos:
    if item['completed']:
        print('\t', item['title'])
