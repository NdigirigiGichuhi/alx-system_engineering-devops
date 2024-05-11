#!/usr/bin/python3

''' Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import csv
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
            name = item.get('name')

        tasks = requests.get(f'{url}/users/{employee_id}/todos')
        todos = tasks.json()

        csv_file = f'{employee_id}.csv'

        main_list = []

        for item in todos:
            my_list = [str(item['userId']), name,
                       str(item['completed']), item['title']]
            main_list.append(my_list)

        with open(csv_file, 'w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(main_list)
