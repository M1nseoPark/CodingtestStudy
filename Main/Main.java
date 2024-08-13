
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        if (a == b && b == c && a == c)
            System.out.println(10000 + a * 1000);
        else if (a == b && b != c)
            System.out.println(1000 + a * 1000);
        else if (b == c && a != b)
            System.out.println(1000 + b * 1000);
        else if (a == c && b != c)
            System.out.println(1000 + a * 1000);
        else
            System.out.println(Math.max(a, Math.max(b, c)) * 100);
    }
}
