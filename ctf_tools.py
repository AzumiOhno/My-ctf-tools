import numpy as np


def rot_n(string: str, n: int) -> str:
    ord_list = [ord(c) for c in string]
    translated_list = []
    for c in ord_list:
        # ord('A') == 65, ord('Z') == 90
        # ord('a') == 97, ord('z') == 122
        if c >= 65 and c <= 90:
            c -= 65
            c = (c - n + 26) % 26
            c += 65
        elif c >= 97 and c <= 122:
            c -= 97
            c = (c - n + 26) % 26
            c += 97
        translated_list.append(c)
    chr_list = [chr(c) for c in translated_list]
    return "".join(chr_list)


def rot_all(string: str) -> list:
    string_list = []
    for i in range(1, 26):
        string_list.append(rot_n(string, i))
    return string_list


def print_rot_n(string: str, n: int):
    translated_string = rot_n(string, n)
    print("ROT{}: {}".format(n, translated_string))
    return


def print_rot_all(string: str):
    for i in range(1, 26):
        print_rot_n(string, i)
    return

