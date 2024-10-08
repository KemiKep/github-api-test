# Тест работы с GitHub API

## Описание

Этот проект представляет собой автоматический тест для работы с GitHub API. Скрипт выполняет следующие действия:

1. Создает новый публичный репозиторий на GitHub.
2. Проверяет его наличие в списке репозиториев.
3. Удаляет созданный репозиторий.

## Установка

1. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

## Настройка

В файле `.env` необходимо указать следующие переменные окружения:

- `GITHUB_USERNAME` — ваш логин на GitHub.
- `GITHUB_TOKEN` — ваш личный токен доступа к GitHub API.
- `REPO_NAME` — имя репозитория, который будет создан, проверен и удален.

### Примечание

Для создания личного токена GitHub:

1. Перейдите в настройки вашего профиля на GitHub.
2. Выберите "Developer settings".
3. Выберите "Personal access tokens".
4. Нажмите "Generate new token", выберите необходимые права доступа (например, `repo`) и создайте токен.

## Запуск теста

Запустите скрипт:

```sh
python test_api.py
```

Скрипт выполнит следующие действия:

- Создаст новый репозиторий.
- Проверит его наличие.
- Удалит созданный репозиторий.
