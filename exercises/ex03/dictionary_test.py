__author__: str = "730521441"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_1() -> None:
    a: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(a) == {"b": "a", "d": "c"}


def test_invert_2() -> None:
    a: dict[str, str] = {"eliza": "lewin", "carol": "pearl"}
    assert invert(a) == {"lewin": "eliza", "pearl": "carol"}


def test_invert_3() -> None:
    a: dict[str, str] = {"eliza": "lewin", "carol": ""}
    assert invert(a) == {"lewin": "eliza", "": "carol"}


def test_count_1() -> None:
    b: list[str] = ["eliza", "lewin", "eliza"]
    assert count(b) == {"lewin": 1, "eliza": 2}


def test_count_2() -> None:
    b: list[str] = ["yo", "yo", "yo"]
    assert count(b) == {"yo": 3}


def test_count_3() -> None:
    b: list[str] = ["", "lewin", "eliza"]
    assert count(b) == {"": 1, "lewin": 1, "eliza": 1}


def test_favorite_color_1() -> None:
    names: dict[str, str] = {"eliza": "blue", "carol": "red", "john": "blue"}
    assert favorite_color(names) == "blue"


def test_favorite_color_2() -> None:
    names: dict[str, str] = {"eliza": "blue", "carol": "red", "carry": "red"}
    assert favorite_color(names) == "red"


def test_favorite_color_3() -> None:
    names: dict[str, str] = {"eliza": "blue", "carol": "red"}
    assert favorite_color(names) == "blue"


def test_bin_len_1() -> None:
    words: list[str] = ["the", "quick", "fox"]
    assert bin_len(words) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_2() -> None:
    words: list[str] = ["the", "the", "fox"]
    assert bin_len(words) == {3: {"the", "fox"}}


def test_bin_len_3() -> None:
    words: list[str] = ["eliza", ""]
    assert bin_len(words) == {5: {"eliza"}, 0: {""}}
