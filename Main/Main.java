
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        ArrayList<Integer> list = new ArrayList<>();
        int n = a * b * c;

        for (int i = 0; i < 10; i++) 
            list.add(0);

        while (n != 0) {
            int x = n % 10;
            list.set(x, list.get(x)+1);
            n = n / 10;
        }

        for (int i = 0; i < 10; i++)
            System.out.println(list.get(i));
    }
}

