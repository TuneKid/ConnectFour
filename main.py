N_COLS = 7
N_ROWS = 6

def init():
  board = [["."]*N_COLS for i in range(N_ROWS)]
  return board

def print_board(board):
  print("1 2 3 4 5 6 7")
  print("_"*13)
  for row in board:
    print("|".join(row))


def get_move(board, player):
  col = int(input("Player {} enter a column:".format(player)))
  

  if not is_valid_col(col):
    print("Invalid Input! Please enter input between 1 and {}".format(N_COLS))
    col = get_move(board, player)

  col -= 1
  return col
  ''''
  for r in range(len(board) - 1, -1, -1):
    if (not placed) and board[r][col] == '.':
      board[r][col] = player
      placed = True
      '''
def make_move(board, player, col):
  r = len(board)-1
  placed = False
  while not placed and r >= 0:
    if board[r][col] == '.':
      board[r][col]=player
      placed = True
    print(placed)
    r -= 1
  if not placed:
      print("Invalid Input! This column is full!")
      col = get_move(board, player)
  return board

def is_valid_col(col):
  return col > 0 and col <= N_COLS

def has_won(board, player):
  return checkRow(board, player) or checkCol(board,player) or checkLeftDiag(board,player) or checkRightDiag(board,player)

def checkRow(board,player):
  numConsecutiveRow = 0
  rRow = 0
  #loop through rows
  #Start at the beginning of each row, and set a counter for each character to the right
  won = False
  while rRow < N_ROWS and not won:
    
    cRow= 0
    numConsecutiveRow = 0
    while cRow < N_COLS and not won: 
      if board[rRow][cRow] == player:
        numConsecutiveRow += 1
        print("Detected player: {} at r: {} c: {} n: {}".format(player, rRow, cRow, numConsecutiveRow))
        print("__")
      else:
        numConsecutiveRow = 0
      won = numConsecutiveRow >= 4
      if won:
        print("HooOooOoOOoOOoOoOOoOooOOoorRrRRRRrrrrRrrrRrRrrrrRrrrAAyAYAYYYyyyYYYyYYyYY")
      cRow += 1
    rRow += 1
  return won

def checkCol(board, player):
  '''
  numConsecutiveCol = 0
  rCol = 0
  #loop through rows
  #Start at the beginning of each row, and set a counter for each character to the right
  wonCol = False
  while rCol < N_COLS and not wonCol:
    
    cCol= 0
    numConsecurive = 0
    while cCol < N_ROWS and not wonCol: 
      if board[cCol][rCol] == player:
        numConsecurive += 1
        print("_________________________________________")
        print("Detected player: {} at r: {} c: {} n: {}".format(player, rCol, cCol, numConsecutiveCol))
      else:
        numConsecutiveCol = 0
      wonCol = numConsecutiveCol >= 4
      if wonCol:
        print("HooOooOoOOoOOoOoOOoOooOOoorAAyAYAYYYyyyYYYyYYyYY")
      cCol += 1
    rCol += 1
  return wonCol
  '''
  return False
def checkLeftDiag(board,player):
  return False
def checkRightDiag(board, player):
  return False
def main():
  
  player = 'x'
  board = init()
  print_board(board)
  num_turns = 1

  game_over = False
  while not game_over and num_turns <= N_ROWS * N_COLS:
    col = get_move(board, player)
    board = make_move(board, player, col)
    game_over = has_won(board, player)
    player = "o" if player == "x" else "x"
    num_turns += 1


    print_board(board)
  if not game_over:
    print("Tie Game")
  else:
    print("Player {} wins!".format("o" if player == "x" else "x"))
main()

