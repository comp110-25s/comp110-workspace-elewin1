__author__: str = "730521441"


def invert(a: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in a:
        if a[key] in inverted:
            raise KeyError("duplicate keys")
        else:
            inverted[a[key]] = key
    return inverted


def count(b: list[str]) -> dict[str, int]:
    dictionary: dict[str, int] = {}
    for i in b:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary


def favorite_color(names: dict[str, str]) -> str:
    winner: str = ""
    highest_number: int = 0
    count_list: dict[str, int] = count(list(names.values()))
    for color in count_list:
        if count_list[color] > highest_number:
            highest_number = count_list[color]
            winner = color
    return winner


def bin_len(words: list[str]) -> dict[int, set[str]]:
    dictionary: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in dictionary:
            dictionary[length] = set()
        dictionary[length].add(word)
    return dictionary
