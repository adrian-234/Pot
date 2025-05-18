"""
    Ez az elem tartalmazza a DetailScreen osztályt
    ami az adott kiadási kategóra részletes megjelenítésért felel.
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from src.expense_tracker.controller.data_controller import DataController


class DetailScreen(Screen):
    """
        A detail_screen mögötti logikát biztosító osztály.
    """
    dataController = DataController()
    currentCategory = ""

    def on_enter(self, *args):
        self.ids.expenses_container.clear_widgets()

        self.ids.category_title.text = self.currentCategory

        for expense in self.dataController.get_all_by_category(self.currentCategory)["expenses"]:
            box = BoxLayout(
                orientation='horizontal',
                spacing=5,
                size_hint_y=None,
                height=60,
            )

            label = Label(
                    text=str(expense["date"]),
                    size_hint_y=None,
                    halign='left',
                )
            label.bind(texture_size=lambda instance, value:
                       setattr(instance, 'height', value[1]))

            label.bind(size=lambda instance, size:
                       setattr(instance, 'text_size', size))
            box.add_widget(label)

            label2 = Label(
                text=str(expense["amount"])+" Ft",
                size_hint_y=None,
                halign='right',
            )
            label2.bind(texture_size=lambda instance, value:
                        setattr(instance, 'height', value[1]))
            label2.bind(size=lambda instance, size:
                        setattr(instance, 'text_size', size))
            box.add_widget(label2)

            self.ids.expenses_container.add_widget(box)

            if expense["desc"] != "":
                label3 = Label(
                    text=expense["desc"],
                    italic=True,
                    size_hint_y=None,
                    halign='left',
                )
                label3.bind(texture_size=lambda instance, value:
                            setattr(instance, 'height', value[1]))
                label3.bind(width=lambda instance, size:
                            setattr(instance, 'text_size', (size, None)))
                self.ids.expenses_container.add_widget(label3)
