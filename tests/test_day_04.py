from code import cleanup


def test_part_one():

    cc = cleanup.CampCleanup()

    tasks = cc._read_input("inputs/04_day_four.txt")

    assert cc.get_number_of_full_overlaps(tasks) == 424


def test_part_two():

    cc = cleanup.CampCleanup()

    tasks = cc._read_input("inputs/04_day_four.txt")

    assert cc.get_number_of_partial_overlaps(tasks) == 804
