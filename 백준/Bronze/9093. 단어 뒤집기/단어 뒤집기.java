import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[] sent = new String[n];
        for(int i = 0; i < n; i++){
            sent[i] = sc.nextLine();
        }

        for(String s : sent){
            String[] words = s.split(" ");
            String res = "";
            for(int i = 0; i < words.length; i++){
                StringBuffer sb = new StringBuffer(words[i]);
                res+=sb.reverse()+" ";
            }
            System.out.println(res);
        }

    }
}
