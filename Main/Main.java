
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();

        for (int i = 1; i < n+1; i++) 
            System.out.println("*".repeat(i));
    }
}
