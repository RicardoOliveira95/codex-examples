import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import javax.swing.JFrame;

public class SnakeGame extends JFrame implements KeyListener {
  private ArrayList<int[]> snake;
  private int[] fruit;
  private int direction;
  private boolean gameOver;
  
  public SnakeGame() {
    // set up window
    setSize(400, 400);
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setVisible(true);
    
    // init variables
    snake = new ArrayList<int[]>();
    snake.add(new int[]{200, 200});
    fruit = new int[] {100, 100};
    direction = KeyEvent.VK_DOWN;
    gameOver = false;
    
    // add key listener
    addKeyListener(this);
  }
  
  public void keyPressed(KeyEvent e) {
    // update direction
    if (e.getKeyCode() == KeyEvent.VK_UP && direction != KeyEvent.VK_DOWN) {
      direction = KeyEvent.VK_UP;
    }
    if (e.getKeyCode() == KeyEvent.VK_DOWN && direction != KeyEvent.VK_UP) {
      direction = KeyEvent.VK_DOWN;
    }
    if (e.getKeyCode() == KeyEvent.VK_LEFT && direction != KeyEvent.VK_RIGHT) {
      direction = KeyEvent.VK_LEFT;
    }
    if (e.getKeyCode() == KeyEvent.VK_RIGHT && direction != KeyEvent.VK_LEFT) {
      direction = KeyEvent.VK_RIGHT;
    }
  }
  
  public void keyReleased(KeyEvent e) {
    // do nothing
  }
  
  public void keyTyped(KeyEvent e) {
    // do nothing
  }
  
  public void update() {
    // move snake
    int[] head = snake.get(0);
    int[] newHead = head.clone();
    if (direction == KeyEvent.VK_UP) {
      newHead[1] -= 10;
    }
    if (direction == KeyEvent.VK_DOWN) {
      newHead[1] += 10;
    }
    if (direction == KeyEvent.VK_LEFT) {
      newHead[0] -= 10;
    }
    if (direction == KeyEvent.VK_RIGHT) {
      newHead[0] += 10;
    }
    // check if snake ate fruit
    if (newHead[0] == fruit[0] && newHead[1] == fruit[1]) {
      snake.add(head.clone());
      newFruit();
    }
    // move body
    for (int i = snake.size() - 1; i > 0; i--) {
      snake.set(i, snake.get(i-1).clone());
    }
    snake.set(0, newHead);
    // check for game over
    if (gameOver()) {
      gameOver = true;
    }
  }
  
  public boolean gameOver() {
    // check if head collided with body
    int[] head = snake.get(0);
    for (int i = 1; i < snake.size(); i++) {
      int[] bodyPart = snake.get(i);
      if (head[0] == bodyPart[0] && head[1] == bodyPart[1]) {
        return true;
      }
    }
    // check if head out of bounds
    if (head[0] < 0 || head[0] > 390 || head[1] < 0 || head[1] > 390) {
      return true;
    }
    return false;
  }
  
  public void newFruit() {
    // generate random x and y
    int x = (int)(Math.random() * 40) * 10;
    int y = (int)(Math.random() * 40) * 10;
    // check if fruit is on top of snake
    for (int[] bodyPart : snake) {
      if (x == bodyPart[0] && y == bodyPart[1]) {
        newFruit();
        return;
      }
    }
    // set fruit
    fruit[0] = x;
    fruit[1] = y;
  }
  
  public void paint(Graphics g) {
    // paint background
    g.setColor(Color.BLACK);
    g.fillRect(0,  0,  400,  400);
    // paint snake
    g.setColor(Color.GREEN);
    for (int[] bodyPart : snake) {
      g.fillRect(bodyPart[0], bodyPart[1], 10, 10);
    }
    // paint fruit
    g.setColor(Color.RED);
    g.fillOval(fruit[0], fruit[1], 10, 10);
    
    // paint game over
    if (gameOver) {
      g.setColor(Color.WHITE);
      g.drawString("Game Over!", 170, 200);
    }
  }
  
  public static void main(String[] args) {
    SnakeGame game = new SnakeGame();
    while (!game.gameOver) {
      game.update();
      game.repaint();
      try {
        Thread.sleep(100);
      }
      catch (Exception e) {
        // do nothing
      }
    }
  }
}