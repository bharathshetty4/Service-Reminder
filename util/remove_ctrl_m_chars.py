import os
import sys
import tempfile

"""
File used to remove ^M
Usage, python remove_ctrl_m_chars.py <file_name>

"""
def main():
    filename = sys.argv[1]
    with tempfile.NamedTemporaryFile(delete=False) as fh:
        for line in open(filename):
            line = line.rstrip()
            fh.write(line + '\n')
        os.rename(filename, filename + '.bak')
        os.rename(fh.name, filename)


if __name__ == '__main__':
    main()
