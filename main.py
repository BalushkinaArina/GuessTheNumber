import tkinter as tk # импортируем библиотеку tkinter
from Сonstants import *
from MainMenu import * # импортируем файл MainMenu

if __name__ == "__main__":
    app = MainMenu() # вызываем класс MainMenu, который создает окно приложения
    app.mainloop() # открываем окно приложения и не даем ему закрыться