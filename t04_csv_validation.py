# Úkol 4 - Validace textového souboru
"""
- Připravte script pro validaci [tohoto](https://pastebin.com/tNmieVFn) CSV souboru ve formátu:
    - Jméno knihy; Jméno autora; ISBN; cena
- Validujte, že všechny hodnoty jsou zadané, že ISBN je ve správném formátu a že cena je kladné číslo
    - cena je zadána jako desetinné číslo oddělené tečkou nebo čárkou, doplněné o měnu (Kč nebo €)
- Pokud narazíte na nevalidní řádek, vypište číslo řádku a jaký nastal problém

# Příklad výstupu
Invalid ISBN on line: 21
Missing title on line: 67
Invalid price on line: 90
Missing author on line: 149
Error! 3 column(s) on line 185!
Invalid price on line: 224
"""

import csv


class CSVReader:
    def __init__(self, filename, delimiter=';'):
        self.filename = filename
        self.delimiter = delimiter
        self.file = None
        self.reader = None
        self.row = None
        self.row_number = 0

    def open(self):
        self.file = open(self.filename, 'r')
        self.reader = csv.reader(self.file, delimiter=self.delimiter)

    def validate(self):
        xx = self.row
        return None

    def read_row(self):
        try:
            self.row = next(self.reader)
        except StopIteration:
            self.row = None
        return self.row

    def close(self):
        self.file.close()


reader = CSVReader('t04_library.csv')
try:
    while True:
        if reader.read_row() is None:
            break
        validate = reader.validate()
        if validate is not None:
            print(f"{validate} on line: {reader.row}")

except FileNotFoundError:
    print('Soubor nebyl nalezen')
except PermissionError:
    print('Nemáte oprávnění ke čtení souboru')
except csv.Error as e:
    print(f'Chyba při čtení CSV souboru: {e}')

