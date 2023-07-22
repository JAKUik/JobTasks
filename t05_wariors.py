# Úkol 5 - Třídy:
"""
Napište třídu 'Warrior' s atributy 'name' a 'maximum_health', dynamickým read-only atributem 'is_alive' 
a metodami pro sčítání ('+'), odčítání ('-') a výpisu informací o warriorovi. Popis atributů a metod:

\- 'Warrior.name' - název warriora inicializovaný přes konstruktor
\- 'Warrior.maximum_health' - kladné nenulové číslo inicializované přes konstruktor
\- 'Warrior.is_alive' - boolean hodnota indikující, zdali je warrior na živu, či je mrtev (viz odčítání)

\- 'Warrior + Warrior' - v případě, kdy oba dva warrioři jsou naživu, vrátí nového Warriora s atributy složenými 
    z atributů dvou sčítaných Warriorů. 'name' je vytvořen jako spojení názvu prvního a druhého Wariora
    oddělené mezerou a 'maximum_health' je vytvořen jako součet maximálního zdraví prvního a druhého warriora. 
    V opačném případě se nic nestane.
\- 'Warrior - Warrior' v případě, kdy oba dva warrioři jsou naživu, ubere obou warriorům jeden život. 
    Pokud warriorovi klesne život na hodnotu 0, je na trvalo považován za mrtvého ('is_alive' bude vracet 'False')
\- 'str(Warrior)' - vypíše informace o daném warriorovi ve formátu: 
    'Warrior(name="{name}", maximum_health={}, is_alive={})'

Příklad:
xena = Warrior(name="Xena",  maximum_health=1)
# str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=True)'
conan = Warrior(name="Barbar Conan",  maximum_health=2)
# True == xena.is_alive == conan.is_alive

child = xena + conan
# child.is_alive == True
# child.name == "Xena Barbar Conan"
# child.maximum_health == 3

fight = xena - conan
# fight is None
# xena.is_alive == False
# conan.is_alive == True
# str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=False)'

child_2 = xena + conan
# child_2 is None
"""


class Warrior:
    def __init__(self, name, maximum_health):
        self.name = name
        self.maximum_health = maximum_health
        self.health = maximum_health

    @property
    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Warrior(name='{self.name}', maximum_health={self.maximum_health}, is_alive={self.is_alive})"

    def __add__(self, other):
        if self.is_alive and other.is_alive:
            n = f"{self.name} {other.name}"
            h = self.maximum_health + other.maximum_health
            return Warrior(n, h)

    def __sub__(self, other):
        if self.is_alive and other.is_alive:
            self.health -= 1
            other.health -= 1


xena = Warrior(name="Xena",  maximum_health=1)
print(xena)
# str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=True)'
conan = Warrior(name="Barbar Conan",  maximum_health=2)
print(conan)
# Warrior(name='Barbar Conan', maximum_health=2, is_alive=True)

child_01 = xena + conan
print(child_01)

fight = xena - conan
print(xena)
print(conan)

child_02 = xena + conan
print(child_02)

