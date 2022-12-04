class CampCleanup():

    def __init__(self):

        pass

    def _read_input(self, input_path):

        with open(input_path) as file:
            tasks = file.read()

        return self._format_input(tasks)

    def _format_input(self, tasks):

        tasks = tasks.split("\n")
        tasks = [x.split(",") for x in tasks]

        return self._extract_range_recursive(tasks)

    def _extract_range_recursive(self, tasks):

        if isinstance(tasks, list):
            return [self._extract_range_recursive(x) for x in tasks]
        else:
            tasks = tasks.split("-")
            tasks = [
                x for x in range(
                    int(tasks[0]),
                    int(tasks[1]) + 1
                )
            ]

            return tasks

    def get_full_overlap(self, task_pair):

        overlap_1 = [x for x in task_pair[0] if x not in task_pair[1]]
        overlap_2 = [x for x in task_pair[1] if x not in task_pair[0]]

        if len(overlap_1) == 0 or len(overlap_2) == 0:
            return 1
        else:
            return 0

    def get_partial_overlap(self, task_pair):

        return any([x for x in task_pair[0] if x in task_pair[1]])

    def get_number_of_full_overlaps(self, tasks):

        overlapped_tasks = [self.get_full_overlap(x) for x in tasks]

        return sum(overlapped_tasks)

    def get_number_of_partial_overlaps(self, tasks):

        overlapped_tasks = [self.get_partial_overlap(x) for x in tasks]

        return sum(overlapped_tasks)
