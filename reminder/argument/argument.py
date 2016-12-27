import argparse
import sys

class MyParser(argparse.ArgumentParser):

    def error(self, message, usage=""):
        sys.stderr.write('error: %s\n' % message)
        self.print_help(usage)
        sys.exit(2)

    def print_help(self, usage, file=None):
        print ('\nusage: reminder [positional Arguments] [optional Arguments]\n\n'\
                'positional arguments:\n'\
                '  add                   Add a Service\n'\
                '  delete                Delete a Service\n'\
                '  create                Create the Remider\n'\
                '  show                  Show the Services registered\n\n'\
                'optional arguments:\n'\
                '  -h, --help            show this help message and exit\n'\
                '  -n NAME, --name NAME  name of the service, Should be unique\n'\
                '  -d DATE, --date DATE  Date of the Purchase in the format of DD/MM/YYYY\n')
        usage = "Example Usage: " + usage
        print (usage)


    def parse_arguments(self):
        parser=MyParser()

        parser.add_argument('add', nargs='*', help='Add a Service')
        parser.add_argument('delete', nargs='*', help='Delete a Service')
        parser.add_argument('create', nargs='?', help='Create the Reminder')
        parser.add_argument('show', nargs='?', help='Show the Services registered')

        #Arguments needed by the create
        parser.add_argument('-n', '--name', help='name of the service, Should be unique') #also needed by delete
        parser.add_argument('-d', '--date', type=str, help='Date of the Purchase in the format of DD/MM/YYYY')

        args = parser.parse_args()

        if(args.add):
            print("add called")

            if(not args.name or not args.date):
                error_message = "Expected one or more arguments"
                usage = "'reminder add --name Bike --date 01/07/2015'"
                self.error(error_message,usage)

            sys.exit(2)

        if(args.delete):
            print("delete called")

            if(not args.name):
                error_message = "Expected one or more arguments"
                usage = "'reminder add --name Bike'"
                self.error(error_message,usage)

            sys.exit(2)

        if(args.create):
            print("create called")


            sys.exit(2)

        if(args.show):
            print("show called")


            sys.exit(2)


