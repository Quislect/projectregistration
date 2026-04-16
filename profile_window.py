import tkinter as tk
from tkinter import messagebox
from auth_logic import load_users, save_users

class ProfileWindow:
    def __init__(self, user):
        self.user = user
        self.root = tk.Tk()
        self.root.title(f"Профиль пользователя - {user.name}")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Заголовок с аватаром
        header_frame = tk.Frame(self.root, bg="#4CAF50", height=150)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        avatar = tk.Label(header_frame, text="👤", font=("Arial", 60),
                          bg="#4CAF50", fg="white")
        avatar.pack(pady=20)
        
        lbl_name_header = tk.Label(header_frame, text=self.user.name,
                                   font=("Arial", 18, "bold"),
                                   bg="#4CAF50", fg="white")
        lbl_name_header.pack()
        
        # Основная информация
        main_frame = tk.Frame(self.root, bg="white", padx=40, pady=30)
        main_frame.pack(fill="both", expand=True)
        
        lbl_info = tk.Label(main_frame, text="Личная информация", 
                           font=("Arial", 14, "bold"),
                           bg="white", fg="#333")
        lbl_info.pack(anchor="w", pady=(0, 20))
        
        # Данные пользователя
        user_data = [
            ("📛 Имя:", self.user.name),
            ("🎂 Возраст:", self.user.age),
            ("📍 Город:", self.user.city),
            ("📞 Телефон:", self.user.phone),
            ("✉️ Почта:", self.user.email),
            ("🔑 Логин:", self.user.login)
        ]
        
        for i, (label_text, value) in enumerate(user_data):
            frame = tk.Frame(main_frame, bg="white")
            frame.pack(fill="x", pady=8)
            
            lbl_name = tk.Label(frame, text=label_text, font=("Arial", 11, "bold"),
                               bg="white", fg="#666", width=12, anchor="w")
            lbl_name.pack(side="left")
            
            lbl_value = tk.Label(frame, text=value, font=("Arial", 11),
                                 bg="white", fg="#333", anchor="w")
            lbl_value.pack(side="left", padx=(10, 0))
        
        # Разделитель
        separator = tk.Frame(main_frame, height=1, bg="#ddd")
        separator.pack(fill="x", pady=20)
        
        # Кнопки
        btn_frame = tk.Frame(main_frame, bg="white")
        btn_frame.pack(fill="x", pady=(10, 0))
        
        btn_logout = tk.Button(btn_frame, text="Выйти из аккаунта", 
                               command=self.logout,
                               bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                               relief="flat", cursor="hand2", height=2)
        btn_logout.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        btn_exit = tk.Button(btn_frame, text="Закрыть", 
                             command=self.exit_app,
                             bg="#9E9E9E", fg="white", font=("Arial", 10),
                             relief="flat", cursor="hand2", height=2)
        btn_exit.pack(side="right", expand=True, fill="x", padx=(5, 0))
    
    def logout(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()
            from auth_window import AuthWindow
            AuthWindow().run()
    
    def exit_app(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите закрыть приложение?"):
            self.root.quit()
            self.root.destroy()
    
    def run(self):
        self.root.mainloop()