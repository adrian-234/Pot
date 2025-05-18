"""
    Ez az elem tartalmazza a DataController osztályt
    amivel a különböző view-k hozzá tudnak férni az adatokhoz.
"""

import datetime
from src.expense_tracker.dao.data_dao import DataDAO


class DataController:
    """
        Függvéynek melyeket a különböző view-k tudnak
        használni az adat olvasáshoz és modosításhoz.
    """

    dao = DataDAO()

    def get_expenses_by_category(self):
        """
            Visszadja adja ketegóriákra bontva a havi kiadásokat.
        """
        res = []
        for category in self.dao.get_categories():
            expenses_sum = 0
            for expense in category["expenses"]:
                expenses_sum += int(expense["amount"])

            res.append({
                "name": category["name"],
                "expense": expenses_sum
            })

        return res

    def get_all_by_category(self, category_name: str):
        """
            Visszadja egy keresett kategória összes adatát.
        """
        for category in self.dao.get_categories():
            if category["name"] == category_name:
                return category
        return None

    def get_categories(self):
        """
            Vissza adja az összes kategória nevét egy tömben.
        """
        res = []
        for category in self.dao.get_categories():
            res.append(category["name"])
        return res

    def get_sum_expenses(self):
        """
            Visszadja az adott havi kiadások összegét.
        """
        res = 0
        for category in self.dao.get_categories():
            for expense in category["expenses"]:
                res += int(expense["amount"])
        return res

    def get_limit(self):
        """
            Visszadja a havi limitet.
        """
        return int(self.dao.get_limit())

    def get_last_log_in(self):
        """
            Visszadja az alkalmazás utolsó megnyitásának az idejét.
        """
        return datetime.date.fromisoformat(self.dao.get_last_log_in())

    def delete_category(self, category_name: str):
        """
            Meghívja a DAO delete_category függvényét,
             hogy kitörölje a megadott kategóriát.
        """
        return self.dao.delete_category(category_name)

    def delete_all(self):
        """
            Kitörli az összes hónapot.
        """
        for category in self.dao.get_categories():
            self.dao.delete_category(category["name"])
        self.dao.set_limit("0")

    def save_limit(self, limit: str):
        """
            Meghívja a DAO set_limit függvényét,
            hogy elmentse az új havi limitet.
        """
        return self.dao.set_limit(limit)

    def add_expense(self, category: str, amount: int,
                    desc: str, date: datetime.date):
        """
            Meghívja a DAO add_expense függvényét,
             hogy elmentse az új kiadást.
        """
        return self.dao.add_expense(category, amount, desc, date)

    def add_category(self, new_category: str):
        """
            Létrehozz egy új kategóriát a new_category
            paraméter alapján, de előtte ellenőrzi,
            hogy már létezik-e ilyen nevű kategória és
            ha igen akkor nem hozz létre egy újat.
        """
        for category in self.dao.get_categories():
            if category["name"] == new_category:
                print("HIBA: Ilyen kategória már létezik.")
                return False

        return self.dao.add_category(new_category)

    def set_last_log_in(self, date: datetime.date):
        """
            Meghívja a DAO set_last_log_in függvényét, hogy elmentse
            az új bejelntkezés dátumát limitet.
        """
        self.dao.set_last_log_in(date)

    def reset_expenses(self):
        """
            Meghívja a DAO reset_expenses függvényét,
             hogy kitörölje az összes havi kiadást.
        """
        self.dao.reset_expenses()
