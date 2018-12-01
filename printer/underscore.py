import re
from .printer import Printer


class Underscore(Printer):
    def print(self, line, file_name='no_file', line_num=1):
        fixed_line = re.sub(r"[\n\t]*", "", line)
        highlight = list("".ljust(len(fixed_line)))
        iterators = re.finditer(self.regex, fixed_line)
        is_highlight = False
        for it in iterators:
            start_pos = it.regs[0][0]
            end_pos = it.regs[0][1]
            for i in range(start_pos, end_pos):
                highlight[i] = chr(136)
                is_highlight = True
        if is_highlight:
            print(f'{fixed_line}:{file_name}:{line_num}')
            print("".join(highlight))
