import numpy as np


class GiantCargoCrane():

    def __init__(self):

        pass

    def _read_input(self, input_path):

        with open(input_path) as file:
            crates = file.read()

        return self._format_inputs(crates)

    def _format_inputs(self, crates):

        crates, rules = crates.split("\n\n")

        crates = self._format_crates(crates)
        rules = self._format_rules(rules)

        return crates, rules

    def _format_crates(self, crates):

        crates = crates.split("\n")
        order = crates.pop(-1)

        keep_indexes = [order.index(str(i)) for i in range(1, 10)]

        def drop_redundant_index(crate, keep_indexes):
            
            return [crate[i] for i in keep_indexes]
        
        crates = [drop_redundant_index(x, keep_indexes) for x in crates]
        crates = np.transpose(crates).tolist()

        def drop_empty_index(crate):

            return [x for x in crate if x != " "] 
    
        crates = [drop_empty_index(x) for x in crates]

        return crates

    def _format_rules(self, rules):

        for x in ["move", "from", "to"]:
            rules = rules.replace(x, "")
        
        rules = rules.split("\n")

        rules = [x.strip().split() for x in rules]

        def convert_to_int(rule):

            return [int(x) for x in rule]

        return [convert_to_int(x) for x in rules]
    
    def move_crates(self, crates, command, model="9000"):

        moved_boxes = crates[command[1] - 1][:command[0]]

        del crates[command[1] - 1][:command[0]]

        if model == "9000":
            moved_boxes.reverse()

        crates[command[2] - 1] = moved_boxes + crates[command[2] - 1]

        return crates

    def move_all_crates(self, crates, commands, model="9000"):

        for command in commands:

            crates = self.move_crates(crates, command, model=model)
    
        return crates

    def get_top_boxes(self, crates):

        return "".join([x[0] for x in crates])
