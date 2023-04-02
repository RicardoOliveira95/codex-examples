import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Minesweeper extends JFrame {
    // set game constants
    private static final int ROWS = 10;
    private static final int COLS = 10;
    private static final int NUM_MINES = 10;
    private static final int CELL_SIZE = 30;
    
    // set up game variables
    private boolean gameOver = false;
    private JButton[][] buttons = new JButton[ROWS][COLS];
    private int[][] minefield = new int[ROWS][COLS];
    private int numCorrectGuesses = 0;
    
    public Minesweeper() {
        // set up game board
        setLayout(new GridLayout(ROWS, COLS));
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                JButton btn = new JButton();
                btn.setPreferredSize(new Dimension(CELL_SIZE, CELL_SIZE));
                btn.addActionListener(new MyButtonListener());
                add(btn);
                buttons[row][col] = btn;
            }
        }
        
        // add mines to minefield
        addMinesToMinefield();
        
        // add numbers to minefield
        addNumbersToMinefield();
        
        // set size of window
        setSize(COLS * CELL_SIZE, ROWS * CELL_SIZE);
    }
    
    // adds mines to minefield
    private void addMinesToMinefield() {
        int numMinesAdded = 0;
        while (numMinesAdded < NUM_MINES) {
            int row = (int) (Math.random() * ROWS);
            int col = (int) (Math.random() * COLS);
            if (minefield[row][col] != -1) {
                minefield[row][col] = -1;
                numMinesAdded++;
            }
        }
    }
    
    // adds numbers to minefield
    private void addNumbersToMinefield() {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (minefield[row][col] != -1) {
                    int numMines = getNumMines(row, col);
                    minefield[row][col] = numMines;
                }
            }
        }
    }
    
    // get number of mines around a cell
    private int getNumMines(int row, int col) {
        int numMines = 0;
        for (int r = row - 1; r <= row + 1; r++) {
            for (int c = col - 1; c <= col + 1; c++) {
                if (r >= 0 && r < ROWS && c >= 0 && c < COLS) {
                    if (minefield[r][c] == -1) {
                        numMines++;
                    }
                }
            }
        }
        return numMines;
    }
    
    // inner class for button listener
    private class MyButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            // get source button
            JButton btn = (JButton) e.getSource();
            if (gameOver) {
                return;
            }
            // check if button is a mine
            for (int row = 0; row < ROWS; row++) {
                for (int col = 0; col < COLS; col++) {
                    if (btn == buttons[row][col]) {
                        // game over if mine
                        if (minefield[row][col] == -1) {
                            gameOver = true;
                            btn.setText("M");
                            btn.setBackground(Color.RED);
                            showAllMines();
                            showGameOverMessage();
                        }
                        // otherwise, show number of mines
                        else {
                            btn.setText(minefield[row][col] + "");
                            btn.setEnabled(false);
                            numCorrectGuesses++;
                            if (numCorrectGuesses == ROWS * COLS - NUM_MINES) {
                                showGameWonMessage();
                            }
                        }
                    }
                }
            }
        }
    }
    
    // displays all mines on the board
    private void showAllMines() {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (minefield[row][col] == -1) {
                    buttons[row][col].setText("M");
                    buttons[row][col].setBackground(Color.RED);
                    buttons[row][col].setEnabled(false);
                }
            }
        }
    }
    
    // displays game over message
    private void showGameOverMessage() {
        JOptionPane.showMessageDialog(null, "Game Over!");
    }
    
    // displays game won message
    private void showGameWonMessage() {
        JOptionPane.showMessageDialog(null, "You Win!");
    }
    
    public static void main(String[] args) {
        Minesweeper game = new Minesweeper();
        game.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        game.setVisible(true);
    }
}