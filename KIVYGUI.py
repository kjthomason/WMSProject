import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label

class MainScreen(Screen):
    pass

class LV_SELECT (Screen):
    pass

class HV_SELECT (Screen):
    pass

class AnotherScreen (Screen):
    pass

class Forklift_Select (Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("mainkv.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
