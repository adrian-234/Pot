"""
    Ez az elem tartalmazza a MainScreen osztályt
    ami a főoldal megjelenítésért felel.
"""

import datetime

from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from src.expense_tracker.controller.data_controller import DataController
from src.expense_tracker.controller.year_controller import YearController


class MainScreen(Screen):
    """
       A main_screen mögötti logikát biztosító osztály.
    """
    dataController = DataController()
    yearController = YearController()
    progress = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        today = datetime.date.today()
        last_log_in = self.dataController.get_last_log_in()

        if today.year != last_log_in.year:
            self.yearController.delete_months()
        elif today.month != last_log_in.month:
            self.yearController.new_month(last_log_in.month,
                                          self.dataController.get_sum_expenses())

        if today.month != last_log_in.month:
            self.dataController.reset_expenses()

        self.dataController.set_last_log_in(today)

    def on_enter(self, *args):
        self.ids.categories_container.clear_widgets()

        for category in self.dataController.get_expenses_by_category():
            label = Button(
                text="• " + category["name"],
                color=(1, 1, 1, 1),
                font_size='16sp',
                background_color=(1, 1, 1, 0),
            )
            label.bind(size=label.setter('text_size'))
            label.bind(on_press=lambda btn, name=category["name"]:
                       self.open_category(name))
            self.ids.categories_container.add_widget(label)

            label = Label(
                text=str(category["expense"]) + " Ft",
                color=(1, 1, 1, 1),
                font_size='16sp',
                halign='right',
            )
            label.bind(size=label.setter('text_size'))
            self.ids.categories_container.add_widget(label)

        remaining_money = (self.dataController.get_limit() -
                           self.dataController.get_sum_expenses())

        self.ids.money.text = str(remaining_money) + " Ft"

        self.progress = (max(remaining_money, 0) /
                         self.dataController.get_limit()) \
            if self.dataController.get_limit() > 0 else 0

    def open_category(self, name):
        """
            Beállítja a detail_screen-en azt hogy,
             melyik kaidási kategória adatait kell megjeleniteni
        """
        self.parent.get_screen("detail_screen").currentCategory = name
        self.parent.current = "detail_screen"
