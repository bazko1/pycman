from src.characters.ghost import *
from src.characters.pacman import Pacman




class Game:
  def __init__(self):
    characters = [GhostBlue, GhostRed, Pacman()]

    # m.setMap([[]]) # create wall object from 0,1 array in size of map
    # 1 - means wall 
    # 0 - walkable space with food - can be normal - can be extra one 

    
    
