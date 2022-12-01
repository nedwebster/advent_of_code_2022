from code import calories


def test_part_one():

    calorie_reader = calories.CalorieReader()
    calorie_list = calorie_reader.read_input(input_path="inputs/day_one.txt")
    output = calorie_reader.find_max_calories(calorie_list, position=0)

    assert output == 72478


def test_part_two():

    calorie_reader = calories.CalorieReader()
    calorie_list = calorie_reader.read_input(input_path="inputs/day_one.txt")

    output0 = calorie_reader.find_max_calories(calorie_list, position=0)
    output1 = calorie_reader.find_max_calories(calorie_list, position=1)
    output2 = calorie_reader.find_max_calories(calorie_list, position=2)

    output = output0 + output1 + output2

    assert output == 210367
