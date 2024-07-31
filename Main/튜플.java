import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();

        // 맨 앞의 {{를 제거함 
        s = s.substring(2, s.length());

        // 맨 뒤의 }}를 제거한 뒤, },{ 형태의 문자열을 -로 바꿈 
        // {{2},{2,1},{2,1,3},{2,1,3,4}}
        s = s.substring(0, s.length()-2).replace("},{", "-");

        String str[] = s.split("-");
        // 나눠진 문자열 배열을 길이에 따라 다시 정렬함 
        Arrays.sort(str, new Comparator<String>() {
            public int compare(String o1, String o2) {
                return Integer.compare(o1.length(), o2.length());
            }
        });

        for (String x : str) {
            String[] temp = x.split(",");

            for (int i = 0; i < temp.length; i++) {
                int n = Integer.parseInt(temp[i]);
                if (!answer.contains(n))
                    answer.add(n);
            }
        }

        return answer;
    }
}