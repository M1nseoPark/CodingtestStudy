
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong();
        long b = in.nextLong();

        if (a == b) 
            System.out.println(0);
        else {
            System.out.println(Math.max(a, b) - Math.min(a, b) - 1);

            for (long i = Math.min(a, b) + 1; i < Math.max(a, b); i++) 
                System.out.print(i + " ");
        }
    }
}
