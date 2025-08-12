import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s=sc.nextLine();

        int[] id=new int[26];
        Arrays.fill(id,-1);

        for(int i=0;i<s.length();i++){
            int k=(int)s.charAt(i)-97;
            if(id[k]==-1){
                id[k]=i;
            }
        }
        for(int i=0;i<26;i++){
            System.out.print(id[i]+" ");
        }

    }
}