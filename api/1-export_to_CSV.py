import json
import requests
import sys
import csv

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

# Create and open the CSV file for writing
user_id = sys.argv[1]
csv_file_name = f'{user_id}.csv'
with open(csv_file_name, mode='w', newline='') as csv_file:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row to the CSV file

    for finished_task in completed_task_title:
        # Write the data for each completed task to the CSV file
        writer.writerow({
            'USER_ID': user_id,
            'USERNAME': user_name,
            'TASK_COMPLETED_STATUS': 'Completed',
            'TASK_TITLE': finished_task
        })

print(f'Employee {user_name} is done with tasks ({task}/{len(results)}).')
print(f'Task data has been exported to {csv_file_name}.')
