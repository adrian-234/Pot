"""
    Ez az elem tartalmazza a UploadScreen osztályt
    ami egy új kiadás feltöltésért felel.
"""

import datetime
from kivy.uix.screenmanager import Screen

from src.expense_tracker.controller.data_controller import DataController


class UploadScreen(Screen):
    """
        A upload_screen mögötti logikát biztosító osztály.
    """
    dataController = DataController()

    def on_enter(self, *args):
        self.ids.category_spinner.values = []
        for category in self.dataController.get_categories():
            self.ids.category_spinner.values.append(category)

    def save(self, category: str, amount: int, desc: str):
        """
            Elemnt egy új kiadást azáltal hogy meghívja
            a controller megfeleő függvényét,
            majd vissza vissza a főoldalra.
            Ha hibás az adat(hoányzik vagy a kiadás negatív) nem csinál semmit
        """
        if (category is None or amount is None or category == ""
                or amount == "" or int(amount) <= 0):
            print("HIBA: Hiányzó vagy hibás adat(ok)!")
        else:
            self.dataController.add_expense(category,
                                            int(amount),
                                            desc,
                                            datetime.date.today())

            self.back_to_main()

    def back_to_main(self):
        """
            Vissza viszi a felhasználükat a
            home screen-re és resteli az inputokat.
        """
        self.ids.amount.text = ""
        self.ids.desc.text = ""

        self.parent.current = "main_screen"
