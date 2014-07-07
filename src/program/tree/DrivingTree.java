package program.tree;

import java.awt.BorderLayout;
import java.util.Enumeration;
import java.util.List;

import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTree;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreeNode;
import javax.swing.tree.TreePath;
import javax.swing.tree.TreeSelectionModel;
import javax.swing.JScrollPane;

import base.Base;

public class DrivingTree extends JPanel {
	
	TreeListener treelist = new TreeListener();
	Base base = Base.getBase();
	 
	private DefaultTreeModel treeModel;
	private DefaultMutableTreeNode root;
	private JTree tree;
	StringBuffer outputString = new StringBuffer();

	private JScrollPane scrollPane;
	
	public DrivingTree(String treeTitle) {
		
		root=new DefaultMutableTreeNode(treeTitle);
		treeModel = new DefaultTreeModel(root);
		setLayout(new BorderLayout(0, 0));
		
		tree = new JTree(treeModel);
		tree.setEditable(true);
		tree.getSelectionModel().setSelectionMode(TreeSelectionModel.SINGLE_TREE_SELECTION);
		tree.setShowsRootHandles(true);
		tree.addTreeSelectionListener((TreeSelectionListener) treelist);
		
		scrollPane = new JScrollPane(tree);
		add(scrollPane);
		
		createTree();
	}
	
	private void createTree() {
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
						String basesStr = base.extractionText("bases","base_id", w);
						
						DefaultMutableTreeNode kroksDMTN = new DefaultMutableTreeNode(kroksStr);
						DefaultMutableTreeNode professionsDMTN = new DefaultMutableTreeNode(professionsStr);
						kroksDMTN.add(professionsDMTN);
						DefaultMutableTreeNode basesDMTN = new DefaultMutableTreeNode(basesStr);
						professionsDMTN.add(basesDMTN);
							
						for(int e =0; e<list.size(); e++){
							DefaultMutableTreeNode DiscipliniDMTN = new DefaultMutableTreeNode(list.get(e));
							basesDMTN.add(DiscipliniDMTN);
						}
						
						treeModel.insertNodeInto(kroksDMTN, root, root.getChildCount());
					}
				}
			}
		}
		
	}

	public DefaultMutableTreeNode addNode(String newNodeStr) throws NullPointerException{
		
		DefaultMutableTreeNode selectedNode=(DefaultMutableTreeNode)(tree.getLastSelectedPathComponent());
		
		DefaultMutableTreeNode newNode =new DefaultMutableTreeNode(newNodeStr);
		
		treeModel.insertNodeInto(newNode, selectedNode, selectedNode.getChildCount());
		
		tree.scrollPathToVisible(new TreePath(newNode.getPath()));
		
		return newNode;
		
		}
	
	public void dellNod() throws NullPointerException{
		
		DefaultTreeModel model = (DefaultTreeModel)tree.getModel();
		
		DefaultMutableTreeNode selectedNode=(DefaultMutableTreeNode)(tree.getLastSelectedPathComponent());
		
		if(!selectedNode.isRoot()) model.removeNodeFromParent(selectedNode);
		
	}
	
	public void informtion(){

		
		// How to get the selected node
		// Returns the last selected node in the tree
		Object treeObject = tree.getLastSelectedPathComponent();
		
		// Cast the Object into a DefaultMutableTreeNode
		
		DefaultMutableTreeNode theFile = (DefaultMutableTreeNode) treeObject;
		
		// Returns the object stored in this node and casts it to a string
		
		String treeNode = (String) theFile.getUserObject();
		
		outputString .append("The Selected Node: " + treeNode + "\n");
		
		// Get the number of children this node has
		
		outputString.append( "Number of Children: " + theFile.getChildCount() + "\n");
		
		// Get the number of siblings
		
		outputString.append( "Number of Siblings: " + theFile.getSiblingCount() + "\n");
		
		// Get the parent of this node
		
		outputString.append("The parent: " + theFile.getParent() + "\n");
		
		// Get the next node
		
		outputString.append("Next Node: " + theFile.getNextNode() + "\n");
		
		// Get the previous node
		
		outputString.append( "Next Node: " + theFile.getPreviousNode() + "\n");
		
		// Get the children for the node
		
		outputString.append("\nChildren of Node\n");
		
		// children() returns an enumeration that contains all the children
		// This for loop will continue to run as long as there are more elements
		// nextElement() returns the next element in the list
		
		for (Enumeration enumValue = theFile.children(); enumValue.hasMoreElements(); ) {
		
			outputString.append(enumValue.nextElement() + "\n");
			
		}
		
		// Get the path from the root
		
		outputString.append("\nPath From Root\n");
		
		// getPath returns an array of TreeNodes
		
		TreeNode[] pathNodes = theFile.getPath();
		
		// Cycle through the TreeNodes
		
		for(TreeNode indivNodes: pathNodes){
			outputString.append(indivNodes + "\n");
		}
		
		JOptionPane.showMessageDialog(DrivingTree.this, outputString, "Information", JOptionPane.INFORMATION_MESSAGE);
		
		outputString.setLength(0);
		
	
	}


class TreeListener implements TreeSelectionListener {

	@Override
	public void valueChanged(TreeSelectionEvent arg0) {
		// TODO Auto-generated method stub
		
	}
	
}
}
