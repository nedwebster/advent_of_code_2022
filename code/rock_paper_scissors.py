class RockPaperScissors():

    def __init__(self):

        self.pick_scores = {
            "X": 1,
            "Y": 2,
            "Z": 3,
        }

        self.result_scores = {
            "A X": 3,
            "B Y": 3,
            "C Z": 3,
            "A Y": 6,
            "B Z": 6,
            "C X": 6,
            "A Z": 0,
            "B X": 0,
            "C Y": 0,
        }

        self.required_result_map = {
            "A X": "A Z",
            "B Y": "B Y",
            "C Z": "C X",
            "A Y": "A X",
            "B Z": "B Z",
            "C X": "C Y",
            "A Z": "A Y",
            "B X": "B X",
            "C Y": "C Z",
        }

    def _read_input(self, input_path):

        with open(input_path) as file:
            matches = file.read()

        return self._format_matches(matches)

    def _format_matches(self, matches):

        return matches.split("\n")

    def get_results(self, matches, needs_map=False):

        if needs_map:
            matches = [self.required_result_map[x] for x in matches]

        pick_scores = [self.pick_scores[x[2]] for x in matches]
        match_scores = [self.result_scores[x] for x in matches]

        total_scores = [x + y for x, y in zip(pick_scores, match_scores)]

        return sum(total_scores)
