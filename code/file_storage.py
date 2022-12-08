import numpy as np


class FileStorage():

    def __init__(self):

        self.fs = {"/": {}}
        self.wd = ['/']
        self.concat_path = "['/']"
        self.doing_ls = False

    def _read_input(self, input_path):

        with open(input_path) as file:
            commands = file.read()

        return self._format_commands(commands)

    def _update_concat_path(self):

        self.concat_path = "".join(["['" + x + "']" for x in self.wd])

    def _format_commands(self, commands):

        commands = commands.split("\n")
        commands = [x.split(" ") for x in commands]
        return commands

    def is_ls(self, command):

        try:
            return command[1] == "ls"
        except:
            return False

    def cd_command(self, command):

        if command[2] == "..":
            self.wd = self.wd[:-1]
            self._update_concat_path()
        else:
            if command[2] not in eval("self.fs" + self.concat_path).keys():
                self.fs[self.wd[-1]] = {}
            self.wd.append(command[2])
            self._update_concat_path()

    def make_command(self, command):

        if command[0] == "dir":
            eval("self.fs" + self.concat_path)[command[1]] = {}
        else:
            eval("self.fs" + self.concat_path)[command[1]] = int(command[0])

    def do_command(self, command):

        # update ls flag if command is an ls command
        if self.is_ls(command):
            self.doing_ls = True
            return

        # if actively in an ls block
        if self.doing_ls:
            # check if ls block has ended
            if command[0] == "$":
                self.doing_ls = False
            # do make command if still in ls block
            else:
                self.make_command(command)
        
        if command[1] == "cd":
            self.cd_command(command)
            return

    def build_file_structure(self, commands):

        for command in commands:
            self.do_command(command)


def recursive_dir_sum(fs):
    test_dict = {}
    dir_sum = 0
    for k, v in fs.items():
        if isinstance(v, dict):
            v, new_dict = recursive_dir_sum(fs[k])
            test_dict[k] = v
        dir_sum += v
    return dir_sum, test_dict

def recursive_recursive_dir_sum(fs):
    d1 = [recursive_dir_sum(fs)[1]]
    for key in d1[-1].keys():
        new_dict = fs[key]
        d1 = d1 + recursive_recursive_dir_sum(new_dict)
    return d1
