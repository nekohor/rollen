from .engineer import Engineer


def roll(line=None):
    rln = Engineer()
    if line:
        rln = rln.set_line(line)
    else:
        pass
    return rln


def tool():
    rln = Engineer()
    return rln
