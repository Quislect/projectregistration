# diagnostic.py
import json
import os
from models import User

DATA_FILE = "users.json"

def show_file_content():
    """Показывает содержимое файла"""
    print("\n" + "="*50)
    print(f"Проверка файла: {os.path.abspath(DATA_FILE)}")
    print("="*50)
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                content = json.load(f)
                print(f"✅ Файл существует")
                print(f"📊 Количество пользователей в файле: {len(content)}")
                print("\n📝 Содержимое файла:")
                for i, user in enumerate(content, 1):
                    print(f"\n{i}. Логин: {user.get('логин')}")
                    print(f"   Имя: {user.get('имя')}")
                    print(f"   Пароль: {user.get('пароль')}")
        except Exception as e:
            print(f"❌ Ошибка чтения: {e}")
    else:
        print("❌ Файл НЕ существует!")
    
    print("="*50)

def save_test():
    """Тест сохранения"""
    print("\n🔧 ТЕСТ СОХРАНЕНИЯ")
    print("-"*50)
    
    # Создаем тестового пользователя
    test_user = User(
        name="Тест Тестович",
        age="30",
        city="Тестоград",
        phone="9991234567",
        email="test@test.com",
        login="testuser",
        password="test123"
    )
    
    # Загружаем существующих пользователей
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            users = json.load(f)
    else:
        users = []
    
    # Добавляем нового
    users.append(test_user.to_dict())
    
    print(f"📝 Сохраняю {len(users)} пользователей...")
    
    # Сохраняем в файл
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
        print("✅ Файл успешно записан!")
        
        # Проверяем размер файла
        size = os.path.getsize(DATA_FILE)
        print(f"📦 Размер файла: {size} байт")
        
        # Проверяем содержимое
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
            print(f"✅ В файле {len(saved_data)} пользователей")
            
            # Проверяем, есть ли наш пользователь
            found = False
            for user in saved_data:
                if user['логин'] == 'testuser':
                    found = True
                    print(f"✅ Найден пользователь: {user['логин']}")
                    break
            
            if not found:
                print("❌ Тестовый пользователь не найден!")
                
    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")
        import traceback
        traceback.print_exc()

def test_auth_logic():
    """Тестируем вашу auth_logic"""
    print("\n🔧 ТЕСТ AUTH_LOGIC")
    print("-"*50)
    
    from auth_logic import register_user, load_users
    
    print("1. Регистрируем нового пользователя...")
    success, message = register_user(
        "Диагностика Диагностович",
        "28",
        "Диагностик",
        "88888888888",
        "diag@test.com",
        "diaguser",
        "diag123"
    )
    
    print(f"   Результат: {message}")
    
    print("\n2. Загружаем пользователей...")
    users = load_users()
    print(f"   Загружено {len(users)} пользователей")
    
    print("\n3. Ищем нового пользователя...")
    found = False
    for user in users:
        if user.login == "diaguser":
            found = True
            print(f"   ✅ Найден! Имя: {user.name}")
            break
    
    if not found:
        print("   ❌ Не найден в загруженном списке!")

if __name__ == "__main__":
    print("="*60)
    print("ДИАГНОСТИКА СОХРАНЕНИЯ ПОЛЬЗОВАТЕЛЕЙ")
    print("="*60)
    
    # Показываем текущее состояние файла
    show_file_content()
    
    # Запускаем тест сохранения
    save_test()
    
    # Показываем состояние после теста
    show_file_content()
    
    # Тестируем вашу auth_logic
    test_auth_logic()
    
    # Финальная проверка
    show_file_content()
    
    print("\n✅ Диагностика завершена!")
    input("\nНажмите Enter для выхода...")