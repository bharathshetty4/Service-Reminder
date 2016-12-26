import argparse
import sys

class MyParser(argparse.ArgumentParser):

    def print_help(self, file=None):
        print ("here iam")

    def parse_arguments(self):
        parser=MyParser()

        parser.add_argument('add', help='Add a Service')
        parser.add_argument('delete', help='Delete a Service')
        parser.add_argument('create', help='Create the Remider')
        parser.add_argument('show', help='Show the Services registered')
        parser.add_argument('help', help='Help Note')

        #Arguments needed by the create
        parser.add_argument('-n', '--name', help='name of the service, Should be unique') #also needed by delete
        parser.add_argument('-d', '--date', help='Date of the Purchase in the format of DD/MM/YYYY')


        args = parser.parse_args()

        if(args.add):
            print("add called")

        if(args.delete):
            print("delete called")

        if(args.create):
            print("create called")

        if(args.show):
            print("show called")

        collected_inputs = {'name': args.n}
        print(collected_inputs)
