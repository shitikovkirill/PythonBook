package base;

import java.io.Serializable;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class Base{
private static Base base=null;	
private	Base (){h2Connection("jdbc:h2:base/test", "sa", "");}

	public Array  askar;
	public String  loginData[][];
	public static Connection connection = null;;
	private ResultSet resultSet = null;
	private Statement statement = null;

	// Создание синглитона
public static Base getBase(){
	if (base==null){
		base=new Base();
		
	}
	return base;
}
	
	// Открытие базы данных
public void  h2Connection(String url, String user, String password){
	
	try {
		Class.forName("org.h2.Driver");
		connection = DriverManager.getConnection(url,user,password);
	} catch (org.h2.jdbc.JdbcSQLException eb) {
		JOptionPane.showMessageDialog( new JFrame(),
                "Открытие одновременно двух тестовых программ невозможно!",
                "Возникла ошибка при открытии программы",
                JOptionPane.ERROR_MESSAGE);
		eb.printStackTrace();
		System.exit(0);
	} catch (Exception e) {
	
		e.printStackTrace();
	}
}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

public List extractionDisciplines(int krokID, int professionID, int baseID ){
	List<String> list = new ArrayList<String>();
	
	try {
		statement = connection.createStatement();
		resultSet = statement.executeQuery("SELECT * FROM DISCIPLINEs WHERE KROK_ID = "+krokID+" and PROFESSION_ID = "+professionID+" and BASE_ID = "+baseID+" ;");
		while (resultSet.next()) {
				list.add(resultSet.getString(5));
		}
		resultSet.close();
		statement.close();
	} catch (SQLException ew) {
		ew.printStackTrace();
	}
	return list;
}

public String extractionText(String table, String rowID, int id ){
	String txt = null;
	try {
		statement = connection.createStatement();
		resultSet = statement.executeQuery("SELECT * FROM "+table+"  WHERE "+rowID+" ="+id+";");
		while (resultSet.next()) {
			txt = resultSet.getString(2);
		}
		resultSet.close();
		statement.close();
	} catch (SQLException ew) {
		ew.printStackTrace();
	}
	return txt;
}


public int getCount(String table){
	
	int result=0;
	try {
		statement = connection.createStatement();
		resultSet = statement.executeQuery("select count(*) from "+table+";");
		System.out.println(resultSet);
		resultSet.next();
		result= resultSet.getInt(1);
		resultSet.close();
		statement.close();
	} catch (SQLException ew) {
		ew.printStackTrace();
	}
	return result;
	
}

public String[] listKrok(){
	ArrayList <String> list = new ArrayList();
	String[] txt = null;
	try {
		statement = connection.createStatement();
		resultSet = statement.executeQuery("SELECT krok FROM kroks;");
		while (resultSet.next()) {
			list.add( resultSet.getString(1));
		}
		resultSet.close();
		statement.close();
		txt=new String[list.size()];
		for(int t = 0;t<list.size();t++){
			txt[t]=list.get(t);
		}
		
	} catch (SQLException ew) {
		ew.printStackTrace();
	}
	return txt;
}
public String[] listSpecialnost(){
	ArrayList <String> list = new ArrayList();
	String[] txt = null;
	try {
		statement = connection.createStatement();
		resultSet = statement.executeQuery("SELECT profession FROM professions;");
		while (resultSet.next()) {
			list.add( resultSet.getString(1));
		}
		resultSet.close();
		statement.close();
		txt=new String[list.size()];
		for(int t = 0;t<list.size();t++){
			txt[t]=list.get(t);
		}
		
	} catch (SQLException ew) {
		ew.printStackTrace();
	}
	return txt;
}

public String[] listBase(){
	ArrayList <String> list = new ArrayList();
	String[] txt = null;
	try {
		statement = connection.createStatement();
		resultSet = statement.executeQuery("SELECT base FROM bases;");
		while (resultSet.next()) {
			list.add( resultSet.getString(1));
		}
		resultSet.close();
		statement.close();
		txt=new String[list.size()];
		for(int t = 0;t<list.size();t++){
			txt[t]=list.get(t);
		}
	} catch (SQLException ew) {
		ew.printStackTrace();
	}
	return txt;
}
//----------------------------------------------------------------


public void save(String obraschenieKBase ){
	
try {
statement = connection.createStatement();
statement.executeUpdate(obraschenieKBase);
statement.close();
} catch (SQLException e) {
e.printStackTrace();
}	
}

public void update(String obraschenieKBase){
	save( obraschenieKBase );
}



public TreeSet<String> list(String obraschenieKBase){
	TreeSet<String> work= new TreeSet<String> ();	
	try {
		statement = connection.createStatement();
		resultSet = statement.executeQuery(obraschenieKBase);
	
	while (resultSet.next()) {
		work.add(resultSet.getString(1));
	}
	
	statement.close();
	} catch (SQLException e) {
		e.printStackTrace();
	}
	return work;
}

public void del(String obraschenieKBase){
	try {
		statement = connection.createStatement();
		statement.executeUpdate(obraschenieKBase);
		statement.close();
	} catch (SQLException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
}

public void closeBase (){
	System.out.println("База закрыта");
		try {
			connection.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
}
protected void finalize(){
	closeBase ();
}
}
