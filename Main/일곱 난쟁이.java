// import java.util.*;


// public class Main {
//     public static void main(String[] arg) {
//         Scanner in = new Scanner(System.in);
//         List<Integer> list = new ArrayList<>();
//         int sum = 0;

//         for (int i = 0; i < 9; i++) {
//             int x = in.nextInt();
//             list.add(x);
//             sum += x;
//         }

//         boolean flag = true;

//         for (int i = 0; i < 8; i++) {
//             for (int j = i + 1; j < 9; j++) {
//                 if ((list.get(i) + list.get(j)) == (sum - 100)) {
//                     list.set(i, 0);
//                     list.set(j, 0);
//                     flag = false;
//                 }

//                 if (!flag)
//                     break;
//             }

//             if (!flag)
//                 break;
//         }

//         list.sort(Comparator.naturalOrder());
//         for (int i = 2; i < 9; i++)
//             System.out.println(list.get(i));
//     }
// }
