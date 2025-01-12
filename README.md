### **Описание проекта**

Этот проект представляет собой минимальное API для работы с задачами, реализованное на Django REST Framework.

API позволяет:
1. Получать список задач
2. Создавать новые задачи

Каждая задача содержит название (`title`), которое не может быть пустым, и статус выполнения (`is_completed`, по умолчанию False).

---

### **Инструкция по установке и запуску проекта**

#### **1. Клонируйте или создайте проект**

```
git clone https://github.com/KhripkovaNA/DjangoTasksAPI.git
cd DjangoTasksAPI
```

#### **2. Установите зависимости**
Создайте и активируйте виртуальное окружение:

```
python -m venv venv
source venv/bin/activate   # для Linux/MacOS
venv\Scripts\activate      # для Windows
pip install -r requirements.txt
```

#### **3. Примените миграции и запустите сервер**

Перейдите в папку `taskmanager` и выполните миграции для настройки базы данных:

```
cd taskmanager
python manage.py makemigrations
python manage.py migrate
```

Запустите сервер разработки:

```
python manage.py runserver
```

API будет доступно по адресу:
http://127.0.0.1:8000/api/tasks/

#### **4. Запустите проверочный скрипт**
1. Убедитесь, что сервер разработки запущен.

2. Запустите скрипт `test_api_script.py` в корневой директории проекта для проверки API:

```
python test_api_script.py
```
