
import unittest

class Overflow(Exception):
    pass

class Winner(Exception):
    pass

class OutOfRange(Exception):
    pass

class FourInLine:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.token = Token()
    
    def placeToken(self, column):
        
        if column > 8:
            raise OutOfRange
        row = self.emptySpace(column)
        self.token.changeColour()
        self.board[row][column] = self.token.colour

        #Condicion vertical
        counter = 0
        for i in range(4): 
            if row > 4:
                break   
            if self.board[row + i][column] == self.token.colour:
                counter = counter +1
                continue
            else:
                break
        if counter == 4:
            raise Winner('You win')

        #Condicion horizontal
        counter = 0        
        for i in range(4):        
            if self.board[row][column -1] == self.token.colour and column != 0:
                column = column -1
                counter = counter +1
                continue
            else:
                break
        
        counter = 0
        for i in range(4):
            if self.board[row][column +i] == self.token.colour and column < 5:
                counter = counter +1
            else:
                break                    
        if counter == 4:
            raise Winner('You win')
        
        #Condicion diagonal
        counter = 0
        for i in range(4):        
            if self.board[row -1][column -1] == self.token.colour and column > 0 and row > 0:
                column = column - 1
                row = row - 1
                counter = counter + 1
                continue
            else:
                counter = 0
                break
            
        for i in range(4):    
            if self.board[row +i][column +i] == self.token.colour and column < 5 or row == 0:
                counter = counter +1
                continue
            else:
                counter = 0
                break
        if counter == 4:
            raise Winner('You win')
    
        for i in range(4):        
            if self.board[row +i][column +i] == self.token.colour and column < 5 and row < 5:
                counter = counter + 1
                continue
            else:
                break
        if counter == 4:
            raise Winner('You win')
        
        counter = 0
        for i in range(4):        
            if self.board[row +1][column -1] == self.token.colour and column != 0 and row < 6:
                column = column - 1
                row = row + 1
                counter = counter + 1
                continue
            else:
                if row == 6 and self.board[row +1][column -1] == self.token.colour:
                    row = row +1
                    column = column -1
                    break
        counter = 0
        for i in range(4):        
            if self.board[row -i][column +i] == self.token.colour and column < 5 and row > 2:
                counter = counter + 1
                continue
            else:
                break
        if counter == 4:
            raise Winner('You win')
    
    def emptySpace(self, column):
        for i in range(8):
            if self.board[7-i][column] == None:
                return 7-i
            else:
                continue
        raise Overflow('Column full')
class Token():
    def __init__(self):
        self.colour = 0
    def changeColour(self):
        if self.colour == 0:
            self.colour = 1
        else:
            self.colour = 0

