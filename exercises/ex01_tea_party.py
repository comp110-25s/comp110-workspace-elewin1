"""The goal of this program is to plan a cozy tea party based on the number of guests"""

__author__: str = "730521441"


def main_planner(guests: int) -> None:
    """the entry point of the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """determine number of needed tea bags"""
    return people * 2


def treats(people: int) -> int:
    """determine number of treats needed"""
    teas = tea_bags(people=people)
    return int(teas * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """determines the cost of all treat and teas"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
