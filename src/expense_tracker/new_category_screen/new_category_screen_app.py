"""
    Ez az elem tartalmazza a NewCategoryScreen osztályt
    ami az új kiadás kategóra hozzáadó
    felület megjelenítésért  és müködésért felel.
"""

from kivy.uix.screenmanager import Screen

from src.expense_tracker.controller.data_controller import DataController


class NewCategoryScreen(Screen):
    """
       A new_category_screen mögötti logikát biztosító osztály.
   """
    dataController = DataController()

    def on_enter(self, *args):
        self.ids.category_name.text = ""

    def save(self, new_category):
        """
            Meghívja a controller add_category metódusát
            ,hogy elmentse az új kiadás kategórát,
            majd vissza viszi a felhasználót a főoldalra
        """
        self.dataController.add_category(new_category)
        self.parent.current = "main_screen"

    def back_to_main(self):
        """
           Vissza viszi a felhasználót a főoldalra
        """
        self.parent.current = "main_screen"
