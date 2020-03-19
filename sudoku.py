board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#(int[][]->boolean)
# recursively solves the sudoku box and return True or False depending on whether 
# it is solved at that stage or not
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row , col = find
    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col]=i
            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False
    


#(int[][],int,tuple(int)->
#Checks if newly added number is not already in the sudoku box
def valid(board, num , pos):
    #Checking through the row
    for j in range(len(board[0])):
        if board[pos[0]][j]== num and pos[1]!=j:
            return False
    #Checking through the row of the matrix
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0]!=i:
            return False
    #Checking each box in the sudoku box
    box_x = pos[1] //3
    box_y = pos[0] //3
    
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if board[i][j] == num and (i,j)!=pos:
                return False
    return True
            
#(int[][]->None)
#Function prints out a board in sudoku style
def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("-------------------")
        for j in range(len(board[0])):
            if j%3==0:
                print("|",end="")
            if j==8:
                print(board[i][j])
                    
            else:
                print(str(board[i][j])+" ",end="")


#(int[][]->tuple(int))
#function returns the position of the empty slot(0) 
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==0):
                return (i,j) # row, colum 
    return None            
                
print_board(board)
solve(board)
print("\n\n")
print_board(board)                
				