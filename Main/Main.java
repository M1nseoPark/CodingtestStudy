
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            String input = in.nextLine();
            String[] arr = input.split(" ");
            int cnt = 0;

            for (int j = 0; j < 4; j++) {
                if (arr[j].equals("0"))
                    cnt++;
            }

            if (cnt == 4)
                System.out.println("D");
            else if (cnt == 3)
                System.out.println("C");
            else if (cnt == 2)
                System.out.println("B");
            else if (cnt == 1)
                System.out.println("A");
            else
                System.out.println("E");
        }
    }
}
