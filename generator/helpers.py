"""helper module provide helper functions to generator modules"""


def alias(key: str, *cmds: str) -> str:
    """alias returns the bind command for the passed in key and cmds(can be multiple commands)"""
    result = f"alias \"{key}\" \""
    for cmd in cmds:
        result += f"{cmd};"
    return result[:len(result)-1] + "\"\n"


def bind(key: str, *cmds: str) -> str:
    """bind returns the bind command for the passed in key and cmds(can be multiple commands)"""
    result = f"bind \"{key}\" \""
    for cmd in cmds:
        result += f"{cmd};"
    return result[:len(result)-1] + "\"\n"


def buy(item: str) -> str:
    """buy returns the buy command for the passed in item"""
    return f"buy {item}"

def exec_cfg(filename: str) -> str:
    """exec returns the exec command for a cfg file"""
    return f"exec {filename}.cfg"


class DotDict(dict):
    """dot.notation access to dictionary attributes"""

    def __getattr__(self, *args):
        val = super().get(*args)
        return DotDict(val) if isinstance(val, dict) else val
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
