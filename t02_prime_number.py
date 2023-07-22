# Úkol 2 - Prvočísla a palindromy
"""
Připravte program, který vypíše první prvočíslo, které je větší než uživatelem zadaná hodnota a které je zároveň
palindromem.

#### Příklady vstupů a očekávané výstupy
| Vstup    | Výstup          |
| -------- | --------------- |
| 100      | 101             |
| 100000   | 1003001         |
| xy       | Invalid input!  |
"""


def next_prime_number(number):
    def is_palindrome(s):
        return s[::-1] == s

    def is_prime(n):
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    number += number % 2 + 1  # Sets the next higher odd number
    while True:
        if is_palindrome(str(number)):
            if is_prime(number):
                return number
        number += 2


# Main program
try:
    number = int(input("Zadej celé kladné minimálně dvojciferné číslo: "))
    if number < 10:
        raise ValueError()
    else:
        print(next_prime_number(number))
except ValueError:
    print("Invalid input!")
