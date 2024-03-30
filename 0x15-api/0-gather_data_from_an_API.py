#!/usr/bin/python3
"""Module returns info about a given employee ID"""

import requests
import sys
import json

url = "https://jsonplaceholder.typicode.com"

employee_id = sys.argv[1]

user_url = f'{url}/users?id={employee_id}'

response = requests.get(user_url)
data = response.text
data = json.loads(data)
name = data[0]['name']

todos_url = f'{url}/todos?userId={employee_id}'
todos_response = requests.get(todos_url)
tasks = todos_response.text
tasks = json.loads(tasks)

complete = 0
all_todos = len(tasks)
completed_tasks = []

for task in tasks:
    if task.get('completed'):
        complete += 1
        completed_tasks.append(task)

print(f'Employee {name} is done with tasks {complete}/{all_todos}:')

for task in completed_tasks:
        print(f'\t {task.get("title")}')
