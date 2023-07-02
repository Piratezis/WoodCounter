from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
import json
from kivy.app import App
# from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
w = screensize[0]
h = screensize[1]
settings2 = json.dumps([
    {'type': 'title',
     'title': 'Настройки'},
    {'type': 'bool',
     'title': 'ВКЛ. тёмную тему',
     'desc': 'Светлая/Тёмная',
     'section': 'example',
     'key': 'boolexample'},
    {'type': 'path',
     'title': 'Загрузить таблицу клиента',
     'desc': 'Выберите таблицу Эксель',
     'section': 'example',
     'key': 'pathexample'},
    {'type': 'title',
     'title': 'Каталог клиентов'},
    {'type': 'options',
     'title': 'Выберите клиента:',
     'section': 'example',
     'key': 'optionsexample',
     'options': ['Вася', 'Лёха', 'Костя']}])
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'resizable', '1')  # разрешить изменять размер
Config.set('graphics', 'widht', w)  # ширина
Config.set('graphics', 'height', h)  # высота окна
layout = dict(zip(map(ord, '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''),
                  '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''))
with open("typeswood.txt", 'r') as fil09:
    te = fil09.readline().split()
typwood = []
for i in te:
    typwood.append(i.translate(layout))

countwood = len(typwood)
tolic = round(1 / countwood + 1, 2)


class WoodApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        al = BoxLayout(orientation='vertical', size_hint=(1, 1))

        box1 = GridLayout(cols=2, rows=1, size_hint=(1, .05))

        f2 = BoxLayout(orientation='vertical', padding=[0], size_hint=(1, .95))
        f2.add_widget(TextInput(background_color=[.58, .63, .62, 1],
                                background_normal='', size_hint=(tolic, 1)))

        f3 = BoxLayout(orientation='horizontal', size_hint=(1, .05))

        f3.add_widget(TextInput(background_color=[.69, .74, .88, 1],
                                background_normal='', size_hint=(0.35, 1)))
        f3.add_widget(Button(text='+', font_size=17, on_press=self.btn_press, background_color=[.15, 1, 0, 1],
                             background_normal='', size_hint=(0.1, 1)))
        f3.add_widget(Button(text='НОВАЯ', font_size=17, on_press=self.btn_press, background_color=[.17, .63, .5, 1],
                             background_normal='', size_hint=(0.3, 1)))
        f1 = GridLayout(cols=countwood, rows=2, padding=[0], size_hint=(1, .05), spacing=1)

        for i2 in range(countwood):
            textw1 = typwood[i2]
            f1.add_widget(
                Button(text=textw1, font_size=14, on_press=self.btn_press, background_color=[.58, .63, .62, 1],
                       background_normal='', size_hint=(tolic, 1)))
        f0 = GridLayout(cols=1, rows=1, size_hint=(0.1, .02), spacing=1)

        f0.add_widget(Button(text='Меню', font_size=14, on_release=self.open_settings,
                             size_hint=(1, 1),
                             pos_hint={"x": 1, "y": 0.2}))
        box1.add_widget(f0)
        box1.add_widget(f1)
        al.add_widget(box1)
        al.add_widget(f3)
        al.add_widget(f2)
        return al

    def btn_press(self, instance):
        pass

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'Вася',
            'pathexample': '/some/path'})

    def build_settings(self, settings):
        settings.add_json_panel('', self.config,
                                data=settings2)


if __name__ == '__main__':
    WoodApp().run()
