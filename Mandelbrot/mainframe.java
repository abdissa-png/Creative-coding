import javax.swing.JFrame;

public class mainframe extends JFrame{
    mainframe(){
        mainpanel panel=new mainpanel();
        this.setTitle("Mandelbrot's Set");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.add(panel);
        this.pack();
        this.setLocationRelativeTo(null);
        this.setVisible(true);
        this.setResizable(false);
    }
}
