import math
from kivymd.app import MDApp
from kivy.lang import Builder

class MyApp(MDApp):
    def build(self):
        self.screen = Builder.load_file('ui.kv')
        return self.screen
    def check(self):
        try:
            r = float(self.screen.ids.inputOkr.text)
            a = float(self.screen.ids.adina.text)
            b = float(self.screen.ids.dvaaa.text)
            c = float(self.screen.ids.triii.text)
        except ValueError:
            self.screen.ids.resultt.text = "Пожалуйста введите правильные числа"
            return
        p = (a+b+c)/2
        result = math.sqrt((p-a)*(p-b)*(p-c)/p)
        if r <= result:
            self.screen.ids.resultt.text = "Введенная окружность может быть вписанна в введенный треугольник"
        else:
            self.screen.ids.resultt.text = "Введенная окружность НЕ может быть вписанна в введенный треугольник"

MyApp().run()


