// import java.util.*;


// public class Main {
//     public static void main(String[] arg) {
//         Scanner in = new Scanner(System.in);
        
//         int n = in.nextInt();
        
//         List<String> arr = new ArrayList<>();
//         int answer = 1;

//         for (int i = 0; i < 10; i++) 
//             arr.add(Integer.toString(i));

//         while (n > 0) {
//             String t = Integer.toString(n % 10);
//             n = n / 10;

//             if (arr.contains(t))
//                 arr.remove(t);
//             else {
//                 if (t.equals("6") && arr.contains("9"))
//                     arr.remove("9");
//                 else if (t.equals("9") && arr.contains("6"))
//                     arr.remove("6");
//                 else {
//                     answer += 1;
//                     for (int i = 0; i < 10; i++) {
//                         arr.add(Integer.toString(i));
//                         arr.remove(t);
//                     }
//                 }
//             }
//         }
        
//         System.out.println(answer);
//     }
// }

