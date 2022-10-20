#FrontEnd FourInLine

# import unittest

from FourInLine import FourInLine
from FourInLine import Overflow
from FourInLine import Winner
from FourInLine import OutOfRange
from FourInLine import NotNum
from FourInLine import Quit

class Frontendgame():
    def __init__(self):        
        self.game = FourInLine()
        self.combustible = True

    def tablero(self):
        for row in range(8):
            for column in range(8):
                print(" " + str(self.game.board[row][column]) + " ", end="")
            print("\n")

    def entrada(self):
        try:
            valor = int(input("Ingrese la columna (0-7): "))
            self.game.placeToken(valor)
        except Winner:
            print('You win')
            self.combustible = False
        except Overflow:
            print('Column full')
        except Quit:
            print("Vuelva pronto")
            self.combustible = False
        except OutOfRange:
            print('Numero fuera de rango, rango valido [0-7]')
        except NotNum:
            print("El valor ingresado no es un número")

    def motor(self):
        while self.combustible == True:
            self.tablero()
            self.entrada()
        
        self.tablero()

if __name__ == '__main__':
    jueguito = Frontendgame()
    jueguito.motor()










# def run(self):
#     self.backendboard = FourInLine()
#     self.motor = True
#     self.tablero = [[" " for _ in range(8)] for _ in range(8)]
#     while self.motor == True:
#         for row in range(8):
#             for column in range(8):
#                 if self.backendboard.board[row][column]== 0:
#                     self.tablero[row][column] = "X"
#                 elif self.backendboard.board[row][column]== 1:
#                     self.tablero[row][column] = "O"
#                 else:
#                     self.tablero[row][column] = " "
#         print(self.tablero)        
# print("\n")
# run()











































#     def __init__(self):
#         self.FE4Line = FourInLine()
#         self.run = True
#         self.interaction = input("\n""Number between 0 - 7 or if you want to quit put 'q':")

#     def run(self):
#         while self.run == True:
#             self.FE4Line.board.replace(None, " ").replace(0, "X").replace(1, "O")
#             print(self.FE4Line.board)

#             if self.interaction != "q" and self.interaction.isdigit() == False:
#                 raise NotNum
#                 print("El valor ingresado no es un número")
#             elif self.interaction != len(8):
#                 raise OutOfRange
#                 print("El numero ingresado esta fuera del tablero - tablero (0-7)")

