"""
    Ez az elem tartalmazza a SettingScreen osztályt
    ami a bellítási felület megjelenítésért és működésért felel.
"""

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from src.expense_tracker.controller.data_controller import DataController
from src.expense_tracker.controller.year_controller import YearController


class SettingScreen(Screen):
    """
       A setting_screen mögötti logikát biztosító osztály.
    """
    dataController = DataController()
    yearController = YearController()

    def on_enter(self, *args):
        self.ids.categories_container.clear_widgets()

        self.ids.limit.text = str(self.dataController.get_limit())

        for category_name in self.dataController.get_categories():
            label = Label(
                text=category_name,
                color=(1, 1, 1, 1),
                font_size='16sp',
                size_hint_x=None,
            )
            label.bind(texture_size=lambda instance, size:
                       setattr(instance, 'width', size[0]))
            self.ids.categories_container.add_widget(label)

            self.ids.categories_container.add_widget(Widget())

            btn = Button(
                text='Törlés',
                color=(1, 1, 1, 1),
                font_size='16sp',
                bold=True,
                background_color=(1, 1, 1, 0),
                size_hint_x=None,
            )
            btn.bind(on_release=lambda instance, name=category_name:
                     self.delete_category(name)
                     )
            btn.bind(texture_size=lambda instance, size:
                     setattr(instance, 'width', size[0])
                     )
            self.ids.categories_container.add_widget(btn)

    def delete_category(self, category):
        """
            Meghívja a controller delete metódusát majd újra tölti az oldalt.
        """
        self.dataController.delete_category(category)

        self.on_enter()

    def focus_change(self, focus):
        """
            Megnézi a havi kaidás limétjét állító input mező értékét amikor
            azt elhagyja a felhasználó
        """
        if not focus:
            if self.ids.limit.text == "" or int(self.ids.limit.text) <= 0:
                print("HIBA: Helytelen érték!")
            else:
                self.dataController.save_limit(self.ids.limit.text)

    def delete_all(self):
        """
            Kitöröl minden adatot a data.json-ből és a yearData.json-ből
        """
        self.dataController.delete_all()
        self.yearController.delete_months()
        self.on_enter()
