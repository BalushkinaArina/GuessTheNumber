import tkinter as tk # импортируем библиотеку tkinter
import random # импортируем библиотеку random
from Сonstants import *
from MainMenu import * # импортируем файл MainMenu

class UserVersusComputer(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent) # передаем окно главного меню как родителя
        self.parent = parent
        self.title(windowTitle) # именуем окно
        self.geometry(f'{windowWidth}x{windowHeight}') # задаем размеры окна
        self.resizable(False, False)

        # Загадываем число
        self.secret_number = random.randint(1,100)

        # Создаем заголовок
        self.label_Title = tk.Label(
            self, # надпись создается в этом окне
            text=labelTitleText_UvC, # текст для надписи
            font=('Arial',18), # размер текст
            fg=color_titleText) # цвет текста
        self.label_Title.pack(pady=12, anchor='center') # устанавливаем надпись в центре окна с отступом 12px

        # Создаем окно для внесения цифр
        self.answerU = tk.Text(self, width=6, height=1, font=('Arial',18), fg=color_titleText)
        self.answerU.pack(pady=12, anchor='center')
        
        # Создаем кнопку для проверки ответа
        self.check_answer = tk.Button(
            self,
            text=text_checkAnswerU, # текст на кнопке
            font=('Arial',16), # размер текст 
            bg=color_bgButton, # цвет кнопки
            fg=color_textButton, # цвет текста кнопки
            command=self.checkAnswerU) # функция, которая вызывается кнопкой
        self.addAnimationHover( # функция для вызовани анимации наведения
            self.check_answer,  # к какой кнопке применяется функция
            color_hover_bgButton, # на какой цвет меняется фон
            color_bgButton, # к какому цвету возвращается фон
            color_hover_textButton, # на какой цвет меняется текст
            color_textButton) # к какому цвету возвращается текс
        self.check_answer.pack(pady=12, anchor='center') # устанавливаем кнопку

        # Правила
        self.label_Title = tk.Label(
            self, # надпись создается в этом окне
            text=textRules_UvC, # текст для надписи
            font=('Arial',12), # размер текст
            fg=color_titleText) # цвет текста
        self.label_Title.pack(pady=12, anchor='center') # устанавливаем надпись в центре окна с отступом 12px

        # Создаем кнопку возвращение в главное меню
        self.go_to_menu = tk.Button(
            self,
            text=text_go_to_menu, # текст на кнопке
            font=('Arial',16), # размер текст 
            bg=color_bgButton, # цвет кнопки
            fg=color_textButton, # цвет текста кнопки
            command=self.go_to_MainMenu) # функция, которая вызывается кнопкой
        self.addAnimationHover( # функция для вызовани анимации наведения
            self.go_to_menu,  # к какой кнопке применяется функция
            color_hover_bgButton, # на какой цвет меняется фон
            color_bgButton, # к какому цвету возвращается фон
            color_hover_textButton, # на какой цвет меняется текст
            color_textButton) # к какому цвету возвращается текс
        self.go_to_menu.pack(pady=12, anchor='center') # устанавливаем кнопку

        # Создаем текст для сообщений
        self.message_label = tk.Label(
                self,
                font=('Arial', 12),
                fg="red"
            )
        self.message_label.pack(pady=12, anchor='center')
    
    # обработка ответа пользователя
    def checkAnswerU(self):
        # Получаем текст из Text-виджета и убираем лишний символ перевода строки
        user_answer = self.answerU.get("1.0", tk.END).strip()

        # Проверяем, что поле не пустое:
        if not user_answer:
            self.show_message('Ошибка. Надо ввести число')
            return
        
        # Проверяем, введено ли число и преобразовываем в целое число
        try:
            user_answer = int(user_answer)
        except ValueError:
            self.show_message("Ошибка. Введите корректное целое число!")
            return
        
        if self.secret_number == user_answer:
            self.show_message('Поздравляю! Вы отгадали!')
        elif self.secret_number > user_answer:
            self.show_message('Неправильно! Загаданное число БОЛЬШЕ!')
        else:
            self.show_message('Неправильно! Загаданное число МЕНЬШЕ!')
    
    # функция выхова главного меню
    def go_to_MainMenu(self):
        self.destroy()
        self.parent.deiconify() 
    
    # функция вызова сообщений
    def show_message(self, m_text):
        # Обновляем текст метки
        self.message_label.config(text=m_text)

    def addAnimationHover(self, button, hover_color_bg, normal_color_bg, hover_color_tx, normal_color_tx):
        def on_enter(event):
            button.config(bg=hover_color_bg,fg=hover_color_tx)

        def on_leave(event):
            button.config(bg=normal_color_bg,fg=normal_color_tx)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
