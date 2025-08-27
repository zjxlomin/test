import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word =  sc.nextLine();

        int L = word.length();
        String[] suffix = new  String[L];
        for(int i=0;i<L;i++){
            suffix[i]=word.substring(i,L);
        }
        Arrays.sort(suffix);
        for(String str:suffix){
            System.out.println(str);
        }
    }
}