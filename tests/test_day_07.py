import numpy as np

from code import file_storage


def test_part_one():

    fs = file_storage.FileStorage()
    commands = fs._read_input("inputs/07_day_seven.txt")

    fs.build_file_structure(commands[1:])

    summed_dirs = file_storage.recursive_recursive_dir_sum(fs.fs)

    output = 0
    for x in summed_dirs:
        output += sum([v for v in x.values() if v <= 100000])

    assert output == 1644735


def test_part_two():

    fs = file_storage.FileStorage()
    commands = fs._read_input("inputs/07_day_seven.txt")

    fs.build_file_structure(commands[1:])

    summed_dirs = file_storage.recursive_recursive_dir_sum(fs.fs)

    total_used = list(summed_dirs[0].values())[0]
    max_space = 70000000
    required_space = 30000000
    remaining_space = max_space - total_used
    overflow = required_space - remaining_space

    final_output = []
    for x in summed_dirs:
        final_output += [v for v in x.values()]

    final_output = np.sort(final_output)

    y = [x for x in final_output if x >= overflow]

    assert y[0] == 1300850
