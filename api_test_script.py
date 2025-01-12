import requests

# Адрес вашего API
API_URL = "http://127.0.0.1:8000/api/tasks/"

# Данные для создания задачи
task_data = {
    "title": "Сделать тестовое задание на Python разработчика"
}

try:
    # Отправляем POST-запрос
    response = requests.post(API_URL, json=task_data)

    # Проверяем успешность запроса
    if response.status_code == 201:
        print("Задача успешно создана!")
        print("Ответ API:", response.json())
    else:
        print(f"Не удалось создать задачу. Код ответа: {response.status_code}")
        print("Ответ API:", response.json())
except requests.exceptions.RequestException as e:
    print("Произошла ошибка при запросе:", e)
