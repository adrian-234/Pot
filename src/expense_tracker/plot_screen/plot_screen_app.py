"""
    Ez az elem tartalmazza a PlotScreen osztályt
    ami kölönböző diagrommokat jelenít meg a kiadások
    alpján.
"""

from kivy.uix.screenmanager import Screen
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from src.expense_tracker.controller.data_controller import DataController
from src.expense_tracker.controller.year_controller import YearController


class PlotScreen(Screen):
    """
       A plot_screen mögötti logikát biztosító osztály.
   """
    dataController = DataController()
    yearController = YearController()

    def on_enter(self, *args):
        plt.clf()
        self.ids.box.clear_widgets()

        monthly = []
        monthly_labels = []
        for category in self.dataController.get_expenses_by_category():
            if category["expense"] > 0:
                monthly.append(category["expense"])
                monthly_labels.append(category["name"])

        yearly = []
        yearly_labels = []
        for month in self.yearController.get_expenses():
            if month["expense"] > 0:
                yearly.append(month["expense"])
                match month["month"]:
                    case 1:
                        yearly_labels.append("Január")
                    case 2:
                        yearly_labels.append("Február")
                    case 3:
                        yearly_labels.append("Március")
                    case 4:
                        yearly_labels.append("Április")
                    case 5:
                        yearly_labels.append("Május")
                    case 6:
                        yearly_labels.append("Június")
                    case 7:
                        yearly_labels.append("Július")
                    case 8:
                        yearly_labels.append("Augusztus")
                    case 9:
                        yearly_labels.append("Szeptember")
                    case 10:
                        yearly_labels.append("Október")
                    case 11:
                        yearly_labels.append("November")
                    case 12:
                        yearly_labels.append("December")
                    case _:
                        yearly_labels.append("HIBA")
                        print("HIBA: Hibás dátum formátum a yearData.json-ben")

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 6))
        fig.patch.set_facecolor((0, 0, 0, 0))

        ax1.pie(monthly,
                labels=monthly_labels,
                radius=1,
                textprops={'color': 'white'})
        ax1.set_position([0.2, 0.55, 0.6, 0.4])
        ax1.text(-0.2, 1,
                 "Havi kiadások:",
                 color='white',
                 fontsize=12,
                 ha='left',
                 transform=ax1.transAxes)

        ax2.pie(yearly,
                labels=yearly_labels,
                radius=1,
                textprops={'color': 'white'})
        ax2.set_position([0.2, 0.1, 0.6, 0.4])
        ax2.text(-0.2, 1,
                 "Éves kiadások:",
                 color='white',
                 fontsize=12,
                 ha='left',
                 transform=ax2.transAxes)

        self.ids.box.add_widget(FigureCanvasKivyAgg(fig))
