package base;

import static org.junit.Assert.*;

import java.util.List;

import base.Base;
import org.junit.Test;

public class BaseTest {
Base base = Base.getBase();
@Test
public void test3() {
	String st[] = base.listKrok();
	System.out.println("ttttttttttt"+st[1]);
}

	@Test
	public void test() {
		
	int count =	base.getCount("kroks");
	int professionsCount = base.getCount("professions");
	int baseCount = base.getCount("bases");
	
	System.out.println("kroks" +count);
	System.out.println("professionsCount " +professionsCount);
	System.out.println("baseCount " +baseCount);
	}
	
	@Test	
	public void test2(){
		List list =null;
		list = base.extractionDisciplines(1,2,1);
		if (list.size()==0){
			System.out.println("!!!!!!!!!!!!!!!!!!!!");
		}
		for(int i = 0; i<list.size(); i++){
			System.out.println(list.get(i));
		}
	}
	
	@Test
	public void extractionTextText(){
		String st = base.extractionText("kroks","krok_id", 1);
		System.out.println(st);
	}
@Test
	public void createTree() {
		int kroksCount = base.getCount("kroks");
		int professionsCount = base.getCount("professions");
		int baseCount = base.getCount("bases");
		
		for (int i=1; i<=kroksCount; i++){
			for (int q=1; q<=professionsCount; q++){
				for (int w=1; w<=baseCount; w++){
					List list = base.extractionDisciplines(i, q, w);
					if(list.size()!= 0){
						String kroksStr = base.extractionText("kroks","krok_id", i);
						String professionsStr = base.extractionText("professions","profession_id", q);
						String baseStr = base.extractionText("bases","base_id", w);
						
						System.out.println("&&&&&& "+ kroksStr+ professionsStr+ baseStr);
					}
				}
			}
		}
		
	}
}
