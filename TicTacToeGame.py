# TicTacToe Game

#Display function 
def displayBoard(row1,row2,row3,row4,row5):
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)

row1 = ["   ,|    ,|    "]
row2 =  "---------------"
row3 = ["   ,|    ,|    "]
row4 = "----------------"
row5 = ["   ,|    ,|    "]

displayBoard(row1,row2,row3,row4,row5)

#Position function



def position_change():

    choice = 'Wrong'

    while choice not in ['0','1','2']:

        choice = input('Pick a positionn in (0,1,2): ')

        if choice not in ['0','1','2']:
            print('Sorry, invalid choice!')

        return int(choice)
    
    
