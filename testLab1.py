import numpy as np
import bisect
import time
from queue import PriorityQueue

start = time.time()

def checkBoardSolvable(layout):
  # https://gamedev.stackexchange.com/questions/40307/why-is-this-8-puzzle-unsolvable
  #layoutVec = np.squeeze(np.asarray(layout))
  numberOfInversions = 0
  layoutVec = np.asarray(layout).reshape(-1)
  for i in range(0,8):
    value1 = layoutVec[i]
    if(value1 != 0):
      for j in range(i,8):
        value2 = layoutVec[j]
        if(value2 != 0):
          if(value1 > value2):
            numberOfInversions += 1
  # even solvable
  if(numberOfInversions % 2 == 0):
    return True

  return False

from random import randrange
def generateRandomBoard():
  board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  for i in range(9):
    x = randrange(3)
    y = randrange(3)
    while(board[y][x] != 0):
      x = randrange(3)
      y = randrange(3)

    board[y][x] = i
  return board

def generateValidBoard():
  layout = generateRandomBoard()
  while(not checkBoardSolvable(layout)):
    layout = generateRandomBoard()

  return layout

'''
def generateH(layout, goal):
    h = 0

    # h2 - manhattan distance
    for x1 in range(3):
          for y1 in range(3):
            for x2 in range(3):
              for y2 in range(3):
                if(layout[y1][x1] == goal[y2][x2]):
                  h += abs(x1-x2) + abs(y1-y2)

    return h
'''
def generateH(layout, goal): # h1 - Missing tiles
    h = 0
    for x in range(3):
      for y in range(3):
        if(layout[y][x] != goal[y][x]):
          h += 1
    return h

import copy
def legalMoves(layout):
  possibleLayouts = []
  x0 = -1
  y0 = -1
  '''
  ex
  -- 0 1 2 --> x
  0  7 1 4
  1  3 0 8
  2  2 6 5
  |
  v
  y
  '''

  for x in range(3):
    for y in range(3):
      if(layout[y][x] == 0):
        x0 = x
        y0 = y

  # check move left (move -x)
  if(x0 > 0):
    tempLayout = [row[:] for row in layout]
    swapValue = tempLayout[y0][x0-1]
    tempLayout[y0][x0-1] = 0
    tempLayout[y0][x0] = swapValue
    possibleLayouts.append(tempLayout)

  # check move right (move +x)
  if(x0 < 2):
    tempLayout = [row[:] for row in layout]
    swapValue = tempLayout[y0][x0+1]
    tempLayout[y0][x0+1] = 0
    tempLayout[y0][x0] = swapValue
    possibleLayouts.append(tempLayout)

  # check move up (move -y)
  if(y0 > 0):
    tempLayout = [row[:] for row in layout]
    swapValue = tempLayout[y0-1][x0]
    tempLayout[y0-1][x0] = 0
    tempLayout[y0][x0] = swapValue
    possibleLayouts.append(tempLayout)

  # check move down (move +y)
  if(y0 < 2):
    tempLayout = [row[:] for row in layout]
    swapValue = tempLayout[y0+1][x0]
    tempLayout[y0+1][x0] = 0
    tempLayout[y0][x0] = swapValue
    possibleLayouts.append(tempLayout)
  return possibleLayouts

class puzzleBoard:
  layout = []
  goal = []
  depth = 0
  h = 0
  f = 0

  def __init__(self, startLayout, goal, depth, parent):
    self.layout = startLayout
    self.goal = goal
    self.depth = depth
    self.h = generateH(self.layout, self.goal)
    self.f = self.depth + self.h

    self.parent = parent

  def getLayout(self):
    return self.layout

  def getGoal(self):
    return self.goal

  def getDepth(self):
    return self.depth

  def geth(self):
    return self.h

  def getf(self):
    return self.f

  def __lt__ (self, other):
      return self.f < other.f

  def getParents(self):
    path =[]
    current = self
    while current:
      path.append(current.layout)
      current = current.parent
    path.reverse()
    return path

  #def seth(self):
  #  self.h = generateH(self.layout, self.goal)

  def genChildren(self, closedList):
    possibleLayouts = legalMoves(copy.deepcopy(self.layout))
    children = []
    for layout in possibleLayouts:
        if tuple(map(tuple, layout)) not in closedList:
            tempChild = puzzleBoard(layout, self.goal, self.depth + 1, self)  # Set self as the parent
            children.append(tempChild)
    return children
  
  #startLayout = generateValidBoard()
#startLayout = [[1, 3, 2], [4, 6, 5], [7, 0, 8]]
#startLayout = [[6, 5, 8], [7, 1, 3], [4, 2, 0]] # Hard-board
startLayout = [[8,6,7],[2,5,4],[3,0,1]] #hardest board

goalLayout = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
currentPuzzle = puzzleBoard(startLayout, goalLayout, 0, [])
closedList = set()
openedList = PriorityQueue()  # openedList = [currentPuzzle]
openedList.put(currentPuzzle)
# goal reached when h == 0
print(currentPuzzle.getLayout())  # print(openedList[0].getLayout())

while currentPuzzle.geth() != 0:
    currentPuzzle = openedList.get()  # Get the node with the lowest f value
    currentLayoutHash = tuple(map(tuple, currentPuzzle.getLayout()))

    if currentLayoutHash in closedList:
        continue

    closedList.add(currentLayoutHash)
    children = currentPuzzle.genChildren(closedList)

    for childPuzzle in children:
        openedList.put(childPuzzle)

# Print the path to the solution
path = currentPuzzle.getParents()
print("Path to solution:")
for step in path:
    for row in step:
        print(row)
    print()  # Blank line between steps

end = time.time()
print(f"Time taken: {end - start} seconds")