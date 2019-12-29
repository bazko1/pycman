class Game:
  def __init__(self):
    m = Map.fromArray([[]])
    characters = [Ghost('blue'), Ghost('Red'), Pacman()]
    
    
    
    # m.setMap([[]]) # create wall object from 0,1 array in size of map
    # 1 - means wall 
    # 0 - walkable space with food - can be normal - can be extra one 
    
    m.setCharacters(characters)
    
    for c in characters:
      c.setChars(characters)
      c.setMap(m)
    
    points = 0 
    graphics = Graphics(m)
    
    
  def step():
    for c in charcters:
      c.step()
      if c == Pacman():
        self.calculateScore(c.getEaten())
        
  
		graphics.update()
      

class Graphics:
  def __init__(self, m):
    self.map = m
    self.imagePaths = {
      'pacmanOpen' : 'c:/pacman.img'
      'pacmanClosed' : 'c:/pacman.img'
      'wall' :
      'food' :
      'superFood' :
      'ghost':
      
      
      
    }
  
  def update():
    for row in self.map:
      for el in row:
        self.draw(el)
      
      
  def draw(self, el):
    if el == pacman:
      curr = el.state
      curr == 0:
        render('pacmanOpen')
      
      else:
        render('pacmanClosed')
    
    
    
    
#named as board
class Map:
  def __init__(self, n):
    	self.arr = [[]] * n
  
class Pacman(Movable):
  def __init__(self):
  	self.eatenFood = 0
    self.eatenGhost = 0
    self.eatenCherry = 0
    m = Map()
    
  def step():
    directionX, directionY = getDirection() # get key return 1, -1
    
    newX = self.x + 1
    
    newField = m[self.y][newX]
    
    if isinstance(Food)
    	if newField.isSuper:
    
    
    self.x += 1
  
class GhostBlue(Movable):
  pass
class GhostRed(Movable):
  pass
class GhostYellow(Movable):
  pass
class GhostPink(Movable):
  pass
class Food():
  
  pass

class SuperFood():
  pass

class Cherry(Movable):
  pass

class Wall():
  pass

  class Movable:
    def __init__(self, chars, map):
    	self.x = 0
      self.y = 0
      self.characters = []
      self.map = [[]]
      
    
    def step(self, Map):
    	#pacman 
      if food:
        pass
      elif superFood:
        pass
      
      return prevX, prevY, newX, newY
  