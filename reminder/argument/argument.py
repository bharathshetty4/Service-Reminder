import argparse
import sys
from reminder.add.add import AddService
from reminder.delete.delete import DeleteService
from reminder.list.list import ListService
from reminder.invite.invite import SendInvite

class MyParser(argparse.ArgumentParser):

    def error(self, message, usage=""):
        sys.stderr.write('\nError: %s\n' % message)
        self.print_help(usage)
        sys.exit(2)

    def print_help(self, usage="", file=None):
        print('\nUsage: reminder [positional Arguments] [optional Arguments]\n\n'
              'Positional arguments:\n'
              '  add                   Add a Service\n'
              '  delete                Delete a Service\n'
              '  create                Create the Reminder\n'
              '  list                  List the Services registered\n\n'
              'Optional arguments:\n'
              '  -h, --help             show this help message and exit\n'
              '  -n NAME, --name NAME,  [Required]Name of the service, Should be unique\n'
              '  -d DATE, --date DATE,  [Required]Date of the Purchase in the format of YYYY/MM/DD\n'
              '  -i INTERVAL, --interval INTERVAL,  [Required]Interval of the reminder, Supported Usage [30,130,365], 6m, 1y\n'
              '  -e END_DATE, --enddate END_DATE,  End Date of the reminder in the format of YYYY/MM/DD,'
              ' Default is 2 years\n'
              '  -t TIME, --time TIME,   Time of the reminder for calendar, Default is 1000\n'
              '  -b BEFORE, --before BEFORE,  Remind n days before the due, Default is 3 day before, Supported Usage 5d, 1w, [6m]\n'
              )
        usage_show = "Example Usage: " + usage
        print(usage_show+"\n")

    def parse_arguments(self):
        parser = MyParser()

        parser.add_argument('pos_arg', nargs='*', help="takes positional argument")


        # Arguments needed by the create
        parser.add_argument('-n', '--name', type=str,
                            help="name of the service, Should be unique') #also needed by delete")
        parser.add_argument('-d', '--date', type=str, help="Date of the Purchase in the format of YYYY/MM/DD")
        parser.add_argument('-i', '--interval', type=str,
                            help="Interval of the reminder, Supported Usage [30,130,365], [6m], [1y]")
        parser.add_argument('-e', '--enddate', type=str, help="End Date of the reminder in the format of YYYY/MM/DD")
        parser.add_argument('-t', '--time', type=str, help="Time of the reminder for calendar, Default is 1000")
        parser.add_argument('-b', '--before', type=str,
                            help="Remind n days before the due, Default is 3 day before, Supported Usage [5d],[1w],[6m]")

        # TODO: Timezone Support

        args = parser.parse_args()

        if 'add' in args.pos_arg:

            if not args.name or not args.date or not args.interval:
                error_message = "Expected one or more arguments"
                usage = "'reminder add --name Bike --date 01/07/2015 --interval 15,30,45 --enddate 01/07/2017 --time 1900 --before 1w'"
                # TODO: time in AM/PM format
                self.error(error_message, usage)

            # Create a Dict
            service = {}
            service["name"] = args.name
            service["date"] = args.date
            service["interval"] = args.interval
            service["enddate"] = args.enddate
            service["time"] = args.time
            service["before"] = args.before

            AddService().add_service(service)

            sys.exit(2)

        if 'delete' in args.pos_arg:

            if not args.name:
                error_message = "Expected one or more arguments"
                usage = "'reminder delete --name Bike'"
                self.error(error_message, usage)

            # Create a Dict
            service = {}
            service["name"] = args.name

            DeleteService().delete_service(service)

            sys.exit(2)

        if 'create' in args.pos_arg:

            SendInvite().send_invite()

            sys.exit(2)

        if 'list' in args.pos_arg:

            ListService().list_service()

            sys.exit(2)
