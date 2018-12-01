import re
import os.path


class ArgumentsValidator:

    @staticmethod
    def is_valid_options(options):
        if len(options) < 2:
            return True
        print('FAIL: only one options can present')
        return False

    @staticmethod
    def is_valid_regex(regex):
        if len(regex) != 1:
            print('FAIL: only one regex can present')
            return False
        try:
            re.compile(regex[0])
        except re.error:
            print('FAIL: invalid regex')
            return False
        return True

    @staticmethod
    def is_valid_files(files):
        for file in files:
            if not os.path.isfile(file):
                print(f'FAIL: file path:"{file}" not exists')
                return False
        return True
