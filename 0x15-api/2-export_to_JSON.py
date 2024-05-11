#!/usr/bin/python3

''' Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        response = requests.get(f'{url}/users?id={employee_id}')

        data = response.json()

        for item in data:
            name = item.get('username')

        tasks = requests.get(f'{url}/users/{employee_id}/todos')
        todos = tasks.json()

        for todo in todos:
            todo['task'] = todo['title']
            todo['username'] = name
            todo.pop('title')
            todo.pop('userId')
            todo.pop('id')

        my_dict = {employee_id: todos}

        json_file = f'{employee_id}.json'
        with open(json_file, 'w') as file:
            json.dump(my_dict, file)
