import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JPanel;
import java.awt.Graphics;
public class mainpanel extends JPanel implements Runnable {
    Thread mainthread;
    Graphics g;
    Color[] colors={Color.RED,Color.ORANGE,Color.YELLOW,Color.GREEN,Color.BLUE,Color.PINK,Color.MAGENTA};
    static float power=-6;
    static double increament=1;
    static int SCREEN_WIDTH=800;
    static int SCREEN_HEIGHT=800;
    mainpanel(){
        this.setPreferredSize(new Dimension(SCREEN_WIDTH,SCREEN_HEIGHT));
        this.setBackground(Color.GRAY);
        this.setFocusable(true);
        mainthread=new Thread(this);
        mainthread.start();
    }
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        this.removeAll();
        draw(g);
    }
    public void draw(Graphics g){
        for(int i=0;i<SCREEN_WIDTH;i++){
            for(int j=0;j<SCREEN_HEIGHT;j++){
                double[] offset=new double[2];
                double[] array=new double[2];
                array[0]=0;
                array[1]=0;
                offset[0]=(double) (i-SCREEN_HEIGHT/2)/100;
                offset[1]=(double) (j-SCREEN_WIDTH/2)/100;
                if(operation.isMandelbrot(array,power,0,offset)){

                    g.setColor(Color.BLACK);
                    g.fillRect(i, j, 1, 1);
                }else{
                    g.setColor(colors[operation.counter%7]);
                    g.fillRect(i, j, 1, 1);
                }
            }
        }
        power+=(float) increament;
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
            if(delta>=0.1){
                repaint();
            }
        }
    }
    
}
