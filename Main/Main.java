
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int x = 2 * n;

        for (int i = 1; i < n; i++) 
            System.out.println("*".repeat(i) + " ".repeat(x-2*i) + "*".repeat(i));
        
        System.out.println("*".repeat(x));

        for (int i = n-1; i > 0; i--) 
            System.out.println("*".repeat(i) + " ".repeat(x-2*i) + "*".repeat(i));
    }
}



// *********
//  ******* (1)
//   ***** (2)
//    *** (3)
//     * (4)