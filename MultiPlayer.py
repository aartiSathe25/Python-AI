def User1Turn(board):
  pos = input("Enter X's Position:")
  pos = int(pos)
  #Not Empty
  if(board[pos-1]!=0):
    print("Wrong Move......!!!!")
    exit(0)
  board[pos-1]=1

def User2Turn(board):
  pos = input("Enter 0's Position:")
  pos = int(pos)
  #Not Empty
  if(board[pos-1]!=0):
    print("Wrong Move......!!!!")
    exit(0)
  board[pos-1]=-1

def ConstBoard(board):
  print("Current State of the board:\n")
  for i in range(0,9):
    if((i>0) and (i%3==0)):
      print("\n")
    if(board[i]==0):
      print("_ ",end=" ")
    if(board[i]==1):
      print("X ",end=" ")
    if(board[i]==-1):
      print("O ",end=" ")
  print("\n\n")



def analyzeboard(board):
  #who has won or not
  cb = [[0,1,2],[3,4,5],[0,3,6],[1,4,7],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] ]

  for i in range(0,8):
    #check who won and return
      if((board[cb[i][0]]!=0) and (board[cb[i][0]]==board[cb[i][1]]) and  (board[cb[i][1]]==board[cb[i][2]])):
          return board[cb[i][0]]


  return 0

def CompTurn(board):
    pos = -1
    value = -2    
    for i in range(0,9):
    #pos empty then put X =1 
        if(board[i]==0):
            board[i]=1
            score = 10
            board[i]=0
            if(score>value):
                value = score
                pos=i
        

def main():
    choice = input("Enter 1 for single Player or 2 for Multi-Player")
    choice = int(choice)
    board = [0,0,0,0,0,0,0,0]
    if(choice==1):
      #code to play agst AI
        print("Computer: X Vs. You:O")
        player = input("Enter to play 1st or 2nd")
        player = int(player)
        #not known
        for i in range(0,9):
            #somebody won pause game over
            if(analyzeboard(board)!=0):
            break
#p=0 2 4 p1

            if((i+player)%2==0):
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)
            
    else:
    #code for Multiplayer
        for i in range(0,9):
            if(analyzeboard(board)!=0):
                break
            if(i%2==0):
                ConstBoard(board)
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)


    x= analyzeboard(board)

    if(x==0):
        ConstBoard(board)
        print("Draw!!!!")
    if(x==-1):
        ConstBoard(board)
        print("Player O has Won")
    if(x==1):
        ConstBoard(board)
        print("Player 1 has Won")



main()
