"""
Сделать окно авторизации\регистрации, используя TKinter
"""
from tkinter import *


class Register:

    def __init__(self, users):
        main = Tk()
        self.users = users
        self.main = main
        main.geometry('400x400+100+100')
        main.resizable(width=False, height=False)
        main.title('регистрация')
        self.lab = Label(text='регистрация')
        self.lab_name = Label(text='Имя пользователя')
        self.ent_login = Entry()
        self.lab_password = Label(text='Пароль')
        self.ent_password = Entry(show='*')
        self.lab_repeat_password = Label(text='Повторите пароль')
        self.ent_repeat_password = Entry(show='*')
        self.btn_input = Button(text='Ввод')
        self.lab_erorr = Label(text="")
        self.btn_register = Button(text='авторизация')

        self.lab.pack(pady=15)
        self.lab_name.pack()
        self.ent_login.pack(pady=(0, 15))
        self.lab_password.pack()
        self.ent_password.pack(pady=(0, 15))
        self.lab_repeat_password.pack()
        self.ent_repeat_password.pack()
        self.btn_input.pack(pady=10)
        self.lab_erorr.pack()
        self.btn_register.pack(side=BOTTOM, pady=20)

        self.btn_input.bind("<Button-1>", self.input_click)
        self.btn_register.bind('<Button-1>', self.register_click)

        main.mainloop()

    def input_click(self, event):
        name = self.ent_login.get()
        password = self.ent_password.get()
        repeat_password = self.ent_repeat_password.get()

        if name == '':
            self.lab_erorr.configure(text="заполните поле 'Имя пользователя'.")
        elif password == '':
            self.lab_erorr.configure(text="заполните поле 'Пароль'.")
        elif repeat_password == '':
            self.lab_erorr.configure(text="заполните поле 'Повторите пароль'.")
        else:
            if name in self.users:
                self.lab_erorr.configure(text="Имя уже используется!")
            elif password != repeat_password:
                self.lab_erorr.configure(text="Пароли не совпадают!")
            else:
                self.users[name] = password
                self.lab_erorr.configure(text="Регистрация прошла успешно.\nАвторизуйтесь по кнопке ниже и начинайте играть")

    def register_click(self, event):
        self.main.destroy()
        login = Login(self.users)


class Login:

    def __init__(self, users):
        main = Tk()
        self.users = users
        self.main = main
        main.geometry('400x400+100+100')
        main.resizable(width=False, height=False)
        main.title('авторизация')
        self.lab = Label(text='авторизация')
        self.lab_name = Label(text='Имя пользователя')
        self.ent_login = Entry()
        self.lab_password = Label(text='Пароль')
        self.ent_password = Entry(show='*')
        self.btn_input = Button(text='Ввод')
        self.lab_erorr = Label(text="")
        self.btn_register = Button(text='регистрация')

        self.lab.pack(pady=15)
        self.lab_name.pack()
        self.ent_login.pack(pady=(0, 15))
        self.lab_password.pack()
        self.ent_password.pack(pady=(0, 15))
        self.btn_input.pack(pady=10)
        self.lab_erorr.pack()
        self.btn_register.pack(side=BOTTOM, pady=20)

        self.btn_input.bind("<Button-1>", self.input_click)
        self.btn_register.bind('<Button-1>', self.register_click)
        main.mainloop()

    def input_click(self, event):
        name = self.ent_login.get()
        password = self.ent_password.get()

        if name == '':
            self.lab_erorr.configure(text="заполните поле 'Имя пользователя'.")
        elif password == '':
            self.lab_erorr.configure(text="заполните поле 'Пароль'.")
        else:
            if name in self.users:
                if self.users[name] != password:
                    self.lab_erorr.configure(
                        text="Неверное имя пользователя или пароль, "
                             "\nповторите попытку или зарегистрируйтесь, \nнажав на кнопку ниже.")
                else:
                    self.main.destroy()
                    game = Game()
            else:
                self.lab_erorr.configure(
                    text="Неверное имя пользователя или пароль, "
                         "\nповторите попытку или зарегистрируйтесь, \nнажав на кнопку ниже.")

    def register_click(self, event):
        self.main.destroy()
        register = Register(self.users)


class Game:

    def __init__(self):
        main = Tk()
        self.main = main
        main.geometry('600x600+100+100')
        main.resizable(width=False, height=False)
        main.title('Крестики-нолики')


users_list = {}
login = Login(users_list)

