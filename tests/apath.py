from pathlib import Path

def abspath(filepath):

    relativepath = Path(filepath)
    return relativepath.absolute()