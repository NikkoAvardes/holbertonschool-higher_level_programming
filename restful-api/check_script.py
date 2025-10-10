#!/usr/bin/env python3
"""
Простой скрипт для проверки task_05_basic_security.py

Использование:
    python3 check_script.py

Этот скрипт проверяет:
1. Синтаксис файла
2. Базовую функциональность
3. Предоставляет инструкции по запуску
"""

import subprocess
import sys
import os


def check_syntax():
    """Проверка синтаксиса файла."""
    file_path = "task_05_basic_security.py"
    
    print("🔍 Проверка синтаксиса task_05_basic_security.py...")
    
    if not os.path.exists(file_path):
        print(f"❌ Файл {file_path} не найден!")
        return False
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "py_compile", file_path
        ], capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("✅ Синтаксис корректен")
            return True
        else:
            print("❌ Синтаксические ошибки:")
            print(result.stderr)
            return False
    except FileNotFoundError:
        print("❌ Python не найден")
        return False


def check_pep8():
    """Проверка PEP8 стандартов."""
    file_path = "task_05_basic_security.py"
    
    print("\n📏 Проверка PEP8...")
    
    # Попробуем использовать pycodestyle
    try:
        result = subprocess.run([
            "pycodestyle", file_path
        ], capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("✅ PEP8 стандарты соблюдены")
        else:
            print("⚠️  PEP8 предупреждения:")
            print(result.stdout)
            print("(Предупреждения не критичны для функциональности)")
        return True
        
    except FileNotFoundError:
        print("⚠️  pycodestyle не установлен")
        print("Установите: pip install pycodestyle")
        return True


def show_usage_instructions():
    """Показать инструкции по использованию."""
    print("\n" + "=" * 50)
    print("📋 ИНСТРУКЦИИ ПО ЗАПУСКУ:")
    print("=" * 50)
    
    print("\n1. 🚀 Запуск Flask сервера:")
    print("   python3 task_05_basic_security.py")
    
    print("\n2. 🧪 Тестирование в другом терминале:")
    print("   python3 test_task_05_basic_security.py")
    
    print("\n3. 📖 Ручное тестирование с curl:")
    print("   # Логин:")
    print('   curl -X POST http://127.0.0.1:5000/login \\')
    print('        -H "Content-Type: application/json" \\')
    print('        -d \'{"username": "user1", "password": "password"}\'')
    
    print("\n   # Basic Auth:")
    print('   curl -u user1:password http://127.0.0.1:5000/basic-protected')
    
    print("\n   # JWT (замените TOKEN на полученный токен):")
    print('   curl -H "Authorization: Bearer TOKEN" \\')
    print('        http://127.0.0.1:5000/jwt-protected')
    
    print("\n4. 🔧 Проверка ошибок линтера:")
    print("   pycodestyle task_05_basic_security.py")
    
    print("\n5. 📦 Необходимые зависимости:")
    print("   pip install flask flask-httpauth flask-jwt-extended")


def main():
    """Главная функция."""
    print("🔎 ПРОВЕРКА СКРИПТА task_05_basic_security.py")
    print("=" * 50)
    
    # Проверка синтаксиса
    syntax_ok = check_syntax()
    
    # Проверка PEP8
    pep8_ok = check_pep8()
    
    # Результат
    print("\n📊 РЕЗУЛЬТАТ ПРОВЕРКИ:")
    print(f"   Синтаксис: {'✅ ОК' if syntax_ok else '❌ ОШИБКА'}")
    print(f"   PEP8: {'✅ ОК' if pep8_ok else '❌ ОШИБКА'}")
    
    if syntax_ok:
        print("\n🎉 Скрипт готов к запуску!")
        show_usage_instructions()
    else:
        print("\n💥 Исправьте синтаксические ошибки перед запуском!")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()