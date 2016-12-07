import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Code to remind your vehicle service date')
    parser.add_argument('--iFile', type=str,required=False,default='influxdb_data.json',help='input file where the json file is stored')
    parser.add_argument('--oFile', type=str, required=False,default='output_file.json',help='output file name where the modified json file to be stored')
    return parser.parse_args()


def execute():
    print ("Hello from the other world")


if __name__ == '__main__':
    sys.exit(execute())
