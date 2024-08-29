
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) 
            arr.add(in.nextInt());

        int x = in.nextInt();
        arr.sort(Comparator.naturalOrder());
        int answer = 0;

        int left = 0;
        int right = n-1;

        while (left < right) {
            int temp = arr.get(left) + arr.get(right);

            if (temp == x) {
                left += 1;
                right -= 1;
                answer += 1;
            }
            else if (temp > x)
                right -= 1;
            else
                left += 1;
        }

        System.out.println(answer);
    }
}

