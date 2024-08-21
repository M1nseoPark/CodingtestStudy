
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        
        List<Integer> list = new ArrayList<>();
        int max = 0;
        int idx = 0;

        for (int i = 0; i < 9; i++) {
            int n = in.nextInt();
            list.add(n);

            if (n > max) {
                max = n;
                idx = i;
            }
        }

        System.out.println(max);
        System.out.println(idx+1);
    }
}

