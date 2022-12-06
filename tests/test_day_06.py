from code import tuning


def test_part_one():

    cs = tuning.CommunicationSystem()

    datastream = cs._read_input("inputs/06_day_six.txt")

    output = cs.find_first_distinct_pattern(datastream, pattern_len=4)

    assert output == 1757


def test_part_two():

    cs = tuning.CommunicationSystem()

    datastream = cs._read_input("inputs/06_day_six.txt")

    output = cs.find_first_distinct_pattern(datastream, pattern_len=14)

    assert output == 2950
