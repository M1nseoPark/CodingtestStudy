
import java.util.*;


public class Main {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        
        int t = in.nextInt();

        for (int i = 0; i < t; i++) {
            String a = in.nextLine();
            String b = in.nextLine();

            if (a.length() != b.length())
                System.out.println("Impossible");
            else {
                HashMap<Character, Integer> amap = new HashMap<>();
                HashMap<Character, Integer> bmap = new HashMap<>();

                for (int j = 0; j < a.length(); j++) {
                    if (amap.containsKey(a.charAt(j)))
                        amap.put(a.charAt(j), amap.get(a.charAt(j)) + 1);
                    else
                        amap.put(a.charAt(j), 1);
                    
                    if (bmap.containsKey(b.charAt(j)))
                        bmap.put(b.charAt(j), bmap.get(b.charAt(j)) + 1);
                    else
                        bmap.put(b.charAt(j), 1);
                }

                for (Character j: amap.keySet())
	                System.out.println(j + amap.get(j));

                for (Character j: bmap.keySet())
	                System.out.println(j + bmap.get(j));

                if (amap.equals(bmap)) 
                    System.out.println("Possible");
                else
                    System.out.println("Impossible");
            }
        }
    }
}

