"""
    Ez az elem tartalmazza a DataDAO osztályt
    amit a data_controller használ.
"""

import os
import json
import datetime


class DataDAO:
    """
        Osztály amely a data.json fájlhoz biztosít műveleteket.
    """
    path = os.path.join(".", "..", "expense_tracker", "Data", "data.json")

    def get_categories(self):
        """
            Beolvasa a data.json fájlt és visszaadja belőle a kategóriákat
             és az azokhoz tartozó adatokat.
        """

        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            return data.get("categories", [])

        print("HIBA: Nem létezik a data.json fájl!")
        return []

    def get_limit(self):
        """
            Beolvasa a data.json fájlt és visszaadja a havi limitet.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            return data.get("limit", 0)

        print("HIBA: Nem létezik a data.json fájl!")
        return 0

    def get_last_log_in(self):
        """
            Beolvasa a data.json fájlt és visszaadja
            hogy mikor volt legutolsára megnyitva az alkalmazás.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            return data.get("lastLogIn", None)

        print("HIBA: Nem létezik a data.json fájl!")
        return None

    def delete_category(self, category_name):
        """
            Kitörli a megadott kategóriát a data.json fájlból.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            if category_name is None:
                data["categories"] = []
                return True

            volt = False

            for category in data["categories"]:
                if category["name"] == category_name:
                    data["categories"].remove(category)
                    volt = True

            if not volt:
                return False

            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            return True

        print("HIBA: Nem létezik a data.json fájl!")
        return False

    def set_limit(self, limit: str):
        """
            Elmenti a paraméterben érkező havi
            kiadás limit értéket a data.json fájl limit adattagjába.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            data["limit"] = limit

            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True

        print("HIBA: Nem létezik a data.json fájl!")
        return False

    def add_expense(self, category: str, amount: int,
                    desc: str, date: datetime.date):
        """
            Hozzád egy új kiadást a paraméterben megadott
            kategirához a többi paraméter által meghatárzott
            értékekkel majd ez elementi a data.json fájlba.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            for cat in data["categories"]:
                if cat["name"] == category:
                    cat["expenses"].append({
                        "amount": amount,
                        "date": str(date),
                        "desc": desc
                    })
                    break

            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True

        print("HIBA: Nem létezik a data.json fájl!")
        return False

    def add_category(self, new_category: str):
        """
            Hozzáadd egy új kiadás kategóriát a cetegories tömbhöz
            majd ezt elemnti a data.json fáljba.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            data["categories"].append({
                "name": new_category,
                "expenses": []
            })

            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True

        print("HIBA: Nem létezik a data.json fájl!")
        return False

    def reset_expenses(self):
        """"
            Kitörli az összes kiadás kategória kiadásait
            majd ez elemnti a data.json fájlba.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            for category in data["categories"]:
                category["expenses"] = []

            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True

        print("HIBA: Nem létezik a data.json fájl!")
        return False

    def set_last_log_in(self, date: datetime.date):
        """
            Elmenti a paraméterben érkező dátumot a d
            ata.json fájl lastLogIn adattagjába.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            data["lastLogIn"] = str(date)

            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                return True

        print("HIBA: Nem létezik a data.json fájl!")
        return False
