import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JPanel;


import java.awt.*;
import java.awt.event.*;
import java.util.Random;
public class gamePanel extends JPanel{
    JButton[][] button;
    String key;
    Random random;
    gamePanel(){
        this.setPreferredSize(new Dimension(675,675));
        this.setLayout(new GridLayout(3,3));
        newButtons();
        generateSudoku(button);       
    }
    public boolean solve(JButton[][] button,int row,int column){
        if(row==8 && column==9){
            return true;
        }
        if(row<8 && column==9){
            row+=1;
            column=0;
        }
        if (!button[row][column].isEnabled()){
            return solve(button,row,column+1);
        }
        for(int i=1;i<10;i++){
            if(check(row,column,button,i)){
                button[row][column].setText(Integer.toString(i));
                if (solve(button,row,column+1)){
                    return true;
                }else{
                button[row][column].setText("");
                }
                }
            }
        return false;
    }
    public void generateSudoku(JButton[][] button){
        random=new Random();
        int count=0;
        while(count<20){
            int x=random.nextInt(9);
            int y=random.nextInt(9);
            int n=random.nextInt(1, 10);
            if (check(x,y,button,n) && button[x][y].getText()==""){
                button[x][y].setText(Integer.toString(n));
                button[x][y].setEnabled(false);
                count+=1;
            }

        }
    }
    public boolean checkFinish(JButton[][] button){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                String str=button[i][j].getText();
                if (str==""){
                    return false;
                }
            }
        }
        return true;
    }
    public void setInactive(JButton[][] button){
        for(JButton[] buttons:button){
            for(JButton minibutton:buttons){
                minibutton.setEnabled(false);
            }
        }
    }
    public boolean check(int row,int column,JButton[][] button,int num){
        for(int i=0;i<9;i++){
            if(button[row][i].getText()!=""){
                if (Integer.valueOf(button[row][i].getText())==num){
                    return false;
                }
            }
        }
        for(int j=0;j<9;j++){
            if(button[j][column].getText()!=""){
            if (Integer.valueOf(button[j][column].getText())==num){
                return false;
            }
        }
        }
        row=row-(row%3);
        column=column-(column%3);
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(button[row+i][column+j].getText()!=""){
                    if (Integer.valueOf(button[row+i][column+j].getText())==num){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    public boolean entryCheck(JButton minibutton,int num){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(button[i][j]==minibutton){
                    return check(i,j,button,num);
                }
            }
        }
        return true;                
    }
    public void newButtons(){
        button=new JButton[9][9];
        int i=-3;
        for(int count=0;count<3;count++){
            i=i+3;
            int j=0;
        for (int m=0;m<3;m++){
            JPanel panel=new JPanel(new GridLayout(3,3));
            panel.setPreferredSize(new Dimension(225,225));
            Random random=new Random();
            panel.setBackground(new Color(random.nextInt(255),random.nextInt(255),random.nextInt(255)));
            for(int k=i;k<i+3;k++){
                for(int l=j;l<j+3;l++){
                    button[k][l]=new JButton();
                    button[k][l].setSize(75, 75);
                    button[k][l].setFont(new Font("MV Boli",Font.BOLD,50));
                    button[k][l].setHorizontalAlignment(JButton.CENTER);
                    button[k][l].setBackground(Color.CYAN);
                    panel.add(button[k][l]);                                        
            }
            panel.setBorder(BorderFactory.createLineBorder(Color.BLACK));            
        }
        j=j+3;
        this.add(panel);
    }
}
            for(JButton[] buttons:button){
                for(JButton minibutton:buttons){
                minibutton.addKeyListener(new KeyListener(){
                    public void keyPressed(KeyEvent e){
                        switch(e.getKeyCode()){
                            case KeyEvent.VK_1:
                                if(entryCheck(minibutton,1)){
                                    minibutton.setText("1");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_2:
                                if(entryCheck(minibutton,2)){
                                    minibutton.setText("2");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_3:
                                if(entryCheck(minibutton,3)){
                                    minibutton.setText("3");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_4:
                                if(entryCheck(minibutton,4)){
                                    minibutton.setText("4");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_5:
                                if(entryCheck(minibutton,5)){
                                    minibutton.setText("5");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_6:
                                if(entryCheck(minibutton,6)){
                                    minibutton.setText("6");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_7:
                                if(entryCheck(minibutton,7)){
                                    minibutton.setText("7");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_8:
                                if(entryCheck(minibutton,8)){
                                    minibutton.setText("8");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                            case KeyEvent.VK_9:
                                if(entryCheck(minibutton,9)){
                                    minibutton.setText("9");
                                }
                                if(checkFinish(button)){
                                    setInactive(button);
                                }
                                break;
                    }

                     
                    
                
                }

                    @Override
                    public void keyTyped(KeyEvent e) {
                        // TODO Auto-generated method stub
                        
                    }

                    @Override
                    public void keyReleased(KeyEvent e) {
                        // TODO Auto-generated method stub
                        
                    }});
            }
        }
        }

    }
