"""
# Úkol 3 - Hokej
- Z webu https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089 vyscrapujte výsledky všechny zápasů
- Vyfiltrujte zápasy, které vyhrál Váš oblíbený tým
- Vypište datum a jméno poraženého týmu

# Příklad výstup
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
"""

import sys
from html.parser import HTMLParser
import urllib.request


class MatchParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.matches = []
        self.current_match = {}
        self.current_tag = ''
        self.in_match = False
        self.extract_score = False

    # < div class ="datetime-container" > 6. & nbsp;3. • 17: 20 <!--  ###--></div>
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if attr[0] == 'class':
                    if 'datetime-container' in attr[1]:
                        self.current_tag = 'datetime'
                        self.current_match = {}
                        self.in_match = True
                    # elif 'team-container team-home' in attr[1] and self.in_match:
                    elif 'team-name' in attr[1] and self.in_match:
                        if 'home' not in self.current_match:
                            self.current_tag = 'home'
                        else:
                            self.current_tag = 'away'
                    elif 'score' in attr[1] and self.in_match:
                        self.current_tag = 'score'
                        self.extract_score = True
        elif tag == 'span' and self.current_tag == 'score':
            self.current_tag = 'score_separator'

    def handle_endtag(self, tag):
        if tag == 'div' and self.current_match and 'away' in self.current_match:
            self.matches.append(self.current_match)
            # print(tag, self.current_match)
            self.current_match = {}
            self.in_match = False
        elif tag == 'span' and self.current_tag == 'score':
            self.current_tag = 'score_separator'

    def handle_data(self, data):
        if self.current_tag in ['home', 'away']:
            self.current_match[self.current_tag] = data.strip()
            self.current_tag = ''
        elif self.current_tag == 'score':
            home_score = data.strip()
            self.current_match['home_score'] = home_score
            self.current_tag = ''
        # elif self.current_tag == 'score_separator':
        elif self.extract_score:
            away_score = data.strip()
            # print(f"***{away_score}***")
            if away_score.isdigit():
                self.current_match['away_score'] = away_score
                self.current_tag = ''
                self.extract_score = False
        elif self.current_tag == 'datetime':
            datetime_str = data.strip()[:8]
            end_date = datetime_str.rfind('.')
            self.current_match['date'] = datetime_str[:end_date+1]
            self.current_tag = ''
            # print(f"***{datetime_str[:end_date]}***")


url = 'https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089'
try:
    with urllib.request.urlopen(url) as response:
        page = response.read().decode('utf-8')
except Exception as error:
    print(f"Error: {error}")
    sys.exit()

parser = MatchParser()
parser.feed(page)

my_team = input("Zadej název svého oblíbeného týmu: ")
# my_team = "Brno"
find_team = False

for match in parser.matches:
    match_date = match.get('date', '')
    home_team = match.get('home', '')
    away_team = match.get('away', '')
    home_score = match.get('home_score', '')
    away_score = match.get('away_score', '')
    # print(f'Datum: {match_date}  {home_team} vs {away_team} - {home_score}:{away_score}')
    if home_team == my_team and home_score > away_score:
        print(f'{match_date} jsme porazili {away_team}')
        find_team = True
    elif away_team == my_team and away_score > home_score:
        print(f'{match_date} jsme porazili {home_team}')
        find_team = True

if not find_team:
    print(f"Tvůj tým {my_team} nezaznamenal žádnou výhru.")
