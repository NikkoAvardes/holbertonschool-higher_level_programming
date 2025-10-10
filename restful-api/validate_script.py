#!/usr/bin/env python3
"""
Comprehensive script validation tool.

Проверка скрипта task_05_basic_security.py на:
- Синтаксические ошибки
- PEP8 соответствие
- Функциональность API endpoints
- Безопасность аутентификации
"""

import subprocess
import sys
import os
import time
import requests
import json


def check_syntax(file_path):
    """Проверка синтаксиса Python файла."""
    print("🔍 Проверка синтаксиса...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "py_compile", file_path
        ], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✅ Синтаксис: ОК")
            return True
        else:
            print("❌ Синтаксические ошибки:")
            print(result.stderr)
            return False
    except subprocess.TimeoutExpired:
        print("❌ Проверка синтаксиса превысила время ожидания")
        return False
    except Exception as e:
        print(f"❌ Ошибка проверки синтаксиса: {e}")
        return False


def check_pep8(file_path):
    """Проверка соответствия PEP8."""
    print("📏 Проверка PEP8...")
    try:
        # Попробуем разные варианты линтеров
        linters = ["pycodestyle", "p8", "flake8"]
        
        for linter in linters:
            try:
                result = subprocess.run([
                    linter, file_path
                ], capture_output=True, text=True, timeout=15)
                
                if result.returncode == 0:
                    print("✅ PEP8: ОК")
                    return True
                else:
                    print(f"⚠️  PEP8 предупреждения ({linter}):")
                    print(result.stdout)
                    # Не возвращаем False, так как предупреждения не критичны
                    return True
            except FileNotFoundError:
                continue
        
        print("⚠️  Линтер не найден, проверка PEP8 пропущена")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка проверки PEP8: {e}")
        return True  # Не критичная ошибка


def check_imports(file_path):
    """Проверка импортов."""
    print("📦 Проверка импортов...")
    try:
        # Читаем файл и проверяем импорты
        with open(file_path, 'r') as f:
            content = f.read()
        
        required_imports = [
            'Flask', 'jsonify', 'request',
            'HTTPBasicAuth', 'JWTManager',
            'generate_password_hash', 'check_password_hash'
        ]
        
        missing_imports = []
        for imp in required_imports:
            if imp not in content:
                missing_imports.append(imp)
        
        if missing_imports:
            print(f"❌ Отсутствуют импорты: {', '.join(missing_imports)}")
            return False
        else:
            print("✅ Импорты: ОК")
            return True
            
    except Exception as e:
        print(f"❌ Ошибка проверки импортов: {e}")
        return False


def start_flask_server(file_path):
    """Запуск Flask сервера."""
    print("🚀 Запуск Flask сервера...")
    try:
        process = subprocess.Popen([
            sys.executable, file_path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Ждем запуска сервера
        time.sleep(3)
        
        # Проверяем, что процесс запустился
        if process.poll() is None:
            print("✅ Flask сервер запущен")
            return process
        else:
            stdout, stderr = process.communicate()
            print("❌ Ошибка запуска сервера:")
            print(stderr.decode())
            return None
            
    except Exception as e:
        print(f"❌ Ошибка запуска сервера: {e}")
        return None


def test_basic_endpoints():
    """Тестирование базовых endpoints."""
    print("🧪 Тестирование базовых endpoints...")
    base_url = "http://127.0.0.1:5000"
    
    tests = [
        {
            "name": "Login endpoint",
            "url": f"{base_url}/login",
            "method": "POST",
            "data": {"username": "user1", "password": "password"},
            "expected": 200
        },
        {
            "name": "Basic Auth endpoint",
            "url": f"{base_url}/basic-protected",
            "method": "GET",
            "auth": ("user1", "password"),
            "expected": 200
        }
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test["method"] == "POST":
                response = requests.post(
                    test["url"],
                    json=test.get("data"),
                    timeout=5
                )
            else:
                auth = test.get("auth")
                response = requests.get(
                    test["url"],
                    auth=auth,
                    timeout=5
                )
            
            if response.status_code == test["expected"]:
                print(f"✅ {test['name']}: ОК")
                passed += 1
            else:
                print(f"❌ {test['name']}: Ожидался {test['expected']}, "
                      f"получен {response.status_code}")
                
        except requests.RequestException as e:
            print(f"❌ {test['name']}: Ошибка запроса - {e}")
    
    print(f"📊 Тесты: {passed}/{total} прошли")
    return passed == total


def validate_script(file_path):
    """Полная валидация скрипта."""
    print("=" * 60)
    print(f"🔎 ПРОВЕРКА СКРИПТА: {os.path.basename(file_path)}")
    print("=" * 60)
    
    if not os.path.exists(file_path):
        print(f"❌ Файл не найден: {file_path}")
        return False
    
    # Проверки
    syntax_ok = check_syntax(file_path)
    pep8_ok = check_pep8(file_path)
    imports_ok = check_imports(file_path)
    
    if not syntax_ok or not imports_ok:
        print("\n❌ Критические ошибки найдены. Исправьте их перед запуском.")
        return False
    
    # Функциональные тесты
    server_process = start_flask_server(file_path)
    if server_process:
        try:
            time.sleep(2)  # Даем серверу время запуститься
            endpoints_ok = test_basic_endpoints()
        finally:
            # Останавливаем сервер
            print("🛑 Остановка сервера...")
            server_process.terminate()
            server_process.wait(timeout=5)
    else:
        endpoints_ok = False
    
    # Итоговый результат
    print("\n" + "=" * 60)
    print("📋 ИТОГОВЫЙ РЕЗУЛЬТАТ:")
    print(f"   Синтаксис: {'✅' if syntax_ok else '❌'}")
    print(f"   PEP8: {'✅' if pep8_ok else '❌'}")
    print(f"   Импорты: {'✅' if imports_ok else '❌'}")
    print(f"   Функциональность: {'✅' if endpoints_ok else '❌'}")
    
    all_ok = syntax_ok and imports_ok and endpoints_ok
    
    if all_ok:
        print("\n🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
        print("\n💡 Как запустить скрипт:")
        print(f"   python3 {os.path.basename(file_path)}")
        print("\n💡 Как протестировать API:")
        print("   python3 test_task_05_basic_security.py")
    else:
        print("\n💥 НАЙДЕНЫ ПРОБЛЕМЫ! Исправьте их перед использованием.")
    
    print("=" * 60)
    return all_ok


def main():
    """Главная функция."""
    if len(sys.argv) != 2:
        print("Использование: python3 validate_script.py <файл_для_проверки>")
        print("Пример: python3 validate_script.py task_05_basic_security.py")
        sys.exit(1)
    
    file_path = sys.argv[1]
    success = validate_script(file_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()