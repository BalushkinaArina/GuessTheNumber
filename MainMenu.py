import tkinter as tk # импортируем библиотеку tkinter
from Сonstants import *
from UserVersusComputer import * # импортируем файл UserVersusComputer
from UserVersusUser import * # импортируем файл UserVersusUser

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(windowTitle) # именуем окно
        self.geometry(f'{windowWidth}x{windowHeight}') # задаем размеры окна

        # Создаем заголовок
        self.label_Title = tk.Label(
            self, # надпись создается в этом окне
            text=labelTitleText, # текст для надписи
            font=('Arial',24), # размер текст
            fg=color_titleText) # цвет текста
        self.label_Title.pack(pady=12, anchor='center') # устанавливаем надпись в центре окна с отступом 12px


        # Создаем кнопку пользователь против компьютера
        self.button_ModeUvC = tk.Button(
            self, # кнопка создается в этом окне
            text=nameButtonModeUvC, # текст на кнопке
            font=('Arial',16), # размер текста
            bg=color_bgButton, # цвет кнопки
            fg=color_textButton, # цвет текста кнопки
            command=self.ModeUvC) # функция, которая вызывается кнопкой
        self.addAnimationHover(# функция для вызовани анимации наведения
            self.button_ModeUvC,  # к какой кнопке применяется функция
            color_hover_bgButton, # на какой цвет меняется фон
            color_bgButton, # к какому цвету возвращается фон
            color_hover_textButton, # на какой цвет меняется текст
            color_textButton) # к какому цвету возвращается текс
        self.button_ModeUvC.pack(pady=12, anchor='center') # устанавливаем кнопку в центре окна с отступом 12px

        # Создаем кнопку пользователь против пользователя
        self.button_ModeUvU = tk.Button(
            self,
            text=nameButtonModeUvC, # текст на кнопке
            font=('Arial',16), # размер текст
            bg=color_bgButton, # цвет кнопки
            fg=color_textButton, # цвет текста кнопки
            command=self.ModeUvU) # функция, которая вызывается кнопкой
        self.addAnimationHover(# функция для вызовани анимации наведения
            self.button_ModeUvU,  # к какой кнопке применяется функция
            color_hover_bgButton, # на какой цвет меняется фон
            color_bgButton, # к какому цвету возвращается фон
            color_hover_textButton, # на какой цвет меняется текст
            color_textButton) # к какому цвету возвращается текс
        self.button_ModeUvU.pack(pady=12, anchor='center') # устанавливаем кнопку

        # Создаем кнопку выход из окна
        self.button_exit = tk.Button(
            self,
            text=nameExit, # текст на кнопке
            font=('Arial',16), # размер текст 
            bg=color_bgButton, # цвет кнопки
            fg=color_textButton, # цвет текста кнопки
            command=self.exitingTheProgram) # функция, которая вызывается кнопкой
        self.addAnimationHover( # функция для вызовани анимации наведения
            self.button_exit,  # к какой кнопке применяется функция
            color_hover_bgButton, # на какой цвет меняется фон
            color_bgButton, # к какому цвету возвращается фон
            color_hover_textButton, # на какой цвет меняется текст
            color_textButton) # к какому цвету возвращается текс
        self.button_exit.pack(pady=12, anchor='center') # устанавливаем кнопку

    def ModeUvC(self):
        self.withdraw()
        game_window = UserVersusComputer(self)
        game_window.mainloop()

    def ModeUvU(self):
        self.withdraw()
        game_window = UserVersusUser(self)
        game_window.mainloop()
    
    def exitingTheProgram(self):
        self.destroy()  # корректное закрытие окна

    # функция для создания анимации при наведении на кнопки
    def addAnimationHover(self, button, hover_color_bg, normal_color_bg, hover_color_tx, normal_color_tx):
        def on_enter(event):
            button.config(bg=hover_color_bg,fg=hover_color_tx)

        def on_leave(event):
            button.config(bg=normal_color_bg,fg=normal_color_tx)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)