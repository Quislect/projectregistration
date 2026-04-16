import re
class User:
    def __init__(self, name, age, city, phone, email, login, password):
        self.name = name
        self.age = age
        self.city = city
        self.phone = phone
        self.email = email
        self.login = login
        self.password = password

    def to_dict(self):
        return {
            "имя": self.name,
            "возраст": self.age,
            "город": self.city,
            "телефон": self.phone,
            "почта": self.email,
            "логин": self.login,
            "пароль": self.password
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data.get("имя", ""),
            age=data.get("возраст", ""),
            city=data.get("город", ""),
            phone=data.get("телефон", ""),
            email=data.get("почта", ""),
            login=data.get("логин", ""),
            password=data.get("пароль", "")
        )
    
    def validate(self):
        """Валидация данных пользователя"""
        errors = []
        
        if not self.name or len(self.name) < 2:
            errors.append("Имя должно содержать минимум 2 символа")
        
        if not self.age or not self.age.isdigit() or int(self.age) < 0 or int(self.age) > 120:
            errors.append("Возраст должен быть числом от 0 до 120")
        
        if not self.city or len(self.city) < 2:
            errors.append("Город должен содержать минимум 2 символа")
        
        phone_clean = re.sub(r'[^0-9]', '', self.phone)
        if not phone_clean or len(phone_clean) < 10:
            errors.append("Телефон должен содержать минимум 10 цифр")
        
        if not self.email or '@' not in self.email or '.' not in self.email:
            errors.append("Введите корректный email")
        
        if not self.login or len(self.login) < 3:
            errors.append("Логин должен содержать минимум 3 символа")
        
        if not self.password or len(self.password) < 3:
            errors.append("Пароль должен содержать минимум 3 символа")
        
        return errors