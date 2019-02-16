import os


def fixture(filename):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 
        "..", "fixtures", filename
    )
