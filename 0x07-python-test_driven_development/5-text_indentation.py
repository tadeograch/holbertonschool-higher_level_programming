#!/usr/bin/python3

"""
5. Text indentation
A function that prints a text with 2 new lines
after each of these characters: ., ? and :
tex_indentation(text)
"""


def text_indentation(text):
    """
    Function that indent the text
    """

    if not type(text) is str:
        raise TypeError("text must be a string")
    c = 0
    while c < len(text):
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            print("{}\n".format(text[c]))
        elif text[c - 1] == '.' or text[c - 1] == '?' or text[c - 1] == ':':
            if text[c] == " ":
                while text[c + 1] == " ":
                    c += 1
            else:
                print("{}".format(text[c]), end="")
        else:
            print("{}".format(text[c]), end="")
        c += 1
