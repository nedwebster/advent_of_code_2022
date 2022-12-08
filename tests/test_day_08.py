from code import treehouse


def test_part_one():

    tf = treehouse.TreeFinder()

    trees = tf._read_input("inputs/08_day_eight.txt")

    big_trees = tf.find_big_trees(trees)

    assert big_trees == 1809


def test_part_two():

    tf = treehouse.TreeFinder()

    trees = tf._read_input("inputs/08_day_eight.txt")

    scenic_score = tf.find_scenic_score(trees)

    assert scenic_score == 479400
