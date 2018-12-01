class Printer:

    def __init__(self, regex):
        self.regex = regex

    def print(self, line, file_name='no_file', line_num=1):
        print(f'{line}:{file_name}:{line_num}')
