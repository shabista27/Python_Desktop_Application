from tkinter import *

#from tkMessageBox import *

#board
#0 1 2
#3 4 5
#6 7 8

turn='X' #first turn

computer="O"
user="X"

#possible winning combinations
wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

board=[" "]*9 #initialize board to all blanks

Labels={}

def addLabel(frame,text,x,y): #creates the labels for X and 0
    label = Label(frame,text=text,font=("Arial",32),borderwidth=4,relief="sunken",width=2)
    label.grid(row = y,column = x,padx = 10,pady = 10)
    label.bind("<Button-1>", lambda event:choose_space(label,x,y)) #adds label when space is clicked
    Labels[x+3*y]=label #converts to coordinates of board as shown on top


def winner(new_board):# see if new board equals any winning combination
    i=0
    while i<len(wins):
        win=wins[i]
        if(new_board[win[0]]==new_board[win[1]] and new_board[win[1]]==new_board[win[2]] and new_board[win[0]]!=" "):
               return new_board[win[0]]
               i+=1
               return ""

def open_spaces(board):#creates list of all open spaces on board for reference
    ret=[]
    for i in range(0,len(board)):
            if board[i]==" ":
                ret.append(i)
                return ret

def change(player):
    if player=="X":
            return "O"
    else:
        return "X"

def minimax(board,player):
    if winner(board)==computer:
        return {"value":1,"position":-1}
    if winner(board)==user:
        return {"value":-1,"position":-1} #CHECK THIS LINE TO CHANGE ALGORITHM
    spaces=open_spaces(board)
    if len(spaces)<1:
        return {"value":0,"position":-1} #tie
    scores=[]
    for i in range(0,len(spaces)):
        next_move=spaces[i]
        board[next_move]=player
        score=minimax(board,change(player))
        scores.append({"value":score["value"],"position":next_move})
        board[next_move]=" "
        if player==computer:
            f=max
        else:
                f=min
                best_move=f(scores, key=lambda x:x["value"])
                return best_move
            



def next_turn(): #switches to next turn after each click on a space
    global turn #works with global variable
    if turn=='O':
        turn='X'
    else:
        turn='O'

def choose_space(label,x,y):
    if label['text']=="" and winner(board)=="":
        label['text']=turn
        board[x+3*y]=turn
        if winner(board)!="":
            showinfo("Winner","Player "+winner(board)+" has won")
            next_turn()
        if turn==computer:
            best_move=minimax(board,computer)
            position=best_move["position"]
        if board[position]==" ": #if there is not a tie and game is not over
            choose_space(Labels[position],position%3,position/3)


def addLabel(frame,text,x,y): #creates the labels for X and 0
    label = Label(frame,text=text,font=("Arial",32),borderwidth=4,relief="sunken",width=2)
    label.grid(row = y,column = x,padx = 10,pady = 10)
    label.bind("<Button-1>", lambda event:choose_space(label,x,y)) #adds label when space is clicked
    Labels[x+3*y]=label #converts to coordinates of board as shown on top
  

window=Tk()
window.title("Tic Tac Toe")
frame=Frame(window,width=400,height=400)

def start_program():
    for x in range(0,3): #creates a board of blank spaces to start with
        for y in range(0,3):
            addLabel(frame,"",x,y)
            global board
            board=[" "]*9
            global turn
            turn="X"
            frame.pack()
            
start_program()

Button(window, text="Restart", command=start_program).pack()

frame.pack()
frame.mainloop()
