#!env python

import hashlib
import sys
import argparse
from argparse import RawTextHelpFormatter
import os.path


def get_file_hash_value(file):
    hasher = hashlib.md5()

    with open(file, 'rb') as mod_file:
        buf = mod_file.read()
        hasher.update(buf)
    return hasher.hexdigest()


def save_hash_value(hash_value, hash_file):
    hash_file = open(hash_file, 'w')
    hash_file.write(hash_value)
    hash_file.close()


def has_expected_hash_value(file, hash_value):
    file_hash_value = get_file_hash_value(file)
    return hash_value == file_hash_value


def read_hash_value(hash_file):
    with open(hash_file, 'rb') as hash_value_file:
        hash_value = hash_value_file.readlines()[0].decode('utf-8')
    return hash_value


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Check hash of file', formatter_class=RawTextHelpFormatter)

    parser.add_argument('-f', '--file', help='File name for file to be checked (default: testfile.txt)', default='testfile.txt', required=False)
    parser.add_argument('-hf', '--hashfile', help='File name for file with hash value (default: hash_value_file.txt)', default='hash_value_file.txt', required=False)

    args = parser.parse_args()

    try:
        if not os.path.isfile(args.file):
            print("source file does not exist.")
            sys.exit(1)

        if not os.path.isfile(args.hashfile):
            hash_value = get_file_hash_value(args.file)
            save_hash_value(hash_value, args.hashfile)

        expected_hash_value = read_hash_value(args.hashfile)
        if (has_expected_hash_value(args.file, expected_hash_value)):
            sys.exit(0)
        else:
            sys.exit(2)

    except IOError:
        sys.exit(1)
