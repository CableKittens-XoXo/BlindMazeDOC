import pygame
import asyncio
from pygame import mixer
from math import fabs
#from win32gui import SetWindowPos
from random import randint
from random import choice


class Maze:
  def __init__(self, size):
    self.gen = False
    self.maze = []
    self.maze_size = size
    for i in range(0, size * 2 + 1):
      line = []
      for i in range(0, size * 2 + 1):
        line.append(2)
      self.maze.append(line)
    for i in range(0, size * 2 + 1):
      for j in range(0, size * 2 + 1):
        if i % 2 != 0 or j % 2 != 0:
          self.maze[i][j] = 1
    for i in range(1, size * 2 + 1, 2):
      for j in range(1, size * 2 + 1, 2):
        self.maze[i][j] = int(((i - 1) / 2) * size + ((j - 1) / 2)) + 3

    # movesqa = 3+numberID, walls = 1, empt = 2
    # number id is for wall gen
    # 0 is path

  def generate(self):
    if self.gen == True:
      re = input("Already Generated, Create new? (y/n)")
      if re == "y":
        pass
      else:
        return
    self.gen = True
    done = False
    dick = {"N": (-2, 0), "E": (0, 2), "S": (2, 0), "W": (0, -2)}
    ch = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x = 0
    while done == False:
      f = (randint(1, self.maze_size) * 2 - 1,
           randint(1, self.maze_size) * 2 - 1)

      #attempt to debug code commented out
      """
      wals = 0
      for i in ch:
        if self.maze[f[0] + i[0]][f[1] + i[1]] == 1:
          wals += 1
      if wals <= 1:
        continue
      x += 1
      if x == 1000:
        self.display()
        input("STOPPED FORCEFULLY")
      """

      dirs = ["N", "E", "S", "W"]
      tdir = []
      if f[0] == 1:
        dirs[0] = "G"
      if f[1] == 1:
        dirs[3] = "G"
      if f[0] == self.maze_size * 2 - 1:
        dirs[2] = "G"
      if f[1] == self.maze_size * 2 - 1:
        dirs[1] = "G"
      for i in range(0, 4):
        if dirs[i] != "G":
          tdir.append(dirs[i])
      dirs = dick[choice(tdir)]
      e = (f[0] + dirs[0], f[1] + dirs[1])
      if self.maze[f[0]][f[1]] == self.maze[e[0]][e[1]]:
        continue
      self.maze[f[0] + (int(dirs[0] / 2))][int(f[1] + (dirs[1] / 2))] = 0

      if self.maze[f[0]][f[1]] < self.maze[e[0]][e[1]]:
        chan = self.maze[e[0]][e[1]]
        for i in range(1, self.maze_size * 2 + 1, 2):
          for j in range(1, self.maze_size * 2 + 1, 2):
            if self.maze[i][j] == chan:
              self.maze[i][j] = self.maze[f[0]][f[1]]
      else:
        chan = self.maze[f[0]][f[1]]
        for i in range(1, self.maze_size * 2 + 1, 2):
          for j in range(1, self.maze_size * 2 + 1, 2):
            if self.maze[i][j] == chan:
              self.maze[i][j] = self.maze[e[0]][e[1]]

      done = True
      for i in range(1, self.maze_size * 2 + 1, 2):
        for j in range(1, self.maze_size * 2 + 1, 2):
          if self.maze[i][j] != 3:
            done = False
            break
        if done is False:
          break
    player = randint(1,4)
    if player == 1:
      self.maze[1][1] = 5
      self.maze[self.maze_size * 2 - 1][self.maze_size * 2 - 1] = 4
    elif player == 2:
      self.maze[1][self.maze_size * 2 - 1] = 5
      self.maze[self.maze_size * 2 - 1][1] = 4
    elif player == 3:
      self.maze[self.maze_size * 2 - 1][1] = 5
      self.maze[1][self.maze_size * 2 - 1] = 4
    else:
      self.maze[self.maze_size * 2 - 1][self.maze_size * 2 - 1] = 5
      self.maze[1][1] = 4
    
  def display(self):
    disp = ""
    for i in range(0, self.maze_size * 2 + 1):
      for j in range(0, self.maze_size * 2 + 1):
        if self.maze[i][j] == 1:
          if i % 2 == 0:
            disp += "-"
          else:
            disp += "|"
        if self.maze[i][j] == 2:
          disp += "+"
        if self.maze[i][j] == 3:
          disp+= " "
        if self.maze[i][j] == 0:
          disp += " "
        if self.maze[i][j] == 5:
          disp += "P"
        if self.maze[i][j] == 4:
          disp += "E"
        if self.maze[i][j] == 6:
          disp += "S"
      disp += "\n"
    print(disp)

