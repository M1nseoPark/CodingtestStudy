import java.util.*;

public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x = in.nextInt();

        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            if (num < x)
                arr.add(num);
        }

        for (int i = 0; i < arr.size(); i++) {
            System.out.print(Integer.toString(arr.get(i)) + " ");
        }
    }
}
