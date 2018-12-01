import sys
from printer import *
from validator import *

options_tag = 'options'
regex_tag = 'regex'
files_tag = 'files'


def main(argv):
    arguments = fetch_arguments(argv)
    if not is_valid_arguments(arguments):
        print('not valid arguments. please follow the instructions:')
        print('main.py [-u/-c/-m] [-FILE_NAME1, ...] REGEX')
        print('example: main.py -c (?:lvasyuk) -test_files/file1 -test_files/file2')
        return

    printer = init_printer(arguments[options_tag][0], arguments[regex_tag][0])

    if len(arguments[files_tag]) == 0:
        standard_input(printer)
    else:
        files_input(arguments[files_tag], printer)


def is_valid_arguments(arguments):
    if ArgumentsValidator.is_valid_options(arguments[options_tag]):
        if ArgumentsValidator.is_valid_regex(arguments[regex_tag]):
            if ArgumentsValidator.is_valid_files(arguments[files_tag]):
                return True
    return False


def init_printer(option, regex):
    return Underscore(regex) if option == '-u' else Color(regex) if option == '-c' else Machine(regex)


def fetch_arguments(args):
    arguments = {
        options_tag: [],
        regex_tag: [],
        files_tag: []
    }
    for arg in args:
        if arg.startswith('-'):
            if arg == '-u':
                arguments[options_tag].append(arg)
            elif arg == '-c':
                arguments[options_tag].append(arg)
            elif arg == '-m':
                arguments[options_tag].append(arg)
            else:
                arguments[files_tag].append(arg[1:])
        else:
            arguments[regex_tag].append(arg)
    return arguments


def standard_input(printer):
    print('Insert text and press Enter (Quit press exit and Enter)')
    for line in sys.stdin:
        if line == 'exit\n':
            return
        printer.print(line)


def files_input(files_path, printer):
    for file_path in files_path:
        file = open(file_path, 'r')
        with file as f:
            for cnt, line in enumerate(f):
                printer.print(line=line, file_name=file_path, line_num=cnt + 1)
        file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
