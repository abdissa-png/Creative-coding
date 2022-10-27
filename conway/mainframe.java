import javax.swing.JFrame;

public class mainframe extends JFrame{
    mainpanel newpanel=new mainpanel();
    mainframe(){
        this.setTitle("Conway game");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.add(newpanel);
        this.pack();
        this.setVisible(true);
        this.setResizable(false);
        this.setLocationRelativeTo(null);
    }
}
