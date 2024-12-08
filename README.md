# Структура проекта
Простой проект, демонстрирующий общую структуру проекта и основные технологии.

### Запуск проекта
В терминале запустите команду
```commandline
uvicorn sample_project.main:app
```
После запуска приложения, для получение статистики обратитесь на [endpoint](http://localhost:8000/statistic?date=2024-12-01)

### Запуск тестов
Для запуска тестов установите dev зависимости и введите команду
```commandline
pytest tests
```

