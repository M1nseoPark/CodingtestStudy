
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) 
            arr.add(in.nextInt());

        int v = in.nextInt();
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (arr.get(i) == v)
                answer += 1;
        }

        System.out.println(answer);
    }
}

