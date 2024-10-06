import requests

def get_user_by_group():
    responce  = requests.get
def get_all_users():
    response = requests.get('http://users/list')
    if response.status_code == 200:
        users_data = response.json()
        print(users_data)
    else:
        print(f"Error: {response.status_code}")

def get_user_by_id(user_id):
    response = requests.get(f'http://users/list/{user_id}')
    if response.status_code == 200:
        user_data = response.json()
        print(user_data)
    else:
        print(f"Error: {response.status_code}")

def get_user_groups():
    response = requests.get('http://users/list/groups')
    if response.status_code == 200:
        user_data = response.json()
        print (user_data)
    else: 
        print (f"Error: {response.status_code}")