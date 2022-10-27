import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.*;
import javax.swing.JPanel;
import java.awt.Graphics;



public class mainpanel extends JPanel implements MouseMotionListener,Runnable{
    Thread mainthread;
    boolean running;
    int[][] MATRIX=new int[50][50];
    static int UNIT_SIZE=10;
    static int SCREEN_HEIGHT=500;
    static int SCREEN_WIDTH=500;
    Graphics g;
    mainpanel(){
        for(int i=0;i<MATRIX.length;i++){
            for(int j=0;j<MATRIX[0].length;j++){
            MATRIX[i][j]=0;
            }
        }
        MATRIX[24][25]=1;
        MATRIX[25][25]=1;
        MATRIX[26][25]=1;
        MATRIX[25][24]=1;
        MATRIX[25][26]=1;
        this.setPreferredSize(new Dimension(SCREEN_WIDTH,SCREEN_HEIGHT));
        this.setBackground(Color.BLACK);
        this.setFocusable(true);
        this.addMouseMotionListener(this);
        this.paint(g);
        running=false;
        mainthread=new Thread(this);
        mainthread.start();
    }
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        draw(g);
    }
    public void checkConditions(){
        for(int row=0;row<MATRIX.length;row++){
            for(int column=0;column<MATRIX[0].length;column++){
                for(int i=-1;i<2;i++){
                    for(int j=-1;j<2;j++){
                        if(i==0 && j==0){
                            continue;
                        }
                        else if(row+i>=MATRIX.length && column+j>=MATRIX[0].length){
                            if(MATRIX[(row+i)-MATRIX.length][(column+j)-MATRIX[0].length]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)-MATRIX.length][(column+j)-MATRIX[0].length]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }
                        else if(row+i>=MATRIX.length && column+j<MATRIX[0].length && column+j>=0){
                            if(MATRIX[(row+i)-MATRIX.length][(column+j)]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)-MATRIX.length][(column+j)]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }
                        else if(row+i>=MATRIX.length && column+j<0){
                            if(MATRIX[(row+i)-MATRIX.length][(column+j)+MATRIX[0].length]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)-MATRIX.length][(column+j)+MATRIX[0].length]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }
                        else if(row+i<MATRIX.length && row+i>=0 && column+j<0){
                            if(MATRIX[(row+i)][(column+j)+MATRIX[0].length]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)][(column+j)+MATRIX[0].length]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }
                        else if(row+i<0 && column+j<0){
                            if(MATRIX[(row+i)+MATRIX.length][(column+j)+MATRIX[0].length]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)+MATRIX.length][(column+j)+MATRIX[0].length]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }
                        else if(row+i<0 && column+j>=0 && column+j<MATRIX[0].length){
                            if(MATRIX[(row+i)+MATRIX.length][(column+j)]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)+MATRIX.length][(column+j)]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }else if(row+i<0 && column+j>=MATRIX[0].length){
                            if(MATRIX[(row+i)+MATRIX.length][(column+j)-MATRIX[0].length]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)+MATRIX.length][(column+j)-MATRIX[0].length]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }else if(row+i>=0 && row+i<MATRIX.length && column+j>=MATRIX[0].length){
                            if(MATRIX[(row+i)][(column+j)-MATRIX[0].length]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)][(column+j)-MATRIX[0].length]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }
                        }
                        else{
                            if(MATRIX[(row+i)][(column+j)]>0 && MATRIX[row][column]>0){
                                MATRIX[row][column]+=1;
                            }else if(MATRIX[(row+i)][(column+j)]>0 && MATRIX[row][column]<=0){
                                MATRIX[row][column]-=1;
                            }

                        }
                    }
                }
                
            }
        }
        for(int row=0;row<MATRIX.length;row++){
            for(int column=0;column<MATRIX[0].length;column++){
                if(MATRIX[row][column]>0){
                    if(MATRIX[row][column]-1<2){
                        MATRIX[row][column]=0;
                    }else if (MATRIX[row][column]-1<=3){
                        MATRIX[row][column]=1;
                    }else if((MATRIX[row][column]-1>3)){
                        MATRIX[row][column]=0;
                    }
                }else if(MATRIX[row][column]==0){
                    continue;
                }else{
                    if (MATRIX[row][column]==-3){
                        MATRIX[row][column]=1;
                    }else{
                        MATRIX[row][column]=0;
                    }

                }
            }
        }
    }
    public void draw(Graphics g){
        for(int row=0;row<MATRIX.length;row++){
            for(int column=0;column<MATRIX[0].length;column++){
                if(MATRIX[row][column]==1){
                    g.setColor(Color.WHITE);
                    g.fillRect((int) (column*(SCREEN_HEIGHT/MATRIX.length)),(int) (row*SCREEN_WIDTH/MATRIX[0].length),(int) (SCREEN_WIDTH/MATRIX[0].length),(int) (SCREEN_HEIGHT/MATRIX.length));
                }
        }
    }
    /*for(int i=0;i<SCREEN_HEIGHT/UNIT_SIZE;i++){
        g.setColor(Color.RED);
        g.drawLine(i*UNIT_SIZE, 0, i*UNIT_SIZE, SCREEN_HEIGHT);
        g.drawLine(0,  i*UNIT_SIZE, SCREEN_WIDTH,i*UNIT_SIZE);
    }*/
}

    public void mouseDragged(MouseEvent e) {
        running=false;
        try {
            int y=e.getX()/(mainpanel.SCREEN_WIDTH/MATRIX[0].length);
            int x=e.getY()/(mainpanel.SCREEN_HEIGHT/MATRIX.length);
            if(x<MATRIX[0].length && x>0 && y>0 && y<MATRIX.length){
                MATRIX[x][y]=1;
            }
            repaint();
            running=true;
        } catch (Exception e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }
        
    }
    @Override
    public void mouseMoved(MouseEvent e) {
        // TODO Auto-generated method stub        
    }
    @Override
    public void run() {
        long lastTime=System.nanoTime();
        double amountofTicks=60.0;
        double ns=1000000000/amountofTicks;
        double delta=0;
        while(true){
            long now=System.nanoTime();
            delta+=(now-lastTime)/ns;
            lastTime=now;
            if(delta>=1 && running){
                checkConditions();
                repaint();
            if(delta>=1){
                delta--;
            }
                //System.out.println("TEST");
            }
        }
    
    }
}