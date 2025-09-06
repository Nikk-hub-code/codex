import math
import numpy as np

class BowlShapeGame:
    def workspace(self,rows,columns):
        workspaceArr = []
        for i in range(rows):
            row_input = input(f"Row {i+1}= ").upper()
            row_values = row_input.split()
            workspaceArr.append(row_values)
        return workspaceArr

    def bowlShape(self,workspaceCoordinates):
        rowCount = len(workspaceCoordinates)
        columnCount = len(workspaceCoordinates[0])
        CoordinatesArr = []
        for i in range(rowCount):
            maximum = []
            for j in range(columnCount):
                if i == 0 or i == columnCount-1:
                    if workspaceCoordinates[j][i] == 'P':
                        CoordinatesArr.append((j,i))
                else:
                    if j == columnCount-1:
                        if workspaceCoordinates[j][i] == 'P':
                            CoordinatesArr.append((j,i))


        print(CoordinatesArr)

    def calPerimeter(self,coordinates):
        pass

    def run(self):
        matrixRow = int(input("Enter the no.of rows= "))
        matrixColumns = int(input("Enter the no.of columns= "))
        wrkspace = self.workspace(matrixRow,matrixColumns)

        bowlCoordinates = self.bowlShape(wrkspace)

        perimeter = self.calPerimeter(bowlCoordinates)
        print(f"Perimeter of the bowl= {perimeter}")

def main():
    bowlShapeGame = BowlShapeGame()
    bowlShapeGame.run()

if __name__ == "__main__":
    main()