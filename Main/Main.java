
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();

        for (int i = 1; i < 21; i++)
            list.add(i);

        for (int i = 0; i < 10; i++) {
            int s = in.nextInt();
            int e = in.nextInt();

            Collections.reverse(list.subList(s-1, e));
        }
        
        for (int i = 0; i < 20; i++) 
            System.out.print(list.get(i) + " ");
    }
}
