"""
    Ez az elem tartalmazza a YearController osztályt
    amivel a különböző view-k hozzá tudnak férni az adatokhoz.
"""

from src.expense_tracker.dao.year_data_dao import YearDataDao


class YearController:
    """
        Függvéynek melyeket a különböző view-k tudnak
         használni az adat olvasáshoz és modosításhoz.
    """
    dao = YearDataDao()

    def get_expenses(self):
        """
            Meghívja a DAO get_expenses függvényét,
             hogy elmentse az új havi limitet.
        """
        return self.dao.get_expenses()

    def new_month(self, month, amount):
        """
            Meghívja a DAO new_month függvényét, hogy elmentsen egy új hónapot.
        """
        return self.dao.new_month(month, amount)

    def delete_months(self):
        """
            Meghívja a DAO delete_months függvényét, hogy kitörlölje az
            összes meglévő elmentett hónapot és a hozzájuk tartozó kiadásokat.
        """
        return self.dao.delete_months()
