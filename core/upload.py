import os


def validate_file(file):

    ext = file.name.split(".")[-1]

    return ext.lower()