
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);

        String str = in.nextLine();
        int m = in.nextInt();

        StringBuilder left = new StringBuilder();
        left.append(str);
        StringBuilder right = new StringBuilder();

        for (int i = 0; i < m; i++) {
            String a = in.next();
            String b = "";

            if (a.equals("L") && left.length() != 0)  {
                right.insert(0, left.charAt(left.length()-1));
                left.deleteCharAt(left.length()-1);
            }
            else if (a.equals("D") && right.length() != 0) {
                left.append(right.charAt(0));
                right.deleteCharAt(0);
            }
            else if (a.equals("B") && left.length() != 0) {
                left.deleteCharAt(left.length()-1);
            }
            else if (a.equals("P")) {
                b = in.next();
                left.append(b);
            }
        }
        
        System.out.println(left + "" + right);
    }
}
