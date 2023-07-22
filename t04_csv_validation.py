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


class TextFileReader:
    def __init__(self, filename, delimiter=';'):
        self.filename = filename
        self.delimiter = delimiter
        self.file = None
        self.line = None
        self.line_number = 0

    def open(self):
        self.file = open(self.filename, 'r', encoding='utf-8')

    def read_line(self):
        self.line = self.file.readline()
        self.line_number += 1
        return self.line

    def validate(self):
        def check_price_format(price):
            import re
            pattern = r'^\-?\d+([.,]\d{1,2})?\s*(Kč|€)$'
            match = re.match(pattern, price)
            return bool(match)

        r = self.line.split(self.delimiter)
        if len(r) < 4:
            return f"Error! {len(r)} column(s)"
        if len(r[0].strip()) == 0:
            return "Missing title"
        if len(r[1].strip()) == 0:
            return "Missing author"
        if len(r[2].strip()) != 10 and len(r[2].strip()) != 13:
            return "Invalid ISBN"
        if len(r[3].strip()) == 0 or not check_price_format(r[3].strip()):
            return "Invalid price"
        return None

    def close(self):
        if self.file:
            self.file.close()


reader = TextFileReader('t04_library.csv')
try:
    reader.open()
    while True:
        if not reader.read_line():
            break
        # print(f"{reader.line_number} - {reader.line}", end="")
        validate = reader.validate()
        if validate is not None:
            print(f"{validate} on line: {reader.line_number}")

except FileNotFoundError:
    print('Soubor nebyl nalezen')
except PermissionError:
    print('Nemáte oprávnění ke čtení souboru')
finally:
    reader.close()




