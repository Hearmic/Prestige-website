import requests

def get_all_users():
    response = requests.get('http://users:8000/users/list')
    if response.status_code == 200:
        user = response.json()
        return user
    else:
        return(f"Error: {response.status_code}")

def get_user_by_id(user_id):
    response = requests.get(f'http://users:8000/list/{user_id}')
    if response.status_code == 200:
        user_data = response.json()
        print(user_data)
        return user_data
    else:
        print(f"Error: {response.status_code}")
        return None

def get_user_groups():
    response = requests.get('http://users/list/groups')
    if response.status_code == 200:
        user_data = response.json()
        print (user_data)
    else: 
        print (f"Error: {response.status_code}")

def get_lesson_info(lesson):
    try:
        user_data = get_user_by_id(lesson.teacher_id)
        first_name = user_data['first_name']
        surname = user_data['surname']
        return f"{lesson.lesson_type} {first_name} {surname}"
    except (KeyError, TypeError):
        # Handle errors if user data is missing or invalid
        return f"{lesson.lesson_type} (Teacher information not found)"