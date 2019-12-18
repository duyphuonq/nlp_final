import sys
import time
import kivy
import json
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.clock import Clock

with open("data.json", "r") as file:
    data = json.load(file)

class Intro(GridLayout):
    def __init__(self, **kwarg):
        super().__init__(**kwarg)
        self.rows = 2
        self.cols = 3
        #Label
        self.label = \
        """Bạn là ai ?"""
        self.label_widget = Label(text=self.label, font_size=20)
        #Phuong
        self.phuong = Button(text="Phương", font_size=30)
        self.phuong.bind(on_press=self.phuong_press)
        #Minh Tron
        self.minh_tron = Button(text="Minh Tròn", font_size=30)
        self.minh_tron.bind(on_press=self.minh_tron_press)
        #Thanh Minh
        self.thanh_minh = Button(text="Thánh Minh", font_size=30)
        self.thanh_minh.bind(on_press=self.thanh_minh_press)
        #Long
        self.long = Button(text="Long", font_size=30)
        self.long.bind(on_press=self.long_press)
        #Hieu
        self.hieu = Button(text="Hiếu", font_size=30)
        self.hieu.bind(on_press=self.hieu_press)
        #Add widgets
        self.add_widget(self.label_widget)
        self.add_widget(self.phuong)
        self.add_widget(self.minh_tron)
        self.add_widget(self.thanh_minh)
        self.add_widget(self.long)
        self.add_widget(self.hieu)

    #Phuong press
    def phuong_press(self, ins):
        add_data.screen_manager.current = "Add_Phuong"
    #Hieu Press
    def hieu_press(self, ins):
        add_data.screen_manager.current = "Add_Hieu"
    #Long press
    def long_press(self, ins):
        add_data.screen_manager.current = "Add_Long"
    #Minh Tron press
    def minh_tron_press(self, ins):
        add_data.screen_manager.current = "Add_Minh_Tron"
    #Thanh minh press
    def thanh_minh_press(self, ins):
        add_data.screen_manager.current = "Add_Thanh_Minh"

class Add(GridLayout):
    def __init__(self, **kwarg):
        super().__init__(**kwarg)
        #request keyboard
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)
        #
        self.rows = 3
        self.it = 0
        self.obs = Label(text="Sample!")
        self.title = Label(text="Name")
        self.start = 0
        self.end = 0
        #self.add_widget(self.obs)
        #
        self.bot = GridLayout(rows=2)
        self.select = GridLayout(cols=5)
        self.one = Button(text="1")
        self.two = Button(text="2")
        self.three = Button(text="3")
        self.four = Button(text="4")
        self.five = Button(text="5")
        #
        self.select.add_widget(self.one)
        self.select.add_widget(self.two)
        self.select.add_widget(self.three)
        self.select.add_widget(self.four)
        self.select.add_widget(self.five)
        #
        self.exit = Button(text="Exit")
        self.exit.bind(on_press=self.exit_p)
        #
        self.add_widget(self.title)
        self.add_widget(self.obs)
        self.bot.add_widget(self.select)
        self.bot.add_widget(self.exit)
        self.add_widget(self.bot)

    def name(self, name):
        if name == "Phuong":
            self.title.text = f"Hi Phuong, day la cau {self.it}/5229"
            self.start = 0
            self.end = 5229
        elif name == "Long":
            self.title.text = f"Hi Long, day la cau {self.it}/10458"
            self.start = 5229
            self.end = 10458
        elif name == "Hieu":
            self.title.text = f"Hi Hieu, day la cau {self.it}/15687"
            self.start = 10458
            self.end = 15687
        elif name == "Minh1":
            self.title.text = f"Hi Minh Tron, day la cau {self.it}/20916"
            self.start = 15687
            self.end = 20916
        elif name == "Minh2":
            self.title.text = f"Hi Thanh Minh, day la cau {self.it}/26413"
            self.start = 20916
            self.end = 26143
    def update_osb(self, text):
        self.obs.text = text

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard = None
    
    def update_it(self):
        self.it += 1
        self.clear_widgets()

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if add_data.screen_manager.current != "Intro":
            if keycode[1] == '1':
                self.update_it()
            elif keycode[1] == '2':
                self.it += 1
            elif keycode[1] == '3':
                self.it += 1
            elif keycode[1] == '4':
                self.it += 1
            elif keycode[1] == '5':
                self.it += 1

            return True

    def exit_p(self, ins):
        sys.exit(0)

        

class Add_DataApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.intro = Intro()
        self.screen = Screen(name="Intro")
        self.screen.add_widget(self.intro)
        self.screen_manager.add_widget(self.screen)
        #
        self.add = Add()
        self.add.name("Phuong")
        self.screen = Screen(name="Add_Phuong")
        self.screen.add_widget(self.add)
        self.screen_manager.add_widget(self.screen)
        #
        self.add = Add()
        self.add.name("Long")
        self.screen = Screen(name="Add_Long")
        self.screen.add_widget(self.add)
        self.screen_manager.add_widget(self.screen)
        #
        self.add = Add()
        self.add.name("Hieu")
        self.screen = Screen(name="Add_Hieu")
        self.screen.add_widget(self.add)
        self.screen_manager.add_widget(self.screen)
        #
        self.add = Add()
        self.add.name("Minh1")
        self.screen = Screen(name="Add_Minh_Tron")
        self.screen.add_widget(self.add)
        self.screen_manager.add_widget(self.screen)
        #
        self.add = Add()
        self.add.name("Minh2")
        self.screen = Screen(name="Add_Thanh_Minh")
        self.screen.add_widget(self.add)
        self.screen_manager.add_widget(self.screen)

        return self.screen_manager

if __name__ == "__main__":
    add_data = Add_DataApp()
    add_data.run()