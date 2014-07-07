package program.redact.panel;

import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class AddPanel extends JPanel {
	private JTextField varTextField [] = new JTextField [5];
	private JTextArea textArea;
	
	/**
	 * Create the panel.
	 */
	public AddPanel() {
		setLayout(new BorderLayout(0, 0));
		
		JPanel panel = new JPanel();
		add(panel, BorderLayout.CENTER);
		panel.setLayout(new GridLayout(2, 0, 0, 0));
		
		textArea = new JTextArea();
		panel.add(textArea);
		
		JPanel panelAsk = new JPanel();
		panel.add(panelAsk);
		panelAsk.setLayout(new GridLayout(5, 1, 5, 5));
		
		for(int i=0; i<5; i++){
			varTextField[i] = new JTextField();
			panelAsk.add(varTextField[i]);
		}
		
		JPanel panelButtom = new JPanel();
		add(panelButtom, BorderLayout.SOUTH);
		panelButtom.setLayout(new BorderLayout(0, 0));
		
		JPanel panel_1 = new JPanel();
		panelButtom.add(panel_1, BorderLayout.CENTER);
		
		JButton addButton = new JButton("Добавить");
		addButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
			}
		});
		panel_1.add(addButton);

	}
	
	public String getAsk(){
		return textArea.getText();
		
	}
	
	public String[] getVar(){
		 String[] var= new String[5];
		 for(int i=0;i<5;i++){
			 var[i]=varTextField[i].getText();
		 }
		return var;
	}

}
