# Калькулятор 1.0

---

## Описание приложения

<p align="center">
  <img src="images\Интерфейс.jpg">
</p>

Калькулятор позволяет выполнять операции над числами или алгебраическими формулами. 

Интерфейс поддерживает русский и английский языки.

Имеется два режима работы:

1. Простой режим. Поддерживает базовые арифметические операции, смена знака, проценты, возведение в квадрат и квадратный корень.
2. Расширенный режим. Поддерживает функции простого режима калькулятора, тригонометрические функции, возведение в произвольную степень, логарифмы (натуральный и десятичный), модуль числа, факториал числа, перевод в системы счисления.

|    Простой    |  Расширенный  |
| ------------- | ------------- |
| <img src="images\Интерфейс_простой.jpg">  | <img src="images\Интерфейс_расширенный.jpg">  |

Пользователь может изменить семейство шрифтов и тему оформления интерфейса, три на выбор: 

* темная (продемонстрирована выше); 
* светлая; 
* детская.

|     GREY      |     CLOWN     |
| ------------- | ------------- |
| <img src="images\Интерфейс_светлая.jpg">  | <img src="images\Интерфейс_детская.jpg">  |

## Используемые технологии

Калькулятор реализован с помощью языка программирования Python. Использовалась встроенная библиотека Tkinter, библиотека для создания графических приложений.

![Библиотека Tkinter](https://i.ibb.co/wpgtPhc/logoPy.png 'Tkinter')

## Инструкции по сборке проекта для нескольких операционных систем

Для Windows: 

С помощью _Auto PY to EXE_ Python-проект был преобразован в исполняемый файл .exe. Благодаря этому наше приложение работает как десктопное и может запускаться на других машинах без необходимости установки Python. Достаточно просто запустить файл main.exe и приложение запустится на вашем компьютере.

Для Linux: 

1. Установить зависимости - sudo apt-get install python3-tk
2. Запустить приложение - python3 main.py

Для MacOS:



## Перечень используемых ресурсов: изображения, звуки и т.п.

Все иконки кнопок создавались командой самостоятельно с помощью платформы Figma.