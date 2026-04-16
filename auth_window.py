import tkinter as tk
from tkinter import messagebox
from auth_logic import authenticate
from profile_window import ProfileWindow
from register_window import RegisterWindow

class AuthWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Авторизация")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Заголовок
        title_frame = tk.Frame(self.root, bg="#4CAF50", height=100)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        
        lbl_title = tk.Label(title_frame, text="Добро пожаловать!", 
                            font=("Arial", 20, "bold"), 
                            bg="#4CAF50", fg="white")
        lbl_title.pack(expand=True)
        
        # Основная форма
        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=40, pady=30)
        main_frame.pack(fill="both", expand=True)
        
        # Поле логина
        lbl_login = tk.Label(main_frame, text="Логин", font=("Arial", 11), 
                            bg="#f0f0f0", fg="#333")
        lbl_login.pack(anchor="w", pady=(0, 5))
        
        self.entry_login = tk.Entry(main_frame, width=35, font=("Arial", 11),
                                     relief="solid", bd=1)
        self.entry_login.pack(pady=(0, 15), ipady=8)
        
        # Поле пароля
        lbl_password = tk.Label(main_frame, text="Пароль", font=("Arial", 11),
                               bg="#f0f0f0", fg="#333")
        lbl_password.pack(anchor="w", pady=(0, 5))
        
        self.entry_password = tk.Entry(main_frame, width=35, font=("Arial", 11),
                                        show="*", relief="solid", bd=1)
        self.entry_password.pack(pady=(0, 25), ipady=8)
        
        # Кнопка входа
        btn_login = tk.Button(main_frame, text="Войти", command=self.login,
                              bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                              relief="flat", cursor="hand2", height=2)
        btn_login.pack(fill="x", pady=(0, 15))
        
        # Разделитель
        separator = tk.Frame(main_frame, height=1, bg="#ddd")
        separator.pack(fill="x", pady=15)
        
        # Блок регистрации
        lbl_register = tk.Label(main_frame, text="Нет аккаунта?", 
                                font=("Arial", 10), bg="#f0f0f0", fg="#666")
        lbl_register.pack()
        
        btn_register = tk.Button(main_frame, text="Зарегистрироваться", 
                                 command=self.open_register,
                                 bg="white", fg="#4CAF50", font=("Arial", 10, "bold"),
                                 relief="flat", cursor="hand2", bd=0)
        btn_register.pack(pady=(5, 0))
        
        # Привязка клавиши Enter
        self.entry_login.bind('<Return>', lambda event: self.login())
        self.entry_password.bind('<Return>', lambda event: self.login())
        
        # Фокус на поле логина
        self.entry_login.focus()
        
    def login(self):
        login = self.entry_login.get().strip()
        password = self.entry_password.get().strip()
        
        if not login or not password:
            messagebox.showerror("Ошибка", "Введите логин и пароль!")
            return
        
        user = authenticate(login, password)
        
        if user:
            self.root.destroy()
            ProfileWindow(user)
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")
            self.entry_password.delete(0, tk.END)
            self.entry_password.focus()
    
    def open_register(self):
        self.root.destroy()
        RegisterWindow()
    
    def run(self):
        self.root.mainloop()