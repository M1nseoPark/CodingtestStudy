
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int y = 0;
        int m = 0;

        for (int i = 0; i < n; i++) {
            int time = in.nextInt();

            y += (time / 30 + 1) * 10;
            m += (time / 60 + 1) * 15;
        }
        
        if (y == m) 
            System.out.println("Y M " + y);
        else if (y < m)
            System.out.println("Y " + y);
        else
            System.out.println("M " + m);
    
    }
}
