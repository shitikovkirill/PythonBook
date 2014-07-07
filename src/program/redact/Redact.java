package program.redact;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTabbedPane;

import program.redact.panel.AddPanel;
import program.redact.panel.RedactPanel;
import program.tree.DrivingTree;
import javax.swing.JButton;

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

}
