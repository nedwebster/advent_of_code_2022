from code import rucksack


def test_part_one():

    organiser = rucksack.Organiser()

    rucksacks = organiser._read_input("inputs/03_day_three.txt")

    assert organiser.get_misplaced_items_score(rucksacks) == 7845


def test_part_two():

    organiser = rucksack.Organiser()

    rucksacks = organiser._read_input("inputs/03_day_three.txt")

    assert organiser.get_badge_score(rucksacks) == 2790
