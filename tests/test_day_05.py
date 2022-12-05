from code import supplystacks


def test_part_one():

    gcc = supplystacks.GiantCargoCrane()

    crates, rules = gcc._read_input("inputs/05_day_five.txt")

    moved_crates = gcc.move_all_crates(crates, rules, model="9000")

    assert gcc.get_top_boxes(moved_crates) == "WSFTMRHPP"


def test_part_two():

    gcc = supplystacks.GiantCargoCrane()

    crates, rules = gcc._read_input("inputs/05_day_five.txt")

    moved_crates = gcc.move_all_crates(crates, rules, model="9001")

    assert gcc.get_top_boxes(moved_crates) == "GSLCMFBRP"
