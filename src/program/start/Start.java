package program.start;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import net.miginfocom.swing.MigLayout;
import javax.swing.JButton;

import program.redact.Redact;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Start extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Start frame = new Start();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Start() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
		
		JPanel panelMenu = new JPanel();
		contentPane.add(panelMenu, BorderLayout.CENTER);
		panelMenu.setLayout(new MigLayout("", "[]", "[][][]"));
		
		JButton buttonStartTest = new JButton("Старт");
		panelMenu.add(buttonStartTest, "cell 0 0");
		
		JButton buttonAddTest = new JButton("Редактировать");
		buttonAddTest.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Redact redact =new Redact();
				redact.show();
			}
		});
		panelMenu.add(buttonAddTest, "cell 0 1");
		
		JButton btnNewButton_2 = new JButton("New button");
		panelMenu.add(btnNewButton_2, "cell 0 2");
	}

}
