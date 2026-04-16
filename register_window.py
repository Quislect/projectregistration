import tkinter as tk
from tkinter import messagebox
from auth_logic import register_user

class RegisterWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Регистрация")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.setup_ui()
        self.root.mainloop()
        
    def setup_ui(self):
        # Заголовок
        title_frame = tk.Frame(self.root, bg="#2196F3", height=100)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        
        lbl_title = tk.Label(title_frame, text="Создание аккаунта", 
                            font=("Arial", 20, "bold"), 
                            bg="#2196F3", fg="white")
        lbl_title.pack(expand=True)
        
        # Контейнер для прокрутки
        canvas = tk.Canvas(self.root, bg="#f0f0f0", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Основная форма
        main_frame = tk.Frame(scrollable_frame, bg="#f0f0f0", padx=40, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Поля формы
        fields = [
            ("Имя:", "entry_name", 0),
            ("Возраст:", "entry_age", 0),
            ("Город:", "entry_city", 0),
            ("Телефон:", "entry_phone", 0),
            ("Почта:", "entry_email", 0),
            ("Логин:", "entry_login", 0),
            ("Пароль:", "entry_password", 1)
        ]
        
        self.entries = {}
        self.error_labels = {}
        
        for i, (label_text, entry_name, is_password) in enumerate(fields):
            frame = tk.Frame(main_frame, bg="#f0f0f0")
            frame.pack(fill="x", pady=(15 if i > 0 else 0, 5))
            
            lbl = tk.Label(frame, text=label_text, font=("Arial", 11),
                          bg="#f0f0f0", fg="#333")
            lbl.pack(anchor="w")
            
            show_char = "*" if is_password else ""
            entry = tk.Entry(frame, width=35, font=("Arial", 11),
                            show=show_char, relief="solid", bd=1)
            entry.pack(fill="x", pady=(5, 0), ipady=8)
            
            # Лейбл для ошибок
            error_lbl = tk.Label(frame, text="", font=("Arial", 9),
                                 bg="#f0f0f0", fg="#f44336")
            error_lbl.pack(anchor="w", pady=(2, 0))
            
            self.entries[entry_name] = entry
            self.error_labels[entry_name] = error_lbl
        
        # Кнопки
        btn_frame = tk.Frame(main_frame, bg="#f0f0f0")
        btn_frame.pack(fill="x", pady=(30, 15))
        
        btn_register = tk.Button(btn_frame, text="Зарегистрироваться", 
                                 command=self.register,
                                 bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                                 relief="flat", cursor="hand2", height=2)
        btn_register.pack(fill="x", pady=(0, 10))
        
        btn_back = tk.Button(btn_frame, text="← Назад к авторизации", 
                             command=self.back_to_auth,
                             bg="white", fg="#666", font=("Arial", 10),
                             relief="flat", cursor="hand2", bd=0)
        btn_back.pack()
        
        # Привязка событий для валидации
        self.entries["entry_age"].bind('<KeyRelease>', lambda e: self.validate_age())
        self.entries["entry_phone"].bind('<KeyRelease>', lambda e: self.validate_phone())
        self.entries["entry_email"].bind('<KeyRelease>', lambda e: self.validate_email())
        
    def validate_age(self):
        """Валидация возраста"""
        age = self.entries["entry_age"].get().strip()
        if age and (not age.isdigit() or int(age) < 0 or int(age) > 120):
            self.error_labels["entry_age"].config(text="Возраст должен быть числом от 0 до 120")
            return False
        else:
            self.error_labels["entry_age"].config(text="")
            return True
    
    def validate_phone(self):
        """Валидация телефона"""
        import re
        phone = self.entries["entry_phone"].get().strip()
        phone_clean = re.sub(r'[^0-9]', '', phone)
        if phone and len(phone_clean) < 10:
            self.error_labels["entry_phone"].config(text="Телефон должен содержать минимум 10 цифр")
            return False
        else:
            self.error_labels["entry_phone"].config(text="")
            return True
    
    def validate_email(self):
        """Валидация email"""
        email = self.entries["entry_email"].get().strip()
        if email and ('@' not in email or '.' not in email):
            self.error_labels["entry_email"].config(text="Введите корректный email")
            return False
        else:
            self.error_labels["entry_email"].config(text="")
            return True
    
    def register(self):
        name = self.entries["entry_name"].get().strip()
        age = self.entries["entry_age"].get().strip()
        city = self.entries["entry_city"].get().strip()
        phone = self.entries["entry_phone"].get().strip()
        email = self.entries["entry_email"].get().strip()
        login = self.entries["entry_login"].get().strip()
        password = self.entries["entry_password"].get().strip()
        
        # Проверка заполнения
        if not all([name, age, city, phone, email, login, password]):
            messagebox.showerror("Ошибка", "Заполните все поля!")
            return
        
        # Валидация
        if not self.validate_age():
            return
        
        if not self.validate_phone():
            return
        
        if not self.validate_email():
            return
        
        success, message = register_user(name, age, city, phone, email, login, password)
        
        if success:
            messagebox.showinfo("Успех", message)
            self.back_to_auth()
        else:
            messagebox.showerror("Ошибка", message)
    
    def back_to_auth(self):
        from auth_window import AuthWindow
        self.root.destroy()
        AuthWindow().run()