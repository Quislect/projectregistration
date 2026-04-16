import json
import os
from models import User

# Получаем абсолютный путь к файлу
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(CURRENT_DIR, "users.json")

print(f"📁 Файл users.json находится по адресу: {DATA_FILE}")

def load_users():
    """Загрузка пользователей из файла"""
    if not os.path.exists(DATA_FILE):
        print("📝 Файл не найден, создаю пример...")
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            users = []
            for item in data:
                users.append(User.from_dict(item))
            print(f"✅ Загружено {len(users)} пользователей из файла")
            # Выводим ID загруженных пользователей
            for user in users:
                print(f"   - {user.login} (ID: {user.id})")
            return users
    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        return []

def save_users(users):
    """Сохранение пользователей в файл"""
    try:
        print(f"💾 Сохраняю {len(users)} пользователей в файл...")
        
        data = [user.to_dict() for user in users]
        
        # Показываем, что именно сохраняем (с ID)
        print(f"   Пользователи для сохранения: {[(u.login, u.id) for u in users]}")
        
        # Записываем в файл
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        # Сразу проверяем, что записалось
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            print(f"✅ Файл сохранен! В файле {len(saved_data)} пользователей")
            
            # Показываем, что именно в файле (с ID)
            for user in saved_data:
                print(f"   - {user.get('логин')} ({user.get('имя')}) - ID: {user.get('id')}")
        
        return True

            
    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")
        import traceback
        traceback.print_exc()
        return False

def get_next_id(users):
    """Получить следующий ID для нового пользователя"""
    if not users:
        return 1  # Если пользователей нет, начинаем с 1
    
    # Находим максимальный ID
    max_id = 0
   
    return  users[0].id + 1


    
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(sample_users, file, ensure_ascii=False, indent=4)
        print(f"✅ Создан файл с примерами: {DATA_FILE}")
    except Exception as e:
        print(f"❌ Ошибка создания файла: {e}")

def register_user(name, age, city, phone, email, login, password, photo_base64=None):
    """Регистрация нового пользователя"""
    # Проверка на пустые поля
    if not all([name, age, city, phone, email, login, password]):
        return False, "Заполните все поля!"
    
    # Валидация
    if not age.isdigit() or int(age) < 0 or int(age) > 120:
        return False, "Возраст должен быть числом от 0 до 120"
    
    if '@' not in email or '.' not in email:
        return False, "Введите корректный email"
    
    if len(login) < 3:
        return False, "Логин должен быть минимум 3 символа"
    
    if len(password) < 3:
        return False, "Пароль должен быть минимум 3 символа"
    
    users = load_users()
    
    # Проверка уникальности
    for user in users:
        if user.login == login:
            return False, "Пользователь с таким логином уже существует!"
        if user.email == email:
            return False, "Пользователь с такой почтой уже существует!"
    
    # Получаем следующий ID
    next_id = get_next_id(users)
    
    # Создаем нового пользователя с числовым ID
    new_user = User(name, age, city, phone, email, login, password, 
                    user_id=next_id, photo_base64=photo_base64)
    users.append(new_user)
    
    print(f"\n📝 Регистрирую пользователя: {login}")
    print(f"   ID пользователя: {new_user.id}")
    print(f"   Имя: {name}")
    print(f"   Email: {email}")
    if photo_base64:
        print(f"   📸 Фото загружено")
    
    # Сохраняем
    if save_users(users):
        print(f"✅ Пользователь {login} (ID: {new_user.id}) успешно сохранен!")
        return True, f"Регистрация успешно завершена! Ваш ID: {new_user.id}"
    else:
        print(f"❌ Ошибка сохранения пользователя {login}")
        return False, "Ошибка при сохранении данных"

def authenticate(login, password):
    users = load_users()
    for user in users:
        if user.login == login and user.password == password:
            return user
    return None

def get_user_by_id(user_id):
    """Получить пользователя по ID"""
    users = load_users()
    for user in users:
        if user.id == user_id:
            return user
    return None

def update_user(updated_user):
    """Обновить данные пользователя"""
    users = load_users()
    for i, user in enumerate(users):
        if user.id == updated_user.id:
            users[i] = updated_user
            return save_users(users)
    return False