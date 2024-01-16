def main():
    board=[['-','-','-'],['-','-','-'],['-','-','-']]
    positions={1:"0 0",2:"0 1",3:"0 2",
               4:"1 0",5:"1 1",6:"1 2",
               7:"2 0",8:"2 1",9:"2 2",
               }
    while(full(board)==True):
        try:
            user_position=int(input("Enter the position you want to play in (1-9) "))
        except ValueError:
            print("Enter a valid position ")

            continue

        
    

    # while True:
    #     player_1=input("Do you want to choose X or 0 ? ")

    #     if player_1 in ["x","0"]:
    #         break

    #     print("Please Enter a valid input....")





    



def display_board(board):
    print(f"""
              -------------
              | {board[0][0]} | {board[0][1]} | {board[0][2]} |
              -------------
              | {board[1][0]} | {board[1][1]} | {board[1][2]} |
              -------------
              | {board[2][0]} | {board[2][1]} | {board[2][2]} |
              -------------
             """)
    
def full(board):
    if (board[0][0]=="x" and board[0][1]=="x"and board[0][2]=="x") or (board[0][0]=="x" and board[0][1]=="x"and board[0][2]=="x") :
        return True
    
    if (board[1][0]=="x" and board[1][1]=="x"and board[1][2]=="x") or (board[1][0]=="x" and board[1][1]=="x"and board[1][2]=="x") :
        return True
    
    if (board[2][0]=="x" and board[2][1]=="x"and board[2][2]=="x") or (board[2][0]=="x" and board[2][1]=="x"and board[2][2]=="x") :
        return True
    
    if (board[1][0]=="x" and board[2][0]=="x" and board[3][0]=="x" or  )
    

    

    

    
    
if __name__=="__main__":
    main()