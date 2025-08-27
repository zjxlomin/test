import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[][] words = new String[n][2];
        for(int i = 0; i < n; i++){
            String str =  sc.nextLine();
            words[i] = str.split(" ");
        }

        for(int i = 0; i < n; i++){
            String a = words[i][0];
            String b = words[i][1];
            String[] aChar = a.split("");
            String[] bChar = b.split("");
            Arrays.sort(aChar);
            Arrays.sort(bChar);
            if(Arrays.equals(aChar, bChar)){
                System.out.println(a+" & "+b+" are anagrams.");
            }
            else{
                System.out.println(a+" & "+b+" are NOT anagrams.");
            }
        }
    }
}
