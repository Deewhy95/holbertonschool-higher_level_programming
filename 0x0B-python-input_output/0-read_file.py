#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        print(f.read(), end="")
