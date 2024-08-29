
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        int k = in.nextInt();

        int[] boy = new int[7];
        int[] girl = new int[7];
        
        for (int i = 0; i < n; i++) {
            int s = in.nextInt();
            int y = in.nextInt();

            if (s == 1)
                boy[y] += 1;
            else
                girl[y] += 1;
        }
            
        int answer = 0;

        for (int i = 1; i < 7; i++) {
            answer += Math.ceil((double)boy[i] / (double)k);
            answer += Math.ceil((double)girl[i] / (double)k);
        }

        System.out.println(answer);
    }
}

