import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();
        int[] scores = new int[n];
        for(int i = 0; i < n; i++){
            scores[i] = sc.nextInt();
            sc.nextLine();
        }
        int[] dp = new int[n];
        dp[0]=scores[0];
        if(n>=2){
            dp[1]=scores[0]+scores[1];
            if(n>=3){
                dp[2]=Math.max(scores[0]+scores[2],scores[1]+scores[2]);
                if(n>3){
                    for(int i = 3; i < n; i++){
                        dp[i]=Math.max(dp[i-2],dp[i-3]+scores[i-1])+scores[i];
                    }
                }
            }
        }

        System.out.println(dp[n-1]);
    }
}