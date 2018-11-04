
# Структура файлов
import sys

for path in sys.path:
    print(path)

# ПРОЧИТАТЬ про:
# pip - это утилита, которая позволяет устанавлимать модули, requirements.txt - создается файл в корне и прописываются
# модули, которые вы используете и которые доступны в интернете, то есть в питоновском репозитории
# Зависимость узнать: $pip freeze | записать: $pip freeze > requirement.txt | посмотреть $cat requirement.txt +
# установить все зависимости из requirement.txt: pip install -r requirement.txt

# ПРОЧИТАТЬ про:
#docs.python.org/3/libraty/os.html
import os

#os.listdir()  # просмотр сожержимого каталога
#os.mkdir()    # создание папки
#os.chdir()    # сменить имя каталога

# sys для работы интрапритатором
import sys

print(sys.argv)

if "help" in sys.argv:
    print("Вы запросили помощь")

# для указания перемметров которые собираемся передовать можно использовать консоль или - run >> edit configurations >>>
# >> parameters  В методичке есть пример


# Классы, конструкторы и методы
class Phone:

    # Конструктор класса - создается когда нужно переопределить, добавить свойство или отрибут объекту,
    # то есть добавить переменную
    # Этот метод пишут, только когда нужно поменять логипу объекта класса
    # __init__ - метод встроенный системный поэтому два поддчеркивания
    # self.model - это конструкция испозуется когда нужно создать атрибут и одать ему значение phone_model
    def __init__(self, phone_model):
        self._model = phone_model
        self._loading()
        self._serial_number = 87982346923479827489382

    # Пример Инкапсуляции на примере внутренного вызова приватного метода
    def _loading(self):  # ВАЖНО!!! одно _перед методом, делает метод приватным и его не видно болше за приделами класс
        print(self._model,'is loading')

    def get_serial_number(self):
        return self._serial_number

    def get_model(self):
        return self._model

    # self - ссылка на объект, который будет создан
    def call(self):
        print(phone._model, "is calling")


phone = Phone("nokia 3310")
phone.call()
phone._loading()     # но вызвать всеже можно
print(phone.get_serial_number())


# Пример наследования. Класс родитель (super) указывается в скобках
class SmartPhone(Phone):

    def call(self):
        print('is calling!!!')

    def sms(self):
        print("is sending sms")

    def email(self):
        print('is sending emil')

    def app(self):
        print('is starting app')

smart_phone = SmartPhone("Nokia 9999")
smart_phone.sms()
smart_phone.app()
smart_phone.call()
print(smart_phone.get_serial_number())


#
class IPhone(SmartPhone):

    # Переопределение конструктора
    def __init__(self, phone_model):

        # supper тут папа, а не дед)
        super().__init__(phone_model) # эти две записи индентичны SmartPhone(self).__init__(phone_model)и

    # Переопределение метода (см значек слева)
    def app(self):
        print("is starting app from apple shop")

    def player(self):
        print('playing music...')

    def brower(self):
        print('browser oppening...')

iphone = IPhone("s6")
iphone.call()
iphone.email()
iphone.app()

class NexGenerationSmartPhone(IPhone):

    def face_id(self):
        print('Face id is working...')

    def print_id(self):
        print("Print ID is working...")

    def pay(self):
        print('PAY!!!')

# Полиморфизм
# для будующего развития класс можно ставить pass
class Samsung(NexGenerationSmartPhone):

    def call(self):
        print("Samsung new type of call +++")

class Nokia(NexGenerationSmartPhone):

    def call(self):
        print("Samsung new type of call +++")

samsung = Samsung("S+6")
nokia = Nokia("sX")

def mobile_call(phone):
    phone.call(phone)

mobile_call(Samsung)
mobile_call(Nokia)