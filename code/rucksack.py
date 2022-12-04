import string


class Rucksack():

    def __init__(self, contents: str):

        self.full_contents = contents
        self.split_contents = self._split_compartments(contents)
        self.common_item = self._get_common_item()

    def _split_compartments(self, contents):

        n_items = len(contents)

        compartment_1 = contents[:int(n_items/2)]
        compartment_2 = contents[int(n_items/2):]

        return compartment_1, compartment_2

    def _get_common_item(self):

        return [
            x for x in self.split_contents[0]
            if x in self.split_contents[1]
        ][0]


class Organiser():

    def __init__(self):

        self.priority_map = dict(zip(
            string.ascii_lowercase + string.ascii_uppercase,
            range(1, 53),
        ))

    def _read_input(self, input_path):

        with open(input_path) as file:
            contents = file.read()

        return self._format_input(contents)

    def _format_input(self, contents):

        contents = contents.split("\n")

        rucksacks = [Rucksack(x) for x in contents]

        return rucksacks

    def get_misplaced_items_score(self, rucksacks):

        common_items = [x.common_item for x in rucksacks]

        scores = [self.priority_map[item] for item in common_items]

        return sum(scores)

    def _chunk_rucksacks(self, rucksacks, n=3):

        chunked_rucksacks = []

        for i in range(0, len(rucksacks), n):
            chunked_rucksacks.append(rucksacks[i:i + n])
    
        return chunked_rucksacks

    def _get_badge(self, three_rucksacks):

        badge = [
            x for x in three_rucksacks[0].full_contents if
            x in three_rucksacks[1].full_contents and
            x in three_rucksacks[2].full_contents
        ][0]

        return badge

    def get_badge_score(self, rucksacks):
        
        chunked_rucksacks = self._chunk_rucksacks(rucksacks, 3)

        badges = [self._get_badge(x) for x in chunked_rucksacks]

        scores = [self.priority_map[item] for item in badges]

        return sum(scores)
