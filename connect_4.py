# 4 in a row game
# https://en.wikipedia.org/wiki/Connect_Four

'''
Game
  board: a 2D array of cells
  check_winner(): check who won the game every input from player1 or player2
  game_over(): terminates a game
  place_checker(x, y, player): takes an input and update a cell
  print_board()

Cell
  is_empty: empty or not empty
  owner: player1 or player2 (1, 2)
  x, y coordinates
  render(): displays O for player1 and X for player2

Player
  name
  number: player1 or player2?
'''

import sys

class Cell():

  def __init__(self, is_empty=True, owner=0, x=-1, y=-1):
    self.is_empty = is_empty
    self.owner = owner
    self.x, self.y = x,y
  
  def render(self):
    owner = self.owner
    if not self.is_empty and owner != 0:
      # is player 1?
      return 'O' if owner == 1 else 'X'
    return '-'
  


class Game():
  board = [] # 6 by 7 matrix

  def __init__(self, width=7, height=6):
    
    self.width, self.height = width, height
    
    # initialize board
    self.board = [[Cell() for j in range(width)] for i in range(height)]
  
  def place_checker(self, x, y, player):
    # get the cell
    x,y = int(x),int(y)
    
    if self.in_bound(x,y):
      # are there any other checkers below y axis?
      x,y = self.get_checker_pos(x,y)
      checker = self.board[y][x]
      
      if not checker.is_empty: return False
      checker.is_empty = False
      checker.owner = player
      if self.check_winner(x,y):
        print('game over', 'Player1' if player == 1 else 'Player2', 'has won!')
        sys.exit()
      return True

    # is it already taken?
    return False

  def get_checker_pos(self, x, y):
    # lower the y axis until there is not checker below
    while y < self.height-1:
      if not self.board[y+1][x].is_empty:
        break
      y += 1
    return (x,y)

  def in_bound(self, x, y): return x < self.width and x >=0 and y < self.height and y >= 0
  
  def is_checker_valid(self, x, y, player): return self.in_bound(x, y) and not self.board[y][x].is_empty and self.board[y][x].owner == player

  def check_winner(self, x, y):
    board = self.board
    checker = board[y][x]
    player = checker.owner
    total = 0
    temp = 0
    
    return self.check_winner_helper(x, y, player)
   
  def check_winner_helper(self, x, y, player):
    
    i,j = 1,1
    count = 1
    # check horizontal
    while self.is_checker_valid(x+i, y, player) or self.is_checker_valid(x-j, y, player):
      if self.is_checker_valid(x+i, y, player): count += 1; i += 1
      if self.is_checker_valid(x-j, y, player): count += 1; j += 1
    
    if count == 4: return True
    else: count = 1; i,j = 1,1

    # check vertical
    while self.is_checker_valid(x, y+i, player) or self.is_checker_valid(x, y-j, player):
      if self.is_checker_valid(x, y+i, player): count += 1; i += 1
      if self.is_checker_valid(x, y-j, player): count += 1; j += 1

    if count == 4: return True
    else: count = 1; i,j = 1,1

    # check left diagonal
    while self.is_checker_valid(x+i, y+i, player) or self.is_checker_valid(x-j, y-j, player):
      if self.is_checker_valid(x+i, y+i, player): count += 1; i += 1
      if self.is_checker_valid(x-j, y-j, player): count += 1; j += 1
    
    if count == 4: return True
    else: count = 1; i,j = 1,1

    # check right diagonal
    while self.is_checker_valid(x-i, y+i, player) or self.is_checker_valid(x+j, y-j, player):
      if self.is_checker_valid(x-i, y+i, player): count += 1; i += 1
      if self.is_checker_valid(x+j, y-j, player): count += 1; j += 1
    
    if count == 4: return True
    else: count = 1; i,j = 1,1

    return False


    
  def print_board(self):

    for i in range(self.height):
      s = ''
      for j in range(self.width):
        s += self.board[i][j].render()
      print(s)

if __name__ == '__main__':
  print('Welcome to Connect 4 game!')
  connect_4 = Game()
  connect_4.print_board()
  
  turns = 1 # odd turns = player 1 else player2
  while True:
    player = 1
    x,y = 0,0
    # is it player2's turn?
    if turns % 2 == 0: 
      player = 2
      print("player2's turn:")
    else: 
      print("player1's turn:")

    x,y = input('x: '),input('y: ')
    
    # only increments the turn if player places a checker correctly
    if connect_4.place_checker(x,y,player):
      turns += 1
    else: print('please find an unoccupied slot!')
    connect_4.print_board()


  

