import re
from .printer import Printer


class Color(Printer):

    def print(self, line, file_name='no_file', line_num=1):
        fixed_line = re.sub(r"[\n\t]*", "", line)
        highlight = list(fixed_line)
        iterators = re.finditer(self.regex, fixed_line)
        in_l = 0;
        for it in iterators:
            start_pos = it.regs[0][0]
            end_pos = it.regs[0][1]
            highlight.insert(start_pos + in_l, "\033[1;34;9m")
            highlight.insert(end_pos + 1 + in_l, "\033[m")
            in_l += 2
        if in_l > 0:
            print(f'{"".join(highlight)}:{file_name}:{line_num}')
