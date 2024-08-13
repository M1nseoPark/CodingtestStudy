
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        int sum = 0;
        int min = 100;

        for (int i = 0; i < 7; i++) {
            int x = in.nextInt();

            if (x % 2 == 1) {
                if (x < min)
                    min = x;
                sum += x;
            }
        }

        if (sum == 0)
            System.out.println("-1");
        else {
            System.out.println(sum);
            System.out.println(min);
        }
    }
}