"""
Maze Key-
0 = Path
1 = Wall
2 = Empty/Corner
3 = Spaces
4 = End
5 = Player
6 = Start
"""

class Player:
  def __init__(self):
    for i in range(0, len(maze.maze)):
      for j in range(0, len(maze.maze[i])):
        if maze.maze[i][j] == 5:
          self.x = i
          self.y = j
          self.start = (i,j)
        if maze.maze[i][j] == 4:
          self.exitx = i
          self.exity = j
          #INEFFECIENT AF BUT VERY MINOR SO IDC
    print("WASD controls")
    print("You find yourself in a dark... well you're not quite sure.\nBut you certainly don't want to stay here, it's cold, and you're hungry.\nYou think you feel a faint draft, but maybe that's just your imagination...")
    


def move(dirp):
  dick = {"N": (-2, 0), "E": (0, 2), "S": (2, 0), "W": (0, -2)}
  mov = dick[dirp]
  if maze.maze[int(player.x + mov[0]/2)][int(player.y + mov[1]/2)] == 1:
    unb.play(bonk)
  if maze.maze[int(player.x + mov[0]/2)][int(player.y + mov[1]/2)] == 0:
    unb.play(step)
    #commit movement
    tx = player.x + mov[0]
    ty = player.y + mov[1]
    if maze.maze[tx][ty] == 4:
      pygame.quit()
      print("You made it out!, well done!")
      maze.maze[player.start[0]][player.start[1]] = 6
      maze.maze[player.x][player.y] = 3
      maze.display()
      return False
    hmm.set_volume(1-((fabs(((player.exitx-player.x))/2+fabs((player.exity-player.y))/2)))/(maze.maze_size*2))
    maze.maze[player.x][player.y] = 3
    maze.maze[tx][ty] = 5
    player.x = tx
    player.y = ty
    #movement commited
  return True

async def mainloop():
  win = True
  while win:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          win = move("N")
        if event.key == pygame.K_d:
          win = move("E")
        if event.key == pygame.K_s:
          win = move("S")
        if event.key == pygame.K_a:
          win = move("W")
    await asyncio.sleep(0)
  unb.play(end)

  
if __name__ == "__main__":
    maze = Maze(4)
    maze.generate()
    mixer.init()
    step = mixer.Sound("step.mp3")
    bonk = mixer.Sound("bonk.mp3")
    hmm = mixer.Sound("hmm.mp3")
    end = mixer.Sound("end.mp3")
    bonk.set_volume(1)
    step.set_volume(1)
    end.set_volume(1)
    pygame.mixer.set_num_channels(20)
    unb = mixer.find_channel()
    ch1 = mixer.Channel(0)
    ch2 = mixer.Channel(1)
    ch3 = mixer.Channel(2)
    ch4 = mixer.Channel(3)
    ch5 = mixer.Channel(4)
    ch6 = mixer.Channel(5)
    ch6.play(hmm, loops = -1)
    player = Player()
    pygame.init()
    screen = pygame.display.set_mode((400, 400), pygame.NOFRAME)
    pygame.display.set_caption("The darkness...")
    #SetWindowPos(pygame.display.get_wm_info()["window"], -1, 0, 0, 0, 0, 1)
    asyncio.run(mainloop())
