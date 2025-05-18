"""
    A fő komponens ez felelős minden más elem helyes meghívásért
"""

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from src.expense_tracker.detail_screen.detail_screen_app import DetailScreen
from src.expense_tracker.main_screen.main_screen_app import MainScreen
from src.expense_tracker.new_category_screen.new_category_screen_app import NewCategoryScreen
from src.expense_tracker.plot_screen.plot_screen_app import PlotScreen
from src.expense_tracker.setting_screen.setting_screen_app import SettingScreen
from src.expense_tracker.upload_screen.upload_screen_app import UploadScreen

kivy.require('1.10.0')


class MyApp(App):
    """
        Ez az osztály felelős minden .kv fájl betöltésért.
    """
    def build(self):
        Builder.load_file("main_screen/mainScreen.kv")
        Builder.load_file("setting_screen/settingScreen.kv")
        Builder.load_file("upload_screen/uploadScreen.kv")
        Builder.load_file("new_category_screen/newCategoryScreen.kv")
        Builder.load_file("detail_screen/DetailScreen.kv")
        Builder.load_file("plot_screen/PlotScreen.kv")

        screen = ScreenManager()
        screen.add_widget(MainScreen(name='main_screen'))
        screen.add_widget(SettingScreen(name='setting_screen'))
        screen.add_widget(UploadScreen(name='upload_screen'))
        screen.add_widget(NewCategoryScreen(name='new_category_screen'))
        screen.add_widget(DetailScreen(name='detail_screen'))
        screen.add_widget(PlotScreen(name='plot_screen'))
        return screen


if __name__ == '__main__':
    MyApp().run()
