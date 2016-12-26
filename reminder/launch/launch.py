import sys

from reminder.argument.argument import MyParser

def execute():
    MyParser().parse_arguments()

if __name__ == '__main__':
    sys.exit(execute())
