import gzip
import io


def open_file(filename, mode="r", encoding=None):
    if isinstance(filename, io.TextIOWrapper):
        return filename

    if filename.endswith(".gz"):
        if mode == "r":
            f = gzip.open(filename, "rt", encoding=encoding)
        elif mode == "w":
            f = gzip.open(filename, "wt", encoding=encoding)
        else:
            raise ValueError("Unknown mode for .gz: " + mode)
    elif filename.endswith(".pickle"):
        if mode == "r":
            f = open(filename, "rb")
        elif mode == "w":
            f = open(filename, "wb")
        else:
            raise ValueError("Unknown mode for .pickle: " + mode)
    else:
        f = open(filename, mode)
    return f