class TestFourInLine(unittest.TestCase):

    def test_CreateGame(self):
        game = FourInLine()
        self.assertEqual(game.board, [[None for _ in range(8)] for _ in range(8)])

    def test_Token(self):
        token = Token()
        self.assertEqual(token.colour, 0)

    def test_ChangeColour(self):
        token = Token()
        token.changeColour()
        self.assertEqual(token.colour, 1)

    def test_ChangeColourInverse(self):
        token = Token()
        token.colour = 1
        token.changeColour()
        self.assertEqual(token.colour, 0)

    def test_EmptySpaceHappy(self):
        game = FourInLine()
        game.emptySpace(1)
        self.assertEqual(game.emptySpace(1), 7)

    def test_EmptySpaceHappy2(self):
        game = FourInLine()
        game.board[7][1] = 0
        row = game.emptySpace(1)
        self.assertEqual(row, 6)

    def test_EmptySpaceSad(self):
        game = FourInLine()
        for i in range(8):
            game.board[7-i][1] = 0
        with self.assertRaises(Overflow):
            game.emptySpace(1)

    def test_ConditionHorizontal(self):
        game = FourInLine()
        for i in range(3):
            game.board[7][7 - i] = 1
        with self.assertRaises(Winner):
            game.placeToken(4)
        
    def test_PlaceTokenVertcialHappy(self):
        game = FourInLine()
        for i in range(3):
            game.board[7 - i][1] = 1
        with self.assertRaises(Winner):
            game.placeToken(1)
    
    def test_PlaceTokenHorizontalHappy0(self):
        game = FourInLine()
        for i in range(3):
            game.board[7][i + 1] = 1
        with self.assertRaises(Winner):
            game.placeToken(0)
    
    def test_PlaceTokenHorizontalHappy7(self):
        game = FourInLine()
        for i in range(3):
            game.board[7][i + 4] = 1
        with self.assertRaises(Winner):
            game.placeToken(7)
    
    def test_PlaceTokenHorizontalHappy1(self):
        game = FourInLine()
        game.board[7][0] = 1
        game.board[7][2] = 1
        game.board[7][3] = 1
        with self.assertRaises(Winner):
            game.placeToken(1)
    
    def test_PlaceTokenHorizontalHappy6(self):
        game = FourInLine()
        game.board[7][7] = 1
        game.board[7][5] = 1
        game.board[7][4] = 1
        with self.assertRaises(Winner):
            game.placeToken(6)
    
    def test_PlaceTokenHorizontalHappy21(self):
        game = FourInLine()
        game.board[7][0] = 1
        game.board[7][1] = 1
        game.board[7][3] = 1
        with self.assertRaises(Winner):
            game.placeToken(2)
    
    def test_PlaceTokenHorizontalHappy22(self):
        game = FourInLine()
        game.board[7][1] = 1
        game.board[7][3] = 1
        game.board[7][4] = 1
        with self.assertRaises(Winner):
            game.placeToken(2)
    
    def test_PlaceTokenHorizontalHappy31(self):
        game = FourInLine()
        game.board[7][1] = 1
        game.board[7][2] = 1
        game.board[7][4] = 1
        with self.assertRaises(Winner):
            game.placeToken(3)
    
    def test_PlaceTokenHorizontalHappy32(self):
        game = FourInLine()
        game.board[7][2] = 1
        game.board[7][4] = 1
        game.board[7][5] = 1
        with self.assertRaises(Winner):
            game.placeToken(3)
    
    def test_PlaceTokenHorizontalHappy41(self):
        game = FourInLine()
        game.board[7][2] = 1
        game.board[7][3] = 1
        game.board[7][5] = 1
        with self.assertRaises(Winner):
            game.placeToken(4)
    
    def test_PlaceTokenHorizontalHappy42(self):
        game = FourInLine()
        game.board[7][3] = 1
        game.board[7][5] = 1
        game.board[7][6] = 1
        with self.assertRaises(Winner):
            game.placeToken(4)
    
    def test_PlaceTokenHorizontalHappy51(self):
        game = FourInLine()
        game.board[7][4] = 1
        game.board[7][6] = 1
        game.board[7][7] = 1
        with self.assertRaises(Winner):
            game.placeToken(5)
    
    def test_PlaceTokenHorizontalHappy52(self):
        game = FourInLine()
        game.board[7][3] = 1
        game.board[7][4] = 1
        game.board[7][6] = 1
        with self.assertRaises(Winner):
            game.placeToken(5)
    
    def test_PlaceTokenDiagonalHappy3DAB(self):
        game = FourInLine()
        game.board[5][0] = 0
        game.board[6][0] = 0
        game.board[7][0] = 0
        game.board[5][1] = 1
        game.board[6][2] = 1
        game.board[7][3] = 1
        with self.assertRaises(Winner):
            game.placeToken(0)
    
    def test_PlaceTokenDiagonalHappy3IAB(self):
        game = FourInLine()
        game.board[5][7] = 0
        game.board[6][7] = 0
        game.board[7][7] = 0
        game.board[5][6] = 1
        game.board[6][5] = 1
        game.board[7][4] = 1
        with self.assertRaises(Winner):
            game.placeToken(7)
    
    def test_PlaceTokenDiagonalHappy3DAR(self):
        game = FourInLine()
        game.board[4][0] = 0
        game.board[5][0] = 0
        game.board[6][0] = 0
        game.board[7][0] = 0
        game.board[2][1] = 1
        game.board[1][2] = 1
        game.board[0][3] = 1
        with self.assertRaises(Winner):
            game.placeToken(0)
    
    def test_PlaceTokenDiagonalHappy3IAR(self):
        game = FourInLine()
        game.board[4][7] = 0
        game.board[5][7] = 0
        game.board[6][7] = 0
        game.board[7][7] = 0
        game.board[2][6] = 1
        game.board[1][5] = 1
        game.board[0][4] = 1
        with self.assertRaises(Winner):
            game.placeToken(7)
    
    def test_PlaceTokenDiagonalHappy1IAB2DAR(self):
        game = FourInLine()
        game.board[7][1] = 0
        game.board[7][0] = 1
        game.board[5][2] = 1
        game.board[4][3] = 1
        with self.assertRaises(Winner):
            game.placeToken(1)
    
    def test_PlaceTokenDiagonalHappy1DAB2IAR(self):
        game = FourInLine()
        game.board[7][6] = 0
        game.board[7][7] = 1
        game.board[5][5] = 1
        game.board[4][4] = 1
        with self.assertRaises(Winner):
            game.placeToken(6)
    
    def test_PlaceTokenDiagonalHappy2IAB1DAR(self):
        game = FourInLine()
        game.board[7][6] = 0
        game.board[6][6] = 0
        game.board[4][7] = 1
        game.board[6][5] = 1
        game.board[7][4] = 1
        with self.assertRaises(Winner):
            game.placeToken(6)
    
    def test_PlaceTokenDiagonalHappy2DAB1IAR(self):
        game = FourInLine()
        game.board[7][1] = 0
        game.board[6][1] = 0
        game.board[4][0] = 1
        game.board[6][2] = 1
        game.board[7][3] = 1
        with self.assertRaises(Winner):
            game.placeToken(1)

if __name__ == '__main__':
    unittest.main()