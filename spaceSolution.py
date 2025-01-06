import os

os.system('COLOR B')

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()

try:
    inner_function()
except:
    print('Функция "inner_function" нет возможности вызвать за пределами функции test_function')

try:
    os.system('PAUSE')
except:
    os.system('CLS')
