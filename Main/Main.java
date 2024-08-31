
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);

        String a = in.nextLine();
        String b = in.nextLine();
        int answer = 0;

        HashMap<Character, Integer> amap = new HashMap<>();
        HashMap<Character, Integer> bmap = new HashMap<>();

        for (int i = 0; i < a.length(); i++) {
            if (amap.containsKey(a.charAt(i)))
                amap.put(a.charAt(i), amap.get(a.charAt(i)) + 1);
            else
                amap.put(a.charAt(i), 1);
        }

        for (int i = 0; i < b.length(); i++) {
            if (bmap.containsKey(b.charAt(i)))
                bmap.put(b.charAt(i), bmap.get(b.charAt(i)) + 1);
            else
                bmap.put(b.charAt(i), 1);
        }

        for (Character c: amap.keySet())
            if (!bmap.containsKey(c))
                answer += amap.get(c);
            else
                answer += Math.abs(amap.get(c) - bmap.get(c));
        
        for (Character c: bmap.keySet())
            if (!amap.containsKey(c))
                answer += bmap.get(c);

        
        System.out.println(answer);
    }
}
