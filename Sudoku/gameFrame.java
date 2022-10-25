import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import java.awt.event.*;
public class gameFrame extends JFrame {
    gameFrame(){
    this.setDefaultCloseOperation(EXIT_ON_CLOSE);
    this.setTitle("Soduku");
    gamePanel gamepanel=new gamePanel();
    JMenuBar bar=new JMenuBar();
    JMenu utility=new JMenu("Utility");
    JMenuItem solve=new JMenuItem("Solve");
    JMenuItem newgame=new JMenuItem("New game");
    newgame.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent e) {
           new gameFrame();
           dispose();
            }
        });
    solve.addActionListener(new ActionListener(){
    public void actionPerformed(ActionEvent e) {
            gamepanel.solve(gamepanel.button,0,0);
        }
    });
    utility.add(solve);
    utility.add(newgame);
    bar.add(utility);
    this.setJMenuBar(bar);
    this.add(gamepanel);
    this.pack();
    this.setLocationRelativeTo(null);
    this.setResizable(false);
    this.setVisible(true);
    }
    
}
