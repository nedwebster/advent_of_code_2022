import numpy as np
from time import sleep
import itertools


class TreeFinder():

    def _read_input(self, input_path):

        with open(input_path) as file:
            trees = file.read()

        return self._format_inputs(trees)

    def _format_inputs(self, trees):

        trees = trees.split("\n")
        trees = [
            [x for x in y] for y in trees
        ]

        trees = np.array(trees)
        trees = trees.astype(int)

        return trees
    
    def find_big_trees(self, trees):
        big_trees = 0

        for i in range(1, trees.shape[0] -1):  
            for j in range(1, trees.shape[1] - 1):

                tree = trees[i, j]

                i_array = trees[i]
                j_array = trees[:, j]

                left_i = i_array[:j]
                right_i = i_array[j+1:]

                up_j =j_array[:i]
                down_j =j_array[i+1:]

                if any([all(tree > left_i), all(tree > right_i), all(tree > up_j), all(tree > down_j)]):
                    big_trees += 1

        big_trees = big_trees + trees.shape[0]*2 + trees.shape[1]*2 - 4

        return big_trees

    def find_scenic_score(self, trees):

        scenic_scores = []

        for i in range(1, trees.shape[0] -1):
            for j in range(1, trees.shape[1] - 1):

                # identify tree
                tree = trees[i, j]

                # get arrays for tree
                i_array = trees[i]
                j_array = trees[:, j]

                # split x and y axis into each side
                left = i_array[:j].tolist()
                right = i_array[j+1:].tolist()
                up =j_array[:i].tolist()
                down =j_array[i+1:].tolist()

                # reverse left and up so the array is ordered correctly
                left.reverse()
                up.reverse()

                # calculate the vision each way
                left_vision = len(list(itertools.takewhile(lambda x: x<tree, left)))
                right_vision = len(list(itertools.takewhile(lambda x: x<tree, right)))
                up_vision = len(list(itertools.takewhile(lambda x: x<tree, up)))
                down_vision = len(list(itertools.takewhile(lambda x: x<tree, down)))

                # add the blocking tree to the vision length (if not an edge tree)
                if left_vision < len(left):
                    left_vision += 1

                if right_vision < len(right):
                    right_vision += 1
                
                if up_vision < len(up):
                    up_vision += 1
                
                if down_vision < len(down):
                    down_vision += 1
        
                scenic_scores.append(left_vision * right_vision * up_vision * down_vision)

        return max(scenic_scores)
