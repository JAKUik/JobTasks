# Processing tasks from an unknown company's entrance interview
Examples worked out independently by Jaroslav Kučera.
In some examples, I left debugging outputs.

## General
- During the processing, it will be possible to consult the assignment and partial solutions with representatives of the company.
- Tasks will be processed in the form of Python scripts.
- The Internet can be used for anything except live consultation with other people.
- Your approach to the assignment (especially analysis), fulfillment of requirements, robustness of the program, and code cleanliness will be evaluated.
- Only [standard Python libraries](https://docs.python.org/3/library/) can be used.

## Assignment
### Task 1 - Recursion:
Write a function ``word_chain`` that takes an arbitrarily large set of words as input and returns the largest number of words that can be chained one after the other so that the first letter of the second word is the same as the last letter of the first word. Repetition of words is not allowed.

Examples:

```
word_chain({'goose', 'dog', 'ethanol'}) == 3  # dog – goose – ethanol
word_chain({'why', 'new', 'neural', 'moon'}) == 3  # (moon – new – why)
```


### Task 2 - Prime numbers and palindromes
- Prepare a program that prints the first prime number greater than the value entered by the user and which is also a palindrome.

#### Examples of inputs and expected outputs
| Vstup    | Výstup          |
| -------- | --------------- |
| 100      | 101             |
| 100000   | 1003001         |
| xy       | Invalid input!  |


### Task 3 - Hockey
- Scrape all match results from https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089
- Filter out matches won by your favorite team
- Print date and name of defeated team

#### Example output
```
13. 3. jsme porazili Vítkovice
14. 3. jsme porazili Vítkovice
17. 3. jsme porazili Vítkovice
18. 3. jsme porazili Vítkovice
31. 3. jsme porazili Plzeň
1. 4. jsme porazili Plzeň
4. 4. jsme porazili Plzeň
7. 4. jsme porazili Plzeň
15. 4. jsme porazili Třinec
18. 4. jsme porazili Třinec
19. 4. jsme porazili Třinec
22. 4. jsme porazili Třinec
```

### Task 4 - Text file validation
- Prepare a script to validate [this](https://pastebin.com/tNmieVFn) CSV file in the format:
    - Book name; Author name; ISBN; price
- Validate that all values are entered, that ISBN is in the correct format, and that price is a positive number.
    - price is entered as a decimal number separated by a dot or comma, supplemented by currency (CZK or €)
- If you encounter an invalid line, print the line number and what problem occurred

#### Example output
```
Invalid ISBN on line: 21
Missing title on line: 67
Invalid price on line: 90
Missing author on line: 149
Error! 3 column(s) on line 185!
Invalid price on line: 224
```

### Task 5 - Classes:
Write a ``Warrior`` class with attributes ``name`` and ``maximum_health``, dynamic read-only attribute ``is_alive``, and methods for addition (``+``), subtraction (``-``), and printing information about a warrior. Description of attributes and methods:

\- ``Warrior.name`` - warrior name initialized via constructor.
\- ``Warrior.maximum_health`` - positive non-zero number initialized via constructor.
\- ``Warrior.is_alive`` - boolean value indicating whether the warrior is alive or dead (see subtraction).

\- ``Warrior + Warrior`` - if both warriors are alive, returns a new Warrior with attributes composed of attributes from two added Warriors. ``name`` is created as a concatenation of the first and second Warrior's names separated by a space and ``maximum_health`` is created as the sum of maximum health from the first and second warrior. Otherwise, nothing happens.
\- ``Warrior - Warrior`` if both warriors are alive, subtracts one life from both warriors. If a warrior's life drops to zero, he is permanently considered dead (``is_alive`` will return ``False``).
\- ``str(Warrior)`` - prints information about a given warrior in the format: ``Warrior(name="{name}", maximum_health={}, is_alive={})``

Example:

```
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
```