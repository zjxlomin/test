import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[] words = new String[n];
        for(int i = 0; i < n; i++){
            words[i] = sc.nextLine();
        }

        int res = 0;
        for(String word : words){
            boolean isGroup = true;
            int L =  word.length();
            List<Character> chars = new ArrayList<>();
            char x;
            for(int i = 0; i < L; i++){
                x=word.charAt(i);
                if(!chars.contains(x)){
                    chars.add(x);
                }
                else{
                    if(word.charAt(i-1)!=x){
                        isGroup = false;
                        break;
                    }
                }
            }
            if(isGroup){ res++; }
        }
        System.out.println(res);
    }
}
