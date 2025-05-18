"""
    Ez az elem tartalmazza a YearDataDao osztályt
    amit a yea_data_controller használ.
"""

import json
import os


class YearDataDao:
    """
        Osztály amely a yearData.json fájlhoz biztosít műveleteket.
    """
    path = os.path.join(".", "..", "expense_tracker", "Data", "yearData.json")

    def get_expenses(self):
        """
            Beolvassa a yearData.json fájlt és visszadja belőle a kidásokat.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("months", [])

        print("HIBA: Nem létezik a yearData.json fájl")
        return []

    def new_month(self, month, amount):
        """"
            Hozzáadd egy új hónapot a months tömbhöz a
            paraméterek alapján ahol a months a hónap
            száma és az amount a havi kiádás mértéke,
            majd ez elmenti a yearData.json fájlba.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            data.get("months", []).append({
                "month": month,
                "expense": amount
            })

            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            return True
        print("HIBA: Nem létezik a yearData.json fájl")
        return False

    def delete_months(self):
        """
            Kitörli az összes hónapot a yearData.json fájlból.
        """
        if os.path.exists(self.path):
            with open(self.path, mode="w", encoding="utf-8") as f:
                json.dump({"months": []}, f, indent=4)

            return True
        print("HIBA: Nem létezik a yearData.json fájl")
        return False
