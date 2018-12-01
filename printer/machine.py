import re
from .printer import Printer


class Machine(Printer):

    def print(self, line, file_name='no_file', line_num=1):
        iterators = re.finditer(self.regex, line)
        for it in iterators:
            start_pos = it.regs[0][0]
            matched_text = it[0]
            # format: file_name:no_line:start_pos:matched_text
            print(f'{file_name}:{line_num}:{start_pos}:{matched_text}')
