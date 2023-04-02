// OPENAI CODEX - Instructions
// Create a quizz app on java swing with country flags displayed on top of each question, asking the user wich countries corresponds to the flag shown on each question, with the options of all countries listed in checkboxes and the number of questions being the same as the number of flags, display the final score when user finishes quizz
// Run quizz app

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class QuizzApp extends JFrame {
    // Declare class variables
    private ArrayList<Flag> flags;
    private int currentQuestion;
    private int totalScore;
    private JLabel lblQuestion, lblScore;
    private JButton btnNext;
    private JCheckBox[] chkOptions;
    private JPanel pnlMain, pnlTop, pnlBottom;

    // Constructor
    public QuizzApp() {
        // Initialize class variables
        flags = new ArrayList<>();
        currentQuestion = 0;
        totalScore = 0;

        // Set frame parameters
        setTitle("Flag Quizz App");
        setSize(400, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        // Initialize components
        lblQuestion = new JLabel();
        lblScore = new JLabel("Score: 0");
        btnNext = new JButton("Next");
        btnNext.addActionListener(new NextButtonListener());
        chkOptions = new JCheckBox[Flag.ALL_COUNTRIES.length];
        for (int i = 0; i < chkOptions.length; i++) {
            chkOptions[i] = new JCheckBox(Flag.ALL_COUNTRIES[i]);
        }
        pnlMain = new JPanel();
        pnlTop = new JPanel();
        pnlBottom = new JPanel();

        // Add components to the frame
        add(pnlMain);
        pnlMain.setLayout(new BorderLayout());
        pnlMain.add(pnlTop, BorderLayout.NORTH);
        pnlMain.add(pnlBottom, BorderLayout.CENTER);
        pnlTop.add(lblQuestion);
        pnlTop.add(lblScore);
        pnlBottom.setLayout(new GridLayout(chkOptions.length + 1, 1));
        for (JCheckBox chkOption : chkOptions) {
            pnlBottom.add(chkOption);
        }
        pnlBottom.add(btnNext);

        // Populate the flags arraylist
        for (String country : Flag.ALL_COUNTRIES) {
            flags.add(Flag.getFlag(country));
        }

        // Load the first question
        loadQuestion();
    }

    // Method to load the next question
    private void loadQuestion() {
        // Reset the checkboxes
        for (JCheckBox chkOption : chkOptions) {
            chkOption.setSelected(false);
        }

        // Check if all questions have been answered
        if (currentQuestion < flags.size()) {
            // Get the current flag
            Flag flag = flags.get(currentQuestion);

            // Set the question label
            lblQuestion.setText("Which countries correspond to this flag?");
            lblQuestion.setIcon(flag.getIcon());

            // Set the checkboxes
            for (int i = 0; i < chkOptions.length; i++) {
                chkOptions[i].setText(Flag.ALL_COUNTRIES[i]);
            }

            // Increment the current question
            currentQuestion++;
        } else {
            // Show the final score
            lblQuestion.setText("You answered " + totalScore + " out of " + flags.size() + " questions correctly!");
            lblQuestion.setIcon(null);

            // Disable the checkboxes
            for (JCheckBox chkOption : chkOptions) {
                chkOption.setEnabled(false);
            }
        }
    }

    // Private inner class to handle the Next button
    private class NextButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Calculate the score
            Flag flag = flags.get(currentQuestion - 1);
            int correctAnswers = 0;
            for (JCheckBox chkOption : chkOptions) {
                if (flag.isCountry(chkOption.getText()) && chkOption.isSelected()) {
                    correctAnswers++;
                }
            }
            totalScore += correctAnswers;
            lblScore.setText("Score: " + totalScore);

            // Load the next question
            loadQuestion();
        }
    }

    // Main method
    public static void main(String[] args) {
        QuizzApp frame = new QuizzApp();
        frame.setVisible(true);
    }
}

// Flag class
class Flag {
    // Array of all countries
    public static String[] ALL_COUNTRIES = {
        "FRANCE", "GERMANY", "INDIA", "RUSSIA", "DENMARK"
    };

    // Instance variables
    private String country;
    private Icon icon;

    // Constructor
    public Flag(String country, Icon icon) {
        this.country = country;
        this.icon = icon;
    }

    // Getter methods
    public String getCountry() {
        return country;
    }

    public Icon getIcon() {
        return icon;
    }

    // Method to check if the country is the same
    public boolean isCountry(String country) {
        return this.country.equals(country);
    }

    // Static method to get a flag for the given country
    public static Flag getFlag(String country) {
        switch (country) {
            case "FRANCE":
                return new Flag(country, new ImageIcon("C:/Users/ricar/js-projs/flag1.png"));
            case "GERMANY":
                return new Flag(country, new ImageIcon("C:/Users/ricar/js-projs/flag2.png"));
            case "INDIA":
                return new Flag(country, new ImageIcon("C:/Users/ricar/js-projs/flag3.png"));
            case "RUSSIA":
                return new Flag(country, new ImageIcon("C:/Users/ricar/js-projs/flag4.png"));
            case "DENMARK":
                return new Flag(country, new ImageIcon("C:/Users/ricar/js-projs/flag5.png"));
            default:
                return null;
        }
    }
}
