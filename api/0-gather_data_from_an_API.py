'''
This module get data from todo api and write the data to a csv file
'''

import json
import requests
import sys


todo_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'


req = requests.get(todo_url)
results = json.loads(req.text)

task = 0
completed_task_title = []
user_name = ''
for result in results:
    if result['completed'] == True:
        task = task + 1
        completed_task_title.append(result['title'])
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(result['userId']))
    user = json.loads(users.text)
    user_name = user['name']


print('Employee {} is done with tasks({}/{}):'.format(user_name, task, len(results)))
for finished_task in completed_task_title:
    print('\t {}'.format(finished_task))
