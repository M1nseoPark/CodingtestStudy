
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        int sum = 0;

        for (int i = 0; i < 5; i++) {
            int x = in.nextInt();
            list.add(x);
            sum += x;
        }

        list.sort(Comparator.naturalOrder());

        System.out.println(sum / 5);
        System.out.println(list.get(2));
    }
}
