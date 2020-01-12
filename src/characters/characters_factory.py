from .ghost import *
from .cherry import *
from .pacman import *


def new_ghost(name):
    class_name = f"Ghost{name}"
    if class_name not in globals():
        raise Exception(f"There is no ghost class : {class_name}")
    return globals()[f"Ghost{name}"]()
    