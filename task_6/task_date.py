from sys import argv
from hw_module import date_check

if __name__ == '__main__':

    print(date_check.final_check_year("".join(argv[1:])))

