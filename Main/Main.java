
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();

        for (int i = 0; i < 2*n; i+=2) {
            System.out.println(" ".repeat(i/2) + "*".repeat(2*n-1-i));
        } 
            
    }
}



// *********
//  ******* (1)
//   ***** (2)
//    *** (3)
//     * (4)