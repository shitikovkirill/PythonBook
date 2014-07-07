package program.redact.panel;

import javax.swing.JPanel;

import net.miginfocom.swing.MigLayout;

import javax.swing.JLabel;
import javax.swing.JComboBox;
import javax.swing.JTextField;

import base.Base;

public class Choise extends JPanel {
	private JTextField textField;
	Base base = Base.getBase();
	private String [] ekzamen;
	private String [] specialnost;
	private String [] istochnick;
	private JComboBox comboBox_ekzamen;
	private JComboBox comboBox_specialnost;
	private JComboBox comboBox_istochnick;
	
	/**
	 * Create the panel.
	 */
	public Choise() {
		
		getDataFoCheckBox();
		
		setLayout(new MigLayout("", "[][grow]", "[][][][]"));
		
		JLabel ekzamLabel = new JLabel("Экзамен: ");
		add(ekzamLabel, "cell 0 0,alignx trailing");
		
		comboBox_ekzamen = new JComboBox(ekzamen);
		add(comboBox_ekzamen, "cell 1 0,growx");
		
		JLabel specialnostLabel = new JLabel("Специальность: ");
		add(specialnostLabel, "cell 0 1,alignx trailing");
		
		comboBox_specialnost = new JComboBox(specialnost);
		add(comboBox_specialnost, "cell 1 1,growx");
		
		JLabel istochnicLabel = new JLabel("Источник: ");
		add(istochnicLabel, "cell 0 2,alignx trailing");
		
		comboBox_istochnick = new JComboBox(istochnick);
		add(comboBox_istochnick, "cell 1 2,growx");
		
		JLabel lblNewLabel = new JLabel("Название теста: ");
		add(lblNewLabel, "cell 0 3,alignx trailing");
		
		textField = new JTextField();
		add(textField, "cell 1 3,growx");
		textField.setColumns(10);

	}
	public int getKrokID(){
		return comboBox_ekzamen.getSelectedIndex()+1;
	}
	public int getSpecialnostID(){
		return comboBox_specialnost.getSelectedIndex()+1;
	}
	public int getBaseID(){
		return comboBox_istochnick.getSelectedIndex()+1;
	}
	public String getTestName(){
		return textField.getText();
	}

	private void getDataFoCheckBox() {
		ekzamen = base.listKrok();
		specialnost = base.listSpecialnost();
		istochnick = base.listBase();
	}

}
