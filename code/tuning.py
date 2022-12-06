class CommunicationSystem:

    def _read_input(self, input_path):

        with open(input_path) as file:
            datastream = file.read()

        return self._format_inputs(datastream)

    def _format_inputs(self, datastream):

        return datastream

    def find_first_distinct_pattern(self, datastream, pattern_len=4):

        for i in range(len(datastream) - pattern_len):
            packet = datastream[i: i + pattern_len]

            if len(set(packet)) == pattern_len:

                return i + pattern_len
        
        pass
