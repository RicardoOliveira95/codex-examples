# Create a tictactoe game using python with tkinter module for the gui

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QLabel, QGridLayout
from PyQt5.QtGui import QIcon


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(50,50,400,400)

        # Create main game window
        self.mainWindow = QWidget()
        self.setCentralWidget(self.mainWindow)

        # Create grid layout
        self.gridLayout = QGridLayout()
        self.mainWindow.setLayout(self.gridLayout)

        # Create the buttons
        self.buttons = []
        for i in range(9):
            self.buttons.append(QPushButton(" "))
            self.buttons[i].clicked.connect(self.buttonClicked)
            self.gridLayout.addWidget(self.buttons[i], i//3, i%3)

        # Create the labels
        self.labels = []
        for i in range(2):
            self.labels.append(QLabel("Player " + str(i+1) + ": 0"))
            self.gridLayout.addWidget(self.labels[i], 4, i)

        self.currentPlayer = 0
        self.show()
    
    def buttonClicked(self):
        button = self.sender()
        button.setText("X" if self.currentPlayer == 0 else "O")
        button.setEnabled(False)
        self.checkForWin()
        self.currentPlayer = 1 if self.currentPlayer == 0 else 0
        self.labels[self.currentPlayer].setText("Player " + str(self.currentPlayer+1) + ": 0")

    def checkForWin(self):
        # Check for horizontal
        for i in range(3):
            if self.buttons[i*3].text() == self.buttons[i*3+1].text() == self.buttons[i*3+2].text() and self.buttons[i*3].text() != " ":
                self.gameOver(self.buttons[i*3].text())
        # Check for vertical
        for i in range(3):
            if self.buttons[i].text() == self.buttons[i+3].text() == self.buttons[i+6].text() and self.buttons[i].text() != " ":
                self.gameOver(self.buttons[i].text())
        # Check for diagonal
        if self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() and self.buttons[0].text() != " ":
            self.gameOver(self.buttons[0].text())
        if self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text() and self.buttons[2].text() != " ":
            self.gameOver(self.buttons[2].text())

    def gameOver(self, player):
        # Disable all buttons
        for button in self.buttons:
            button.setEnabled(False)
        # Set player label
        self.labels[self.currentPlayer].setText("Player " + str(self.currentPlayer+1) + " Wins!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ttt = TicTacToe()
    sys.exit(app.exec_())