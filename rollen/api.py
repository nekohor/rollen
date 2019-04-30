from .engineer import Rollen


def roll(line=None):
    rln = Rollen()
    if line:
        rln = rln.set_line(line)
    else:
        pass
    return rln


def tool():
    rln = Rollen()
    return rln
