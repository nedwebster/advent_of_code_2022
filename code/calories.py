class CalorieReader():

    def __init__(self):

        pass

    def read_input(self, input_path):
        
        with open(input_path) as file:
            calories = file.read()
        
        calories = self._format_calories(calories)

        return calories

    def _format_calories(self, calories):

        calories = calories.split("\n\n")
        calories = [x.split("\n") for x in calories]

        def convert_to_int(str_list):
            return [int(x) for x in str_list]
        
        calories = [convert_to_int(x) for x in calories]

        return calories

    def find_max_calories(self, formatted_calories, position=0):

        summed_calories = [sum(x) for x in formatted_calories]
        summed_calories.sort(reverse=True)

        return summed_calories[position]
