# Как проверить скрипт task_05_basic_security.py

## 🔍 Быстрая проверка

```bash
# Простая проверка синтаксиса и PEP8
python3 check_script.py
```

## 📋 Методы проверки скрипта

### 1. Проверка синтаксиса
```bash
python3 -m py_compile task_05_basic_security.py
echo "Если нет ошибок - синтаксис корректен"
```

### 2. Проверка PEP8 стандартов
```bash
# С помощью pycodestyle
pycodestyle task_05_basic_security.py

# Или с помощью flake8 (если установлен)
flake8 task_05_basic_security.py
```

### 3. Запуск и тестирование

#### Запуск сервера:
```bash
python3 task_05_basic_security.py
```

#### Тестирование в другом терминале:
```bash
# Автоматическое тестирование
python3 test_task_05_basic_security.py

# Ручное тестирование
curl -X POST http://127.0.0.1:5000/login \
     -H "Content-Type: application/json" \
     -d '{"username": "user1", "password": "password"}'
```

## 🚀 Полная последовательность проверки

1. **Синтаксис**: `python3 -m py_compile task_05_basic_security.py`
2. **PEP8**: `pycodestyle task_05_basic_security.py`
3. **Запуск**: `python3 task_05_basic_security.py` (в одном терминале)
4. **Тестирование**: `python3 test_task_05_basic_security.py` (в другом терминале)

## 📦 Зависимости

Убедитесь, что установлены необходимые пакеты:
```bash
pip install flask flask-httpauth flask-jwt-extended
```

## 🎯 Ожидаемые результаты

- ✅ Синтаксис корректен
- ✅ PEP8 стандарты соблюдены  
- ✅ Сервер запускается на http://127.0.0.1:5000
- ✅ Все тесты проходят успешно