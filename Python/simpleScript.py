#!/usr/bin/python3
#
#   Basic shell for a python script with arguments
#
#   Copyright 2020 Graydon Smith


import argparse

def main():
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("arg", help = "Arg description", action = "store")
    args = parser.parse_args()

# end main

if __name__ == "__main__":
    main()
