from code import rock_paper_scissors


def test_part_one():

    rps = rock_paper_scissors.RockPaperScissors()

    matches = rps._read_input("inputs/day_two.txt")

    result = rps.get_results(matches)

    assert result == 13675


def test_part_two():

    rps = rock_paper_scissors.RockPaperScissors()

    matches = rps._read_input("inputs/day_two.txt")

    result = rps.get_results(matches, needs_map=True)

    assert result == 14184
