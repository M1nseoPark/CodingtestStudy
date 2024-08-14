
import java.io.*;


public class Main {
    public static void main(String[] arg) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            int test = Integer.parseInt(br.readLine());

            for (int i = 0; i < test; i++) {
                String[] input = br.readLine().split(" ");
                int a = Integer.parseInt(input[0]);
                int b = Integer.parseInt(input[1]);

                bw.write((a + b) + "");
                bw.write("\n");
            }
        
            bw.flush();
            bw.close();
        } 
        catch (Exception e) { }
    }
}
