import os
import time
import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

# Загрузка переменных окружения из файла .env
load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

def create_repo():
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    data = {'name': REPO_NAME, 'private': False}
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Проверка на HTTP ошибки
    except RequestException as e:
        print(f"Ошибка при создании репозитория: {e}")
        return False
    if response.status_code == 422:
        print("Репозиторий с таким именем уже существует.")
    else:
        print(response.status_code, response.json())  # Добавлено для отладки
    return response.status_code == 201

def check_repo_exists():
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except RequestException as e:
        print(f"Ошибка при проверке существования репозитория: {e}")
        return False
    return response.status_code == 200

def delete_repo():
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
    except RequestException as e:
        print(f"Ошибка при удалении репозитория: {e}")
        return False
    return response.status_code == 204

if __name__ == "__main__":
    if create_repo():
        print("Репозиторий успешно создан.")
        if check_repo_exists():
            print("Репозиторий существует.")
            if delete_repo():
                print("Репозиторий успешно удалён.")
            else:
                print("Ошибка при удалении репозитория.")
        else:
            print("Репозиторий не найден.")
    else:
        print("Ошибка при создании репозитория.")