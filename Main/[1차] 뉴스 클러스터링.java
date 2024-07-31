import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        ArrayList<String> A = new ArrayList<>();
        ArrayList<String> B = new ArrayList<>();
        ArrayList<String> union = new ArrayList<>();
        ArrayList<String> intersection = new ArrayList<>();

        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        for (int i = 0; i < str1.length()-1; i++) {
            char first = str1.charAt(i);
            char second = str1.charAt(i + 1);
            
            if (first >= 'a' && first <= 'z' && second >= 'a' && second <= 'z')
                A.add(first + "" + second);
        }
        
        for (int i = 0; i < str2.length()-1; i++) {
            char first = str2.charAt(i);
            char second = str2.charAt(i + 1);
            
            if (first >= 'a' && first <= 'z' && second >= 'a' && second <= 'z')
                B.add(first + "" + second);
        }
        
        Collections.sort(A);
        Collections.sort(B);

        for (String s : A) {
            if (B.remove(s))
                intersection.add(s);
            union.add(s);
        }

        for (String s : B) {
            union.add(s);
        }

        double answer = 0;

        if (union.size() == 0)
            answer = 1;
        else
            answer = (double) intersection.size() / (double) union.size();

        return (int)(answer * 65536);
    }
}