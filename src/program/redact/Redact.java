package program.redact;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.border.EmptyBorder;
import javax.swing.JTabbedPane;

import program.redact.panel.AddPanel;
import program.redact.panel.Choise;
import program.redact.panel.RedactPanel;
import program.tree.DrivingTree;

import javax.swing.JButton;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Redact extends JFrame {

	private JPanel contentPane;

	/**
	 * Create the frame.
	 */
	public Redact() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
		
		JPanel panelTree = new JPanel();
		contentPane.add(panelTree, BorderLayout.EAST);
		panelTree.setLayout(new BorderLayout(0, 0));
		
		DrivingTree drivingTree = new DrivingTree("Тесты");
		panelTree.add(drivingTree, BorderLayout.CENTER);
		
		JPanel panelButton = new JPanel();
		panelTree.add(panelButton, BorderLayout.SOUTH);
		
		JButton addButton = new JButton("Add");
		addButton.addActionListener(new AddButtonListener());
		panelButton.add(addButton);
		
		JButton dellButton = new JButton("Dell");
		panelButton.add(dellButton);
		
		JButton editButton = new JButton("Edit");
		panelButton.add(editButton);
		
		JPanel panelUp = new JPanel();
		contentPane.add(panelUp, BorderLayout.NORTH);
		
		
		JTabbedPane tabbedPane = new JTabbedPane(JTabbedPane.TOP);
		
		AddPanel addPanel = new AddPanel();
		tabbedPane.addTab("Добавить тест", addPanel);
		contentPane.add(tabbedPane, BorderLayout.CENTER);
		
		RedactPanel redactPanel = new RedactPanel();
		tabbedPane.addTab("Изменить", redactPanel);
		contentPane.add(tabbedPane, BorderLayout.CENTER);
	}
public class AddButtonListener implements ActionListener {
	public void actionPerformed(ActionEvent arg0) {
		JFrame parent = new JFrame();
		Choise choise = new Choise();
		JOptionPane optionPane = new JOptionPane();
	    optionPane.setMessage(choise);
	    optionPane.setMessageType(JOptionPane.QUESTION_MESSAGE);
	    optionPane.setOptionType(JOptionPane.OK_CANCEL_OPTION);
	    JDialog dialog = optionPane.createDialog(parent, "Создать тест");
	    dialog.setVisible(true);
	    
	    int selection = getSelection(optionPane);

	    switch (selection) {
	    case JOptionPane.OK_OPTION:
	    	int krokID =choise.getKrokID();
	    	int specialnostID = choise.getSpecialnostID();
	    	int baseID = choise.getBaseID();
	    	String testName = choise.getTestName();
	      System.out.println("OK_OPTION");
	      
	      break;
	    case JOptionPane.CANCEL_OPTION:
	      System.out.println("CANCEL");
	      break;
	    default:
	      System.out.println("Others");
	    }

	  }

	  public int getSelection(JOptionPane optionPane) {
	    int returnValue = JOptionPane.CLOSED_OPTION;

	    Object selectedValue = optionPane.getValue();
	    if (selectedValue != null) {
	      Object options[] = optionPane.getOptions();
	      if (options == null) {
	        if (selectedValue instanceof Integer) {
	          returnValue = ((Integer) selectedValue).intValue();
	        }
	      } else {
	        for (int i = 0, n = options.length; i < n; i++) {
	          if (options[i].equals(selectedValue)) {
	            returnValue = i;
	            break; // out of for loop
	          }
	        }
	      }
	    }
	    return returnValue;
	  }
	}
}

