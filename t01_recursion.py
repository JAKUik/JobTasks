"""
### Úkol 1 - Rekurze:
Napište funkci ``word_chain``, která na vstupu dostane libovolně velkou množinu slov a vrátí největší počet slov,
které lze zřetězit jeden po druhém tak, že první písmeno druhého slova je stejné jako poslední písmeno prvního slova.
Opakování slov není povoleno.

Příklady:
word_chain({'goose', 'dog', 'ethanol'}) == 3  # dog – goose – ethanol
word_chain({'why', 'new', 'neural', 'moon'}) == 3  # (moon – new – why)
"""


def search_all_paths(words, current_word=None, path=None):
    """
    Recursive function. Searches all chained lists
    :param words: A set of words
    :param current_word: Actual processed word
    :param path: List of processed words
    :return: All chained lists
    """
    if path is None:
        path = []
    if current_word:
        path.append(current_word)
    all_paths = []
    for word in words:
        if not current_word or word[0] == current_word[-1]:
            remaining_words = words.copy()
            remaining_words.remove(word)
            new_paths = search_all_paths(remaining_words, word, path.copy())
            all_paths.extend(new_paths)
    if not all_paths and current_word:
        all_paths.append(path)
    return all_paths


def word_chain(words):
    """
    Searches for the longest list from all chained lists
    :param words: A set of words
    :return: Longest list
    """
    all_paths = search_all_paths(words)
    longest_path = []
    for path in all_paths:
        if len(longest_path) <= len(path):
            # print(path)
            longest_path = path
    return longest_path


print(word_chain({'goose', 'dog', 'ethanol'}))
print(word_chain({'why', 'new', 'neural', 'moon'}))
print(word_chain({'red', 'rabbit', 'tulip', 'sunflower', 'pear', 'elephant', 'rose', 'tiger', 'apple'}))

print(word_chain({'ahoj', 'nazdar', 'lojza', 'růže', 'emerald', 'skupina', 'pozdrav', 'opona', 'program', 'otec',
                  'mák', 'léto', 'voda', 'opice', 'družka', 'film', 'komedie', 'leopold', 'jaro', 'epos'}))

